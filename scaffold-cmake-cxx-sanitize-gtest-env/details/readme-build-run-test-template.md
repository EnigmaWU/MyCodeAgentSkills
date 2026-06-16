# README_BuildRunTest.md Template

When scaffolding a new C/C++ project, inject the following `README_BuildRunTest.md` into the root directory. Replace `{{PROJECT_NAME}}` with the actual project name.

```markdown
# {{PROJECT_NAME}} - Build, Run, and Test Guide

This project is configured with a robust `CMakeLists.txt` designed to enforce C11/C++17 standards, provide compiler fallbacks (like finding Homebrew LLVM on macOS), and automatically discover Google Test executables.

It also supports compiling with LLVM/GCC Sanitizers to catch memory leaks, data races, and undefined behavior.

## 1. Prerequisites

- **CMake** (v3.16+)
- **Google Test** (`libgtest-dev` on Linux, or installed via Homebrew on macOS)
- A modern C/C++ compiler (GCC or Clang)

## 2. Standard Build & Run

To build the project without any sanitizers:

```bash
mkdir -p build
cd build
cmake ..
make -j$(nproc)
```

## 3. Running Unit Tests

The `CMakeLists.txt` uses a custom `UT_addEachCXX_asTestExe` macro. Simply drop any `*.cxx` file into the `Test/` directory, and it will be compiled into an independent test executable.

```bash
cd build
ctest --output-on-failure
```

*Note: You can also run the individual test executables generated in the `build/Test/` directory directly.*

## 4. Building with Sanitizers

To run your tests and application with strict memory and thread checks, change the `CMAKE_BUILD_TYPE` during the configuration step.

**Address Sanitizer (ASAN)** - Catches out-of-bounds access and use-after-free:
```bash
cmake -DCMAKE_BUILD_TYPE=DiagASAN ..
make clean && make
ctest
```

**Thread Sanitizer (TSAN)** - Catches data races:
```bash
cmake -DCMAKE_BUILD_TYPE=DiagTSAN ..
make clean && make
ctest
```

**Other available profiles:**
- `DiagUBSAN` (Undefined Behavior)
- `DiagMSAN` (Memory Sanitizer - Uninitialized memory)
- `DiagLSAN` (Leak Sanitizer)
```
