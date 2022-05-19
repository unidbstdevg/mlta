from formula import Formula
from user_input import TruthTableFillUi
from duality import get_dual_function
from binary_set import BinarySet

a = TruthTableFillUi()
a.ask()
user_func = a.results

dual_func = get_dual_function(user_func)

formula = Formula(user_func).make_pnf()
dual_formula = Formula(dual_func).make_pnf()
print("f :", formula)
print("f*:", dual_formula)

row_set = BinarySet(a.size)
# print header of truth table
SPAN_BEFORE_F = "  "
print("\n" + " ".join(row_set.header()) + SPAN_BEFORE_F + "f" + "  f*")

i = 0
while True:
    f = user_func[i]
    f_ = dual_func[i]
    print(str(row_set) + SPAN_BEFORE_F + str(f) + "  " + str(f_))

    i += 1
    if not row_set.next():
        break

print()
if user_func == dual_func:
    print("This function IS self-dual")
else:
    print("This function IS NOT self-dual")

input("\nPress 'enter' to exit")
