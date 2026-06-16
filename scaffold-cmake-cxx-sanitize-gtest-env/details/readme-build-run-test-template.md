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

## 5. VSCode Integrated Testing

You can seamlessly run and debug your Google Tests using VSCode's built-in "Testing" sidebar. 

1. **Install Extensions**: Ensure you have the `CMake Tools` and `C/C++` extensions installed. You may also want to install `C++ TestMate` for deeper test discovery.
2. **Configure CMake**: Open the Command Palette (`Cmd+Shift+P` on macOS) and run `CMake: Configure`.
3. **Build the Tests**: Run `CMake: Build` to compile the test executables.
4. **Discover Tests**: Open the **Testing** activity bar (the beaker icon on the left). VSCode will automatically discover the CTest targets.
5. **Run/Debug**: Click the "Play" icon to run the tests, or the "Bug" icon to debug a specific test. You can set breakpoints directly in your `*.cxx` files.
```
