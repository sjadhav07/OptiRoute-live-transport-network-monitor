cmake_minimum_required(VERSION 3.17 FATAL_ERROR)

project(OptiRoute-live-transport-network-monitor)

set(SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp")

add_executable(OptiRoute-live-transport-network-monitor ${SOURCES})
target_compile_features(OptiRoute-live-transport-network-monitor
    PRIVATE
        cxx_std_11
)