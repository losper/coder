import pytest
from coder.cpp2graph import Cpp2Graph
from coder.langparser import LangParser
from coder.visval import SaveGraphPng
import tree_sitter_cpp as tsc
import networkx as nx


def test_add():
    nxg = nx.DiGraph()
    exp = Cpp2Graph(nxg)
    cpp = LangParser(tsc.language())
    cpp.parse_string(
        """
    #include <iostream>
    int foo(){
        return 0;
    }
    int boo(){
        return 1;
    }
    int main(){
        foo();
        boo();
    }
    """,
        exp.process,
    )
    SaveGraphPng(nxg)
