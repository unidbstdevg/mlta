from formula import Formula
from user_input import TruthTableFillUi
from utils import count_binary_operators

a = TruthTableFillUi()
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

input()
