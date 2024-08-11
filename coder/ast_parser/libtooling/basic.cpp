#include "src/cppparser/CppParser.h"
#include <pybind11/pybind11.h>
#include <vector>

int PyParseFile(const char* cppFile)
{
    return ParseFile(cppFile);
}

PYBIND11_MODULE(basic, module)
{
    module.doc() = "A basic pybind11 extension";
    module.def("PyParseFile", &PyParseFile, "Process a list of strings");
}