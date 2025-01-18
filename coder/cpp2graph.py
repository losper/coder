import networkx as nx
import uuid
import logging


class CmdState:
    def __init__(self, type, depth) -> None:
        self.uuid = str(uuid.uuid4())
        self.type = type
        self.depth = depth
        self.text = ""
        self.op_num = 0
        pass


class StateMachine:
    def __init__(self):
        self.state = []
        self.root = CmdState("root", 0)
        pass

    def forward(self, cmdState):
        self.state.append(cmdState)
        pass

    def clear(self, depth):
        # 清理已完成的语法状态
        while True:
            if len(self.state) == 0:
                break
            item = self.state[-1]
            if item.depth >= depth:
                self.state.pop()
                continue
            break
        pass

    def last(self):
        if len(self.state) == 0:
            return self.root
        return self.state[-1]


class Cpp2Graph:
    def __init__(self, G: nx.Graph):
        self.depth = 0
        self.G = G
        self.states = StateMachine()
        self.action = {
            "binary_expression": self.binary_expression,
            "number_literal": self.number_literal,
            "function_definition": self.function_definition,
            "identifier": self.identifier,
            "+": self.opeartor_comput,
            "-": self.opeartor_comput,
            "*": self.opeartor_comput,
            "/": self.opeartor_comput,
            "==": self.opeartor_comput,
            "!=": self.opeartor_comput,
            ">": self.opeartor_comput,
            ">=": self.opeartor_comput,
            "<": self.opeartor_comput,
            "<=": self.opeartor_comput,
        }
        pass

    def get_root(self):
        return self.states.root.uuid

    def add_sub_node(self, type, depth):
        tmp = self.states.last()
        inst = CmdState(type, depth)
        self.G.add_edge(tmp.uuid, inst.uuid, type="has")
        pass

    def set_name(self, depth, type, text):
        tmp = self.states.last()
        node = self.G.nodes[tmp.uuid]
        node["text"] = text
        node["type"] = tmp.type
        pass

    def process(self, depth, type, text):

        self.states.clear(depth)
        if type in self.action:
            self.action[type](depth, type, text)
        pass

    def function_definition(self, depth, type, text):
        self.add_sub_node(type, depth)
        pass

    def identifier(self, depth, type, text):
        logging.error(f"{depth}:{type}:{text}")
        self.set_name(depth, type, text)
        pass

    def binary_expression(self, depth, type, text):
        inst = CmdState(type, depth)

        self.states.forward(inst)
        self.G.add_edge(tmp.uuid, inst.uuid)
        logging.info(f"link:{type}:{text}")
        pass

    def number_literal(self, depth, type, text):
        cmdState = self.states.last()
        unique_id = str(uuid.uuid4())
        cur_uuid = cmdState.uuid
        self.G.add_node(unique_id, text=text)
        self.G.add_edge(cur_uuid, unique_id)
        pass

    def opeartor_comput(self, depth, type, text):
        cmdState = self.states.last()
        cur_uuid = cmdState.uuid
        if cur_uuid in self.G.nodes:
            node = self.G.nodes[cur_uuid]
            logging.info(f"set text {cur_uuid} : {text}")
            node["text"] = text
        else:
            logging.error(f"opeartor_comput => could not find {uuid}")
        pass
