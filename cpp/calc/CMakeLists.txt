cmake_minimum_required (VERSION 2.8)
project (calc)

# compiler settings
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_FLAGS "-W -Wall -O2")

# path solves
include_directories(.)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# main
add_subdirectory(src/calc)
add_executable(print src/print.cpp)
target_link_libraries(print calc)
