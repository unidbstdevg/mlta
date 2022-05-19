from os import system
from binary_set import BinarySet

ALPHABET = ('0', '1')
MAX_VARS_COUNT = 7


class TruthTableFillUi:

    def __init__(self):
        self.results = []
        self.buf = " "

    def ask(self):
        size = self.ask_size()
        self.s = BinarySet(size)

        self.buf = " ".join(self.s.header()) + "  f\n"
        while True:
            self.buf += str(self.s) + "  "
            self.redraw()

            self.ask_fill_f()

            if not self.s.next():
                break

    def ask_size(self):
        N = -1
        while True:
            ans = input("Number of variables: ")
            try:
                N = int(ans)
                if N < 1 or N > MAX_VARS_COUNT:
                    print(
                        "[error] Number of variables should be between 1 and "
                        + str(MAX_VARS_COUNT))
                    continue

                break
            except ValueError:
                print("[error] Please type number")
                continue

        return N

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
