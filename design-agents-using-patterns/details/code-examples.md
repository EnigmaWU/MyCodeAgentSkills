# Framework Implementation Templates (ADK & LangChain)

This document provides verified Python orchestration templates for implementing key agentic design patterns.

---

## 1. Google Agent Development Kit (ADK) Templates

Google's ADK uses a declarative approach where agents are configured with distinct tools and sub-agents, and a runner manages their sessions and execution event loops.

### Coordinator-Specialist Topology with Tools

```python
import uuid
from typing import Dict, Any, Optional
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool
from google.genai import types

# 1. Define Tool Functions
def search_database_handler(query: str) -> str:
    """
    Searches the primary database for record information.
    Args:
        query: Search term or record ID.
    """
    # Real implementation or safety check goes here
    return f"Database query result for '{query}'"

# 2. Wrap in Function Tools
db_tool = FunctionTool(search_database_handler)

# 3. Define Specialist Sub-Agent
specialist_agent = Agent(
    name="DB_Specialist",
    model="gemini-2.5-flash",
    description="A specialist agent that queries the database for records.",
    tools=[db_tool]
)

# 4. Define Coordinator Agent (Auto-Delegation enabled by sub_agents)
coordinator_agent = Agent(
    name="Coordinator",
    model="gemini-2.5-flash",
    instruction=(
        "You are the main coordinator. Your role is to analyze the user's request "
        "and delegate to DB_Specialist if they are asking for database records. "
        "Do not answer queries about database records yourself."
    ),
    description="Main entrypoint coordinator.",
    sub_agents=[specialist_agent]
)

# 5. Execution Runner helper
async def run_adk_agent(request_text: str):
    runner = InMemoryRunner(app_name="AgenticApp", root_agent=coordinator_agent)
    user_id = "user_456"
    session_id = str(uuid.uuid4())
    
    await runner.session_service.create_session(
        app_name=runner.app_name, 
        user_id=user_id, 
        session_id=session_id
    )
    
    # Run the event loop
    events = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=types.Content(
            role='user',
            parts=[types.Part(text=request_text)]
        )
    )
    
    for event in events:
        # Handle events (state changes, tool calls, model outputs)
        if event.type == "model_response":
            print(event.data)
```

---

## 2. LangChain & LangGraph (LCEL) Templates

LangChain uses LangChain Expression Language (LCEL) to chain prompts, LLMs, and output parsers. Branching routes use `RunnableBranch` or conditional state transitions in graphs.

### Intent Router using `RunnableBranch`

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch

# 1. Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# 2. Define Specialist Chains
def sql_handler(state: dict) -> str:
    # SQL query logic goes here
    return f"Processed query '{state['request']}' via SQL."

def nosql_handler(state: dict) -> str:
    # NoSQL query logic goes here
    return f"Processed query '{state['request']}' via NoSQL."

def general_handler(state: dict) -> str:
    return f"Processed query '{state['request']}' via General Knowledge."

# 3. Create the Router Classifier Chain
router_prompt = ChatPromptTemplate.from_messages([
    ("system", """Analyze the query and classify it.
    - If it requires structured relational querying or table lookups, output 'sql'.
    - If it is document-oriented or key-value lookup, output 'nosql'.
    - For all other questions, output 'general'.
    ONLY output one word: 'sql', 'nosql', or 'general'."""),
    ("user", "{request}")
])

router_chain = router_prompt | llm | StrOutputParser()

# 4. Define the Branches
branches = {
    "sql": RunnablePassthrough.assign(output=sql_handler),
    "nosql": RunnablePassthrough.assign(output=nosql_handler),
    "general": RunnablePassthrough.assign(output=general_handler),
}

# 5. Create the RunnableBranch
delegation_branch = RunnableBranch(
    (lambda x: x['decision'].strip() == 'sql', branches["sql"]),
    (lambda x: x['decision'].strip() == 'nosql', branches["nosql"]),
    branches["general"] # Default fallback branch
)

# 6. Assemble the Coordinator Runnable
coordinator_chain = {
    "decision": router_chain,
    "request": RunnablePassthrough()
} | delegation_branch | (lambda x: x['output'])

# Example Invocation
# result = coordinator_chain.invoke({"request": "Find order #12345 in the orders table."})
# print(result)
```

---

## 3. Loop Safety & Reflection Template (Pure Python/LangChain)

How to implement an evaluation-generation loop with a hard retry limit.

```python
from typing import Dict, Any, Tuple

def generate_code_draft(prompt: str) -> str:
    # Call generator model
    return "def add(a, b): return a + b"

def evaluate_code(code: str) -> Tuple[bool, str]:
    # Evaluate code against strict criteria
    # Returns (success, feedback)
    if "return a + b" in code:
        return True, "Code is correct."
    return False, "Error: missing summation logic."

