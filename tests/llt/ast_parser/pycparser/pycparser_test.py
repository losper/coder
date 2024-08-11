# test_module.py
import os
from coder.ast_parser.pycparser.parser import some_function


def test_addition():
    assert some_function(f"""{os.getenv("TEST_ROOT")}/example/c/func.c""") == 0


# from pycparser import c_parser, c_ast

# # 读取 C 代码
# with open('example.c', 'r') as f:
#     text = f.read()

# # 创建解析器并解析代码
# parser = c_parser.CParser()
# ast = parser.parse(text)

# # 打印 AST
# print(ast)
