# comparison_demo.py

def comparison_examples():
    print("🔍 Comparison Operators in Python")
    print("---------------------------------")

    a = 10
    b = 20

    print(f"a = {a}, b = {b}\n")

    # Equality
    print("a == b:", a == b)   # False
    print("a != b:", a != b)   # True

    # Greater / Less than
    print("a > b:", a > b)     # False
    print("a < b:", a < b)     # True

    # Greater / Less than or equal
    print("a >= b:", a >= b)   # False
    print("a <= b:", a <= b)   # True

def user_input_comparison():
    print("\n✨ Let's try with your own numbers!")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print(f"\nComparing {x} and {y}...")
    print("x == y:", x == y)
    print("x != y:", x != y)
    print("x > y:", x > y)
    print("x < y:", x < y)
    print("x >= y:", x >= y)
    print("x <= y:", x <= y)

if __name__ == "__main__":
    comparison_examples()
    user_input_comparison()