def run_self_correcting_generation(user_request: str, max_retries: int = 3) -> str:
    current_prompt = user_request
    state = {
        "draft": "",
        "feedback": "",
        "retry_count": 0,
        "success": False
    }
    
    # Enforce strict iteration bounds
    while state["retry_count"] < max_retries:
        state["draft"] = generate_code_draft(current_prompt)
        success, feedback = evaluate_code(state["draft"])
        
        if success:
            state["success"] = True
            break
            
        state["retry_count"] += 1
        state["feedback"] = feedback
        # Construct refined prompt using evaluator feedback
        current_prompt = f"{user_request}\n\nPrevious Attempt:\n{state['draft']}\n\nFeedback:\n{feedback}\nPlease fix the error."
        print(f"Reflection iteration {state['retry_count']} failed. Feedback: {feedback}")
        
    if not state["success"]:
        # Fallback / Escalation pathway
        print("Max reflection retries reached. Executing fallback.")
        return f"Warning: Best effort draft after {max_retries} attempts: {state['draft']}"
        
    return state["draft"]
```

---

## 4. Coding Agent System Examples

This section provides configuration templates and implementation scripts for interactive IDE coding tools and collaborative multi-agent code-generation pipelines.

### A. Continue config.yaml Custom Agent & MCP Configuration

Template for configuring custom agents, system prompts, and Model Context Protocol (MCP) context servers in `~/.continue/config.yaml`.

```yaml
# ~/.continue/config.yaml
models:
  - name: CustomRefactorAgent
    provider: openai
    model: gpt-4o
    chatOptions:
      temperature: 0.2
      # Establish clear persona guidelines
      baseAgentSystemMessage: |
        You are a senior software engineer specialized in refactoring.
        Provide type annotations, clean interfaces, and respect memory/execution limits.
        Do not use external libraries unless already present in the workspace.

# Context Providers enable inserting specific context using '@' in chat
contextProviders:
  - name: code
    params: {}
  - name: diff
    params: {}
  - name: terminal
    params: {}
  # Expose custom endpoints using the HTTP context provider
  - name: http
    params:
      url: "http://localhost:8080/context-provider"
      title: "internal-docs"
      description: "Queries internal API documentation"

# MCP Servers provide tools and resource discovery protocols
mcpServers:
  sqlite-database:
    type: command
    command: npx
    args:
      - -y
      - "@modelcontextprotocol/server-sqlite"
      - --db-path
      - "/Users/user/workspace/project.db"
```

### B. Cline/Continue-Style Interactive Shell Loop with .clineignore Guards

Python class demonstrating a command execution loop that respects path exclusions (e.g., `.clineignore`), handles user validation cards, and captures shell execution outputs.

```python
import os
import fnmatch
import subprocess
from typing import Dict, Any, Tuple, List

