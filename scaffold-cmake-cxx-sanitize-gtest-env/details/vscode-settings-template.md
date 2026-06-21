# VSCode Settings Template

When scaffolding a new C/C++ project, inject the following configuration into `.vscode/settings.json`. This wires up the CMake Tools extension to automatically use our custom Sanitizer build profiles and configures `clangd`.

```json
{
    "cmake.cmakePath": "cmake",
    "cmake.buildDirectory": "${workspaceFolder}/CMakeBuilt",
    "cmake.debugConfig": {
        "stopAtEntry": true
    },
    "cmake.defaultVariants": {
        "buildType": {
            "default": "DiagASAN",
            "description": "The build type.",
            "choices": {
                "DiagASAN": {
                    "short": "DiagASAN",
                    "long": "Diagnosis in AddressSanitizer",
                    "buildType": "DiagASAN"
                },
                "DiagTSAN": {
                    "short": "DiagTSAN",
                    "long": "Diagnosis in ThreadSanitizer",
                    "buildType": "DiagTSAN"
                },
                "DiagUBSAN": {
                    "short": "DiagUBSAN",
                    "long": "Diagnosis in UndefinedBehaviorSanitizer",
                    "buildType": "DiagUBSAN"
                },
                "DiagMSAN": {
                    "short": "DiagMSAN",
                    "long": "Diagnosis in MemorySanitizer",
                    "buildType": "DiagMSAN"
                },
                "DiagLSAN": {
                    "short": "DiagLSAN",
                    "long": "Diagnosis in LeakSanitizer",
                    "buildType": "DiagLSAN"
                }
            }
        }
    },
    "clangd.arguments": [
        "--compile-commands-dir=${workspaceFolder}/CMakeBuilt",
        "--background-index",
        "--background-index-priority=normal",
        "--clang-tidy"
    ],
    "editor.formatOnSave": true
}
```
