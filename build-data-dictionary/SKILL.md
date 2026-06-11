---
name: build-data-dictionary
description: >
  WHEN/WHERE/WHO: Database designers, business analysts, or agents analyzing forms, reports, or data-heavy requirements.
  HOW: Use this SKILL to extract domain nouns from text and map them into a strict Data Dictionary (Element Name, Data Type, Length, Allowed Values).
  WHY: Ambiguous data definitions cause integration failures. If system A thinks "Zip Code" is an integer and system B thinks it's a 10-char string, the system crashes.
---

# Build Data Dictionary

## Who
Database Designers, Business Analysts, and AI Agents. The agent uses this skill to formalize data definitions before database schemas are written.

## What
This skill implements the Data Dictionary methodology from *Software Requirements (3rd Edition)*. It scans requirements text for domain nouns (data elements) and constructs a table that defines:
1. **Data Element:** The name of the primitive or structure.
2. **Description:** What it means in the business domain.
3. **Data Type:** String, Integer, Date, Boolean, etc.
4. **Length:** Maximum size.
5. **Allowed Values:** Enums, ranges, or constraints.

## When
Invoke this skill when analyzing UI forms, report specifications, or any requirement involving data input/output. Trigger phrases include: "build a data dictionary," "define the data types," "what are the allowed values for this," or "extract the data model."

## Where
Applies to PRDs, report mockups, UI wireframes, and API specifications.

## Why
A requirement that says "The user shall enter their address" is incomplete. A developer needs to know: Is State a 2-letter abbreviation or the full name? Is Zip Code 5 digits or 9? The Data Dictionary answers these questions definitively.

## Inputs
- Functional requirements, user stories, or UI/report descriptions.

## Output
- A markdown table representing the Data Dictionary.

## Constraints
- Distinguish between **Primitive Data Elements** (e.g., `FirstName`) and **Data Structures** (e.g., `Address = Street + City + State + ZipCode`).
- If a data type or length is unknown, mark it as `TBD` (To Be Determined). Do not guess database-specific implementations (like `VARCHAR(255)`) unless explicitly stated; use logical types like `String (Max 50)`.

## One More Thing
If the input text contains no specific data fields (e.g., "The system shall be fast"), stop and inform the user that a Data Dictionary requires data elements to define.

## How

### Phase 1: Noun Extraction
1. Scan the text for nouns that represent data the system must store, process, or transmit (e.g., "Customer," "Order Date," "SKU").

### Phase 2: Structural Breakdown
2. Identify which nouns are complex **Data Structures** and break them down into their constituent **Primitive Data Elements**.

### Phase 3: Definition Definition
3. For each primitive element, define its Description, Data Type, Length, and Allowed Values. Infer reasonable defaults based on domain knowledge if missing, but clearly mark assumptions.

### Phase 4: Formatting
4. Output the extracted data using the Data Dictionary Format table.

## Resources
- [Data Dictionary Format](./details/data-dictionary-format.md)

## Validation
1. Verify that complex data structures are fully decomposed into primitives.
2. Ensure no fields are left entirely blank (use `TBD` if unknown).