class CodeAgentExecutionGuard:
    def __init__(self, workspace_root: str, ignore_patterns: List[str] = None):
        self.workspace_root = workspace_root
        self.ignore_patterns = ignore_patterns or []
        self.load_ignore_file()

    def load_ignore_file(self):
        ignore_path = os.path.join(self.workspace_root, ".clineignore")
        if os.path.exists(ignore_path):
            with open(ignore_path, "r") as f:
                for line in f:
                    stripped = line.strip()
                    if stripped and not stripped.startswith("#"):
                        self.ignore_patterns.append(stripped)

    def is_ignored(self, file_path: str) -> bool:
        """Checks if a file matches ignore patterns (like .env or secrets)."""
        rel_path = os.path.relpath(file_path, self.workspace_root)
        for pattern in self.ignore_patterns:
            if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(os.path.basename(file_path), pattern):
                return True
        return False

    def prompt_user_approval(self, action: str) -> bool:
        """Simulates an explicit user-in-the-loop approval gate."""
        print(f"\n[SECURITY GATE] Action Requested: {action}")
        choice = input("Approve action? (y/n/abort): ").strip().lower()
        return choice == 'y'

    def write_file_safely(self, target_file: str, content: str) -> bool:
        if self.is_ignored(target_file):
            print(f"Access Denied: File '{target_file}' matches ignore patterns in .clineignore.")
            return False
            
        if not self.prompt_user_approval(f"Write to file {target_file}"):
            return False
            
        # Write to file
        with open(target_file, "w") as f:
            f.write(content)
        return True

    def execute_terminal_command(self, command: str, timeout: int = 30) -> Tuple[int, str, str]:
        """Runs a terminal command capturing stdout and stderr for loop diagnostics."""
        if not self.prompt_user_approval(f"Execute shell command: '{command}'"):
            return -1, "", "Command aborted by user."

        try:
            # Execute within restricted working directory context
            process = subprocess.run(
                command,
                shell=True,
                cwd=self.workspace_root,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return process.returncode, process.stdout, process.stderr
        except subprocess.TimeoutExpired:
            return -1, "", f"Timeout error: Command execution exceeded {timeout}s limit."
        except Exception as e:
            return -1, "", f"Execution error: {str(e)}"
```

### C. OpenCode-Style Specialized Multi-Agent Pipeline

A coordinator orchestrating code generation through a `Scaffolder` (Implementer) and a `ProcessAgent` (Reviewer/Supervisor) evaluating type annotations and style compliance.

```python
class OpenCodeCoordinator:
    def __init__(self):
        self.staging_area = {
            "requirements": "",
            "code_draft": "",
            "logs": [],
            "completed": False
        }

    def run_scaffolder(self, prompt: str) -> str:
        # Simulated generator response
        return "def parse_data(raw_payload: str):\n    return raw_payload.split(',')"

    def run_process_agent_review(self, code: str) -> List[str]:
        # Evaluates code quality against criteria
        issues = []
        if "-> " not in code or ": " not in code:
            issues.append("[REVIEW] Missing type annotations on function parameters or return values.")
        return issues

    def execute_pipeline(self, requirements: str, max_reflections: int = 3) -> Dict[str, Any]:
        self.staging_area["requirements"] = requirements
        current_prompt = requirements
        
        for iteration in range(max_reflections):
            print(f"\n[OpenCode Pipeline] Iteration {iteration + 1}...")
            
            # Scaffolder drafts code
            draft = self.run_scaffolder(current_prompt)
            self.staging_area["code_draft"] = draft
            
            # ProcessAgent reviews
            issues = self.run_process_agent_review(draft)
            if not issues:
                self.staging_area["completed"] = True
                print("Code review passed. No issues found.")
                break
                
            print(f"Code review failed: {issues}")
            self.staging_area["logs"].extend(issues)
            
            # Refine prompt using review logs
            current_prompt = f"{requirements}\n\nPrevious draft:\n{draft}\n\nReview feedback:\n{', '.join(issues)}"
            
        return self.staging_area
```

---

## 5. Agent Memory & State Management

This section provides templates for managing contextual short-term buffers, session scoped states, and persistent storage using the Google Agent Developer Kit (ADK) and generic token compaction.

### A. Google ADK Session Storage Configuration

How to configure session storage persistence using standard ADK services.

```python
# InMemorySessionService (for local development/testing)
from google.adk.sessions import InMemorySessionService
in_memory_sessions = InMemorySessionService()

# DatabaseSessionService (for SQLAlchemy database persistence)
# Requires: pip install google-adk[sqlalchemy]
from google.adk.sessions import DatabaseSessionService
db_url = "sqlite:///./session_memory.db"
persistent_sessions = DatabaseSessionService(db_url=db_url)
```

### B. Scoped State Mutation inside ADK ToolContext

How to update session state variables from within an active ADK tool using prefix scopes (`user:`, `temp:`, and standard session state).

```python
import time
from google.adk.tools.tool_context import ToolContext

def log_user_login(tool_context: ToolContext) -> dict:
    """
    Updates the session state upon a user login event.
    Accesses and modifies the session's state dictionary safely.
    """
    # 1. Access the state dictionary through context
    state = tool_context.state

    # 2. Update session-scoped dynamic variable
    state["task_status"] = "active"

    # 3. Update user-scoped persistent variable (cross-session)
    login_count = state.get("user:login_count", 0) + 1
    state["user:login_count"] = login_count
    state["user:last_login_ts"] = time.time()

    # 4. Set temporary turn-scoped flag (discarded after processing turn)
    state["temp:validation_needed"] = True

    return {
        "status": "success",
        "message": f"User login tracked. Total logins: {login_count}."
    }
```

### C. Short-Term Context Window Token Compaction

A simple helper showcasing how to trim or summarize older conversation history when context limits are reached.

```python
from typing import List, Dict

def compact_conversation_history(
    messages: List[Dict[str, str]], 
    max_tokens: int = 4000, 
    token_estimator_func = len  # Simplified word-count estimator for demonstration
) -> List[Dict[str, str]]:
    """
    Trims/compacts messages list when estimated token count exceeds budget.
    Preserves system message (always first index) and latest active turns.
    """
    system_message = messages[0] if messages and messages[0]["role"] == "system" else None
    active_history = messages[1:] if system_message else messages
    
    total_tokens = sum(token_estimator_func(msg["content"]) for msg in messages)
    
    if total_tokens <= max_tokens:
        return messages

    print(f"Token budget exceeded ({total_tokens}/{max_tokens}). Compacting context...")
    
    # Prune oldest conversation turns until within budget
    while total_tokens > max_tokens and len(active_history) > 2:
        # Prune oldest user-assistant exchange (first 2 elements of history)
        pruned_turn = active_history[:2]
        active_history = active_history[2:]
        total_tokens -= sum(token_estimator_func(msg["content"]) for msg in pruned_turn)

    # Re-assemble with system prompt preserved
    compacted = [system_message] + active_history if system_message else active_history
    return compacted
```



