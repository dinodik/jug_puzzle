import sys
import treelib

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def propagate(node):
    curr_config = node.value
    next_config = []
    for i in range(N):
        config = curr_config.copy()
        # fill jug
        if curr_config[i] < volumes[i]:
            config[i] = volumes[i]
            next_config.append(config)
        # empty jug
        if curr_config[i] > 0:
            config[i] = 0
            next_config.append(config)
            # transfer jug
            for j in range(N):
                config = curr_config.copy()
                if j != i:
                    space_available = volumes[j] - curr_config[j]
                    if space_available >= curr_config[i]:
                        config[j] += config[i]
                        config[i] = 0
                    else:
                        config[j] = volumes[j]
                        config[i] -= space_available 
                    next_config.append(config)
    for config in next_config:
        if not config in seen_configs:
            node.children.append(Node(config))
            seen_configs.append(config)

def populateTree(tree, node, parent=None):
    value_str = str(node.value)
    if parent == None:
        tree.create_node(value_str, value_str)
    else:
        tree.create_node(value_str, value_str, parent=parent)
    for child in node.children:
        populateTree(tree, child, parent=value_str)

def error():
    print("Invalid input, try in the form\n\tpython jug_puzzle.py a,b,c,...\nwhere a, b, c, ... are volumes. Avoid whitespace. ")
    sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        error()

    arg = sys.argv[1].split(',')

    volumes = []
    try:
        for n in arg:
            volumes.append(int(n))
    except ValueError:
        error()

    N = len(volumes)
    root = Node([0] * N)
    seen_configs = [root.value]

    current_level_nodes = [root]
    next_level_nodes = []

    while len(current_level_nodes) > 0:
        for node in current_level_nodes:
            propagate(node)
            next_level_nodes += node.children

        current_level_nodes = next_level_nodes
        next_level_nodes = []

    print(len(seen_configs))

    tree = treelib.Tree()
    populateTree(tree, root)
    tree.show()
