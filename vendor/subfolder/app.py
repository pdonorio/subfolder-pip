class App:
    def __init__(self, arg: int = 42):
        self.arg = arg

    def test(self):
        print(f"Hello, world ({self.arg})!!")
