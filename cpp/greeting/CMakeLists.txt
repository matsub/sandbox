cmake_minimum_required (VERSION 2.8)
project (greeting)

# SET COMPILER OPTIONS
# --------------------
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_FLAGS "-W -Wall -O2")

# SOLVE PATHS
# -----------
include_directories(.)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# BUILD BINARIES
# --------------
add_subdirectory(src/greeting)

# hello
add_executable(hello src/hello.cpp)
target_link_libraries(hello greeting)

# hi
add_executable(hi src/hi.cpp)
target_link_libraries(hi greeting)

# test
add_executable(test test/gtest_example.cpp)
target_link_libraries(test
    pthread
    /usr/local/lib/libgtest.a
    /usr/local/lib/libgtest_main.a
    )
