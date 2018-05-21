case class Node(data: Char, var left: Node = null, var right: Node = null)

def serialize(node: Node): String = node match {
  case null => "-"
  case _ => node.data.toString + serialize(node.left) + serialize(node.right)
}

def deserialize(data: String): Node = deserialize2(data.toIterator)

def deserialize2(data: Iterator[Char]): Node = if(data.isEmpty) null else data.next() match {
  case '-' => null
  case a: Char => Node(a, deserialize2(data), deserialize2(data))
}

val root = Node('1')
root.left = Node('2')
root.left.right = Node('3')
root.left.right.left = Node('4')
root.left.right.right=Node('5')

val a1 = serialize(root)
val a2 = serialize(deserialize(a1))

