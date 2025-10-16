import random 
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# State
class State(TypedDict):
    graph_state: str

# Conditional edge
def decide_mood(state) -> Literal["node_2", "node_3", "node_4"]:

    # Often, we will use state to decide on the next node to visit
    user_input = state['graph_state'] 

    # Randomly choose between nodes 2, 3, and 4 with roughly equal probability
    r = random.random()
    if r < 0.34:
        return "node_2"
    if r < 0.67:
        return "node_3"
    return "node_4"

# Nodes
def node_1(state):
    print("---Node 1---")
    return {"graph_state":state['graph_state'] +" I love"}

def node_2(state):
    print("---Node 2---")
    return {"graph_state":state['graph_state'] +" BMS!"}

def node_3(state):
    print("---Node 3---")
    return {"graph_state":state['graph_state'] +" ECE course!"}

def node_4(state):
    print("---Node 4---")
    return {"graph_state":state['graph_state'] +" LLM Course!"}

# Build graph
builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_node("node_4", node_4)
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)
builder.add_edge("node_4", END)

# Compile graph
graph = builder.compile()