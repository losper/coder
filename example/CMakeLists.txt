cmake_minimum_required(VERSION 3.10)
project(MyGTestProject)

# 设置C++标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 查找gtest库
find_package(GTest REQUIRED)

# 添加可执行文件
add_library(main src/main.cpp)
# 添加test目录下所有.cpp结尾的文件
file(GLOB_RECURSE TEST_FILES "test/*.cpp")
add_executable(test ${TEST_FILES})

# 链接gtest库
target_link_libraries(main PRIVATE GTest::GTest GTest::Main)
target_link_libraries(test PRIVATE main GTest::GTest GTest::Main)

# 设置编译选项以启用覆盖率
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    target_compile_options(main PRIVATE -fprofile-arcs -ftest-coverage)
    target_compile_options(test PRIVATE -fprofile-arcs -ftest-coverage)
    target_link_libraries(main PRIVATE --coverage)
    target_link_libraries(test PRIVATE --coverage)
endif()

# 设置覆盖率报告生成
add_custom_target(
    coverage
    COMMAND ${CMAKE_COMMAND} --build . --target main
    COMMAND ${CMAKE_COMMAND} --build . --target test
    COMMAND ./test
    COMMAND gcovr --html --html-details index.html -r .. --filter '../src/.*'
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
)
