cmake_minimum_required(VERSION 3.17 FATAL_ERROR)

project(OptiRoute-live-transport-network-monitor)

# Dependencies
# If dependencies are managed with conan, we prepend current build folder 
# to the CMake module patch, where CMake looks for dependencies. 
if(EXISTS ${CMAKE_CURRENT_BINARY_DIR}/conaninfo.txt)
    list(PREPEND CMAKE_MODULE_PATH "$CMAKE_CURRENT_BINARY_DIR")
endif()

set(SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp")

add_executable(OptiRoute-live-transport-network-monitor ${SOURCES})
target_compile_features(OptiRoute-live-transport-network-monitor
    PRIVATE
        cxx_std_11
)