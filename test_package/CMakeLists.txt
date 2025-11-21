cmake_minimum_required(VERSION 3.19.8)
project(PackageTest CXX)

find_package(cool-concepts CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example cool::concepts)
