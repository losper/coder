from pycparser import c_parser, c_ast


def some_function(path: str):
    # 读取 C 代码
    with open(path, "r") as f:
        text = f.read()

    # 创建解析器并解析代码
    parser = c_parser.CParser()
    ast = parser.parse(text)

    # 打印 AST
    print(ast)
    return 0
