from os import system
from binary_set import BinarySet

ALPHABET = ('0', '1')


class TruthTableFillUi:

    def __init__(self, size):
        self.results = []
        self.s = BinarySet(size)
        self.buf = " ".join(self.s.header()) + "  f\n"

    def ask(self):
        while True:
            self.buf += str(self.s) + "  "
            self.redraw()

            self.ask_fill_f()

            if not self.s.next():
                break

    def ask_fill_f(self):
        f = input()
        while f not in ALPHABET:
            self.redraw(error="[warn] f should be one of " + str(ALPHABET))
            f = input()

        self.buf += f + "\n"

        self.results.append(int(f))

    def redraw(self, error=""):
        clear_screen()

        if error != "":
            print(error)

        print(self.buf, end="")


def clear_screen():
    system("cls||clear")
