from math import log2
from binary_set import BinarySet


class Formula:

    def __init__(self, results):
        size = log2(len(results))
        if size % 1 != 0:
            raise BadResultsCountException
        self.operands_count = int(size)

        self.results = {}
        s = BinarySet(self.operands_count)
        i = 0
        while True:
            self.results[tuple(s)] = results[i]
            i += 1

            if not s.next():
                break

        self.header = s.header()

    # Perfect disjunctive normal form
    def make_pdnf(self):
        rs = []
        for s, f in self.results.items():
            if f == 0:
                continue

            terms = []
            for i in range(len(self.header)):
                term = ""
                if s[i] == 0:
                    term += "!"

                term += self.header[i]
                terms.append(term)

            r = "(" + "*".join(terms) + ")"
            rs.append(r)

        res = " V ".join(rs)
        return res

    # Perfect conjunctive normal form
    def make_pcnf(self):
        rs = []
        for s, f in self.results.items():
            if f == 1:
                continue

            terms = []
            for i in range(len(self.header)):
                term = ""
                if s[i] == 1:
                    term += "!"

                term += self.header[i]
                terms.append(term)

            r = "(" + " V ".join(terms) + ")"
            rs.append(r)

        res = " * ".join(rs)
        return res

    # Polynomial normal form
    def make_pnf(self):
        columns = self._pnf_make_triangle_table_columns()

        terms = self._pnf_get_terms_from_columns(columns)

        res = " ^ ".join(terms)
        return res

    def _pnf_make_triangle_table_columns(self):
        column = list(self.results.values())

        columns = []
        columns.append(column)
        while len(column) != 1:
            new_column = []
            for i in range(1, len(column)):
                new_column.append(column[i - 1] ^ column[i])

            column = new_column
            columns.append(column)

        return columns

    def _pnf_get_terms_from_columns(self, columns):
        t = BinarySet(self.operands_count)
        i = 0
        terms_masks = []
        while True:
            if columns[i][0] == 1:
                mask = str(t).replace(" ", "")
                terms_masks.append(mask)

            i += 1
            if not t.next():
                break

        terms = make_terms_by_masks(terms_masks, t.header())
        terms = list(map(lambda x: str.join("*", list(x)), terms))

        return terms


def make_terms_by_masks(masks, alphabet):
    terms = []
    for mask in masks:
        t = apply_mask(alphabet, mask)

        if t == "":
            t = "1"

        terms.append(t)

    return terms


def apply_mask(string, mask):
    res = ""

    ln = min(len(mask), len(string))
    for i in range(ln):
        if mask[i] == '1':
            res += string[i]

    return res


class BadResultsCountException:
    pass
