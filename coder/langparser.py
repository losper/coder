from tree_sitter import Language, Parser
from .iparser import IParser
import logging


class LangParser(IParser):
    def __init__(self, lang):
        LANGUAGE = Language(lang)
        self.parser = Parser(LANGUAGE)
        # self.parser.set_language(CPP_LANGUAGE)
        self.tree = None
        pass

    def parse_file(self, file_path, callback):
        with open(file_path, "rb") as f:
            source_code = f.read()
        self.tree = self.parser.parse(source_code)
        self.traverse(callback, self.tree.root_node)
        pass

    def parse_string(self, ctx, callback):
        self.tree = self.parser.parse(bytes(ctx, "utf8"))
        self.traverse(callback, self.tree.root_node)
        pass

    def traverse(self, callback, node, depth=0):
        if callback(depth, node.type, node.text.decode("utf-8")):
            return
        # 获取当前节点的子节点数量
        child_count = node.child_count

        # 遍历所有子节点
        for i in range(child_count):
            child_node = node.child(i)
            self.traverse(callback, child_node, depth + 1)
