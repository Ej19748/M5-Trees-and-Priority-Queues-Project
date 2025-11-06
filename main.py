from binary_expression_tree import BinaryExpressionTree

def main():
    postfix_expressions = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]

    print("----- Binary Expression Tree -----")

    for postfix in postfix_expressions:
        try:
            tree = BinaryExpressionTree()
            tree.build_tree(postfix)

            infix = tree.inorder_traversal()
            postfix_display = tree.postorder_traversal()
            result = tree.evaluate_tree()

            print(f"Infix Expression: {infix}")
            print(f"Postfix Expression: {postfix_display}")
            print(f"Evaluated Result: {result}")

        except Exception as e:
            print(f"Error processing '{postfix}': {e}")

if __name__ == "__main__":
    main()
