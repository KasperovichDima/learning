from __future__ import annotations
from collections import deque


class Node:

    def __init__(self, name: str, neighbors: dict[Node, float] | None = None) -> None:
        self.name = name
        self.neighbors: dict[Node, float] = neighbors if neighbors else {}

    def add_friend(self, friend: dict[Node, int]) -> None:
        self.neighbors.update(friend)

    def find_friend_by_name(self, name: str) -> Node | None:
        """Поиск в ширину"""
        queue = deque(self.neighbors.keys())
        checked: set[Node] = set()

        while queue:
            candidate = queue.popleft()
            if candidate in checked:
                continue
            checked.add(candidate)
            if candidate.name == name:
                return candidate
            queue.extend(candidate.neighbors.keys())

    def find_shortest_path_to(self, target: Node) -> str:
        """Алгоритм Дейкстры"""
        processed: set[Node] = set()
        processed.add(target)

        def get_lowest_cost_unprocessed_node() -> Node | None:

            lowest = float('inf')
            res = None
            for to_node, from_node_and_cost in costs.items():
                if to_node not in processed and from_node_and_cost[1] < lowest:
                    lowest = from_node_and_cost[1]
                    res = to_node
    
            return res

        def get_path(node: Node) -> str:
            if node.name == self.name:
                return self.name
            return get_path(costs[node][0]) + f' -> {node.name}'


        ToFromCosts = dict[Node, tuple[Node, float]]
        
        costs: ToFromCosts = {k: (self, v) for k, v in self.neighbors.items()}
        costs[target] = (self, float('inf'))
        while (processing_node := get_lowest_cost_unprocessed_node()):
            processing_node_cost = costs[processing_node][1]
            for neighbor_node, neighbor_cost in processing_node.neighbors.items():
                new_cost = processing_node_cost + neighbor_cost
                if neighbor_node not in costs or new_cost < costs[neighbor_node][1]:
                    costs[neighbor_node] = (processing_node, new_cost)
            processed.add(processing_node)

        return f'{get_path(target)}: {str(costs[target][1])}'

    def __repr__(self) -> str:
        return self.name


anuj = Node('anuj')
peggy = Node('peggy')
bob = Node('bob', {anuj: 10, peggy: 15})
alice = Node('alice', {peggy: 5})
tom = Node('tom')
john = Node('john')
clair = Node('clair', {tom: 17, john: 9})
dima = Node('dima', {bob: 3, clair: 21, alice:7})

res = dima.find_friend_by_name('anuj')
print(res)


F = Node('F')
D = Node('D', {F: 10})
E = Node('E', {F: 25, D: 2})
B = Node('B', {D: 15, F: 70})
C = Node('C', {B: 7, D: 30, E: 5})
A = Node('A', {B: 50, C: 10})

print(A.find_shortest_path_to(F))


# E = Node('E')
# B = Node('B')
# D = Node('D', {B: 1})
# C = Node('C', {E: 30, D: 1})
# A = Node('A', {B: 10})
# B.add_friend({C: 20})
# print(A.find_shortest_path_to(E))

