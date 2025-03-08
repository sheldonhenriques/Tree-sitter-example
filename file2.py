from file1 import Greeter

DEFAULT_NAME = "Guest"  # Global variable

def get_greeting(name=None):
    if not name:
        name = DEFAULT_NAME  # Use the global variable if no name is provided
    greeter = Greeter(name)
    return greeter.greet()

if __name__ == "__main__":
    name = input("Enter your name (or press Enter to use default): ").strip()
    print(get_greeting(name if name else None))
