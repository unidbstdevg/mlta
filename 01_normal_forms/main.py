from formula import Formula
from user_input import TruthTableFillUi
from utils import count_binary_operators

N = -1
while True:
    ans = input("Number of variables: ")
    try:
        N = int(ans)
        if N < 1 or N > 7:
            print("[error] Number of variables should be between 1 and 7")
            continue

        break
    except ValueError:
        print("[error] Please type number")
        continue

a = TruthTableFillUi(N)
a.ask()
print()

f = Formula(a.results)

pdnf = f.make_pdnf()
print("pdnf:", pdnf)

pcnf = f.make_pcnf()
print("pcnf:", pcnf)

pnf = f.make_pnf()
print("pnf:", pnf)

counts = {
    "pdnf": count_binary_operators(pdnf),
    "pcnf": count_binary_operators(pcnf),
    "pnf": count_binary_operators(pnf)
}
winner = sorted(counts.items(), key=lambda x: x[1])[0]
print("{} have minimal binary operators count: {}".format(winner[0], winner[1]))
