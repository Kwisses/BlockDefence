# BlockDefence - Johnathon Kwisses (Kwistech)
from BlockDefence.game_files.game_loop import App
from BlockDefence.game_files.settings import money, lives


def main():
    app = App()
    app.game_loop()

if __name__ == "__main__":
    main()
