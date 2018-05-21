class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def serialize(node):
    if node:
        return str(node.data) + serialize(node.left) + serialize(node.right)
    else:
        return "-"


def deserialize(data):
    return deserialize_ext(iter(list(data)))


def deserialize_ext(data):
    x = next(data, None)
    if not x or x == '-':
        return None
    else:
        return Node(x, deserialize_ext(data), deserialize_ext(data))


a = Node('1')
a.right = Node('2')
a.right.left = Node('3')
a.right.left.left = Node('4')
a.right.left.right = Node('5')

serialized = serialize(a)
print(serialized)

s = serialize(deserialize(serialized))
print(s)



