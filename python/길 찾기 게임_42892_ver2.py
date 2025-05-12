import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None

def build_tree(nodes, Lx, Rx):
    if not nodes:
        return None

    root = nodes[0]
    root_node = Node(root[0], root[1], root[2])
    left_nodes = []
    right_nodes = []

    for node in nodes[1:]:
        x, y, idx = node
        if Lx <= x < root[0]:
            left_nodes.append(node)
        elif root[0] < x <= Rx:
            right_nodes.append(node)

    root_node.left = build_tree(left_nodes, Lx, root[0] - 1)
    root_node.right = build_tree(right_nodes, root[0] + 1, Rx)

    return root_node

def preorder(node, result):
    if node:
        result.append(node.idx)
        preorder(node.left, result)
        preorder(node.right, result)

def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.idx)

def solution(nodeinfo):
    nodeinfo = [[x, y, idx + 1] for idx, (x, y) in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))  # y 내림차순, x 오름차순

    root = build_tree(nodeinfo, 0, 100000)  # x 범위 넉넉하게 설정

    preorder_result = []
    postorder_result = []

    preorder(root, preorder_result)
    postorder(root, postorder_result)

    return [preorder_result, postorder_result]
