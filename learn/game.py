class Game:
    x="Hello World"
    def __init__(self):
        # class initialization
        print("Game initialized")
        self.a = 1

    def run(self):
        # run other code
        print("Game running")
        print(f"Value of a: {self.a}")
        print(f"Value of x: {self.x}")

    def run_other(self):
        # run other code
        print("Running other code")


game = Game()
game.run()
game.run_other()