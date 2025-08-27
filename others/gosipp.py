import random

def gossip(num_nodes=10, rounds=5):
    nodes = [False] * num_nodes
    nodes[0] = True

    for r in range(rounds):
        for i in range(num_nodes):
            if nodes[i]:
                target = random.randint(0, num_nodes - 1)
                nodes[target] = True
        print(f"Round {r + 1}: {nodes.count(True)} / {num_nodes} nodes know")

gossip(20, 6)