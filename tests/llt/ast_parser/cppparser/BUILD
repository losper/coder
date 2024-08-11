load("@rules_cc//cc:defs.bzl", "cc_test")

cc_test(
    name = "cppparser_test",
    srcs = ["cppparser_test.cpp"],
    deps = [
        "//src/cppparser:CppParser",
        "@googletest//:gtest_main",
    ],
)

py_test(
    name = "basic_test",
    srcs = ["basic_test.py"],
    deps = ["//src/cppparser:basic_lib"],
)