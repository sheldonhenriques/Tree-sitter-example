class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

if __name__ == "__main__":
    greeter = Greeter("Alice")
    print(greeter.greet())
