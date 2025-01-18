import matplotlib.pyplot as plt
import networkx as nx


def SaveGraphPng(nxg):
    v_labels = nx.get_node_attributes(nxg, "text")
    pos = nx.circular_layout(nxg)
    # 把节点画出来
    nx.draw_networkx_nodes(nxg, pos, node_color="g", node_size=500, alpha=0.8)
    # 把边画出来
    nx.draw_networkx_edges(nxg, pos, width=1.0, alpha=0.5, edge_color="b")
    # 把节点标签画出来
    nx.draw_networkx_labels(nxg, pos, v_labels, font_size=16)
    # 显示图形
    plt.savefig("test.png")
