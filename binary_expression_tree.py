from stack import Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

class BinaryExpressionTree:
    def __init__(self):
        self.root = None

    def build_tree(self, postfix_expression):
        tokens = postfix_expression.split()
        stack = Stack()
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                new_node = Node(token)

                if stack.is_empty():
                    raise ValueError(f"Error: Stack is empty when processing operator '{token}'")

                new_node.right = stack.top()
                stack.pop()

                if stack.is_empty():
                    raise ValueError(f"Error: Stack is empty - missing left operand for operator '{token}'")

                new_node.left = stack.top()
                stack.pop()

                stack.push(new_node)

            elif token.replace('.', '', 1).replace('-', '', 1).isdigit():
                new_node = Node(token)
                stack.push(new_node)

            else:
                raise ValueError(f"Error: Unsupported token '{token}'")

        if stack.is_empty():
            raise ValueError("Error: Stack is empty after processing all tokens")

        self.root = stack.top()
        stack.pop()

        if not stack.is_empty():
            raise ValueError("Error: Unused tokens left on the stack")

    def evaluate_tree(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            raise ValueError("Error: Tree is empty")

        if node.is_leaf():
            return float(node.value)

        op = node.value
        x = self.evaluate_tree(node.left)
        y = self.evaluate_tree(node.right)

        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            raise ValueError(f"Error: Unknown operator '{op}'")

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return ""

        if node.is_leaf():
            return node.value

        left_expr = self.inorder_traversal(node.left)
        right_expr = self.inorder_traversal(node.right)

        return f"({left_expr} {node.value} {right_expr})"

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return ""

        if node.is_leaf():
            return node.value

        left_expr = self.postorder_traversal(node.left)
        right_expr = self.postorder_traversal(node.right)

        return f"{left_expr} {right_expr} {node.value}"
