import pycosat
from itertools import product
from collections import defaultdict


# converts given coords and field value to SAT value
# x,y in [0,8], n in [1,9]
def i(x,y,n):
	return (x+y*9)*9 + n

# generates standard sudoku rules
def gen_sudoku_basis(cnf):
	# at least one number in each field
	for y in range(9):
		for x in range(9):
			t = []
			for n in range(1,10):
				t.append(i(x,y,n))
			cnf.append(t)

	# only one number per field
	for y in range(9):
		for x in range(9):
			for n in range(1,10):
				for k in range(1,10):
					if n == k:
						continue
					cnf.append([-i(x,y,n), -i(x,y,k)])

	# each number at least one time in each column
	for y in range(9):
		for n in range(1,10):
			t = []
			for x in range(9):
				t.append(i(x,y,n))
			cnf.append(t)

	# each number at least one time in each row
	for x in range(9):
		for n in range(1,10):
			t = []
			for y in range(9):
				t.append(i(x,y,n))
			cnf.append(t)

	# each number at least one time in each block
	for x in range(3):
		for y in range(3):
			for n in range(1,10):
				t = []
				for dy in range(3):
					for dx in range(3):
						t.append(i(3*x+dx,3*y+dy,n))
				cnf.append(t)

# convert a given solution to a beautiful string matrix
def sol2matr(sol):
	m = [[None]*9 for _ in range(9)]

	for i in sol:
		if i > 0:
			i -= 1
			n = (i % 9) + 1
			x = (i / 9) % 9
			y = i / 81
			if not m[x][y] is None and m[x][y] != n:
				print "collision at %s,%y: %s vs %s" % (x,y,m[x][y], n)
				return "error"
			m[x][y] = n

	r = ""
	for y in range(9):
		if y % 3 == 0:
			r += "+---+---+---+\n"
		for x in range(9):
			if x % 3 == 0:
				r += "|"
			r += " " if m[x][y] is None else str(m[x][y])
		r += "|\n"
	r += "+---+---+---+"
	return r

# print solutions from given cnf
def print_sol(cnf):
	solution = None
	counter = 0
	for sol in pycosat.itersolve(cnf):
		if type(sol) != list:
			print sol
			return

		if solution is None:
			solution = sol
		counter += 1
		if counter > 100:
			break

	print sol2matr(solution)
	if counter > 100:
		print "over 100 more solutions..."
	elif counter > 1:
		print "total solutions: %s" % counter


# generate rules from string matrix
def gen_from_preset(cnf, d):
	lines = d[1:].replace("|", "").replace("+---+---+---+\n", "")[:-1].split("\n")
	for y,l in enumerate(lines):
		for x,c in enumerate(l):
			if c != " ":
				cnf.append([i(x,y,int(c))])

def example_sudoku():
	d = """
+---+---+---+
|  2| 8 | 5 |
| 9 |  6|1 8|
|   |  1| 9 |
+---+---+---+
|7 5|   |38 |
|   |8 9|   |
| 68|   |4 1|
+---+---+---+
| 5 |6  |   |
|4 7|5  | 3 |
| 1 | 9 |2  |
+---+---+---+
"""

	cnf = []

	gen_sudoku_basis(cnf)
	gen_from_preset(cnf, d)

	print_sol(cnf)

def hardest_sudoku():
	d = """
+---+---+---+
|8  |   |   |
|  3|6  |   |
| 7 | 9 |2  |
+---+---+---+
| 5 |  7|   |
|   | 45|7  |
|   |1  | 3 |
+---+---+---+
|  1|   | 68|
|  8|5  | 1 |
| 9 |   |4  |
+---+---+---+
"""

	cnf = []

	gen_sudoku_basis(cnf)
	gen_from_preset(cnf, d)

	print_sol(cnf)

# generate rules from areas
def gen_from_areas(cnf, d, sums):
	sums = sums.split(" ")
	sumdict = {}
	for s in sums:
		sumdict[s[0]] = int(s[1:])

	lines = d[1:].replace("|", "").replace("+---+---+---+\n", "")[:-1].split("\n")
	posdict = defaultdict(list)
	for y,l in enumerate(lines):
		for x,c in enumerate(l):
			posdict[c].append((x,y))

	for k,ar in posdict.items():
		n = len(ar)
		summ = sumdict[k]
		pos = posdict[k]

		for vec in product(range(1,10), repeat=n):
			if sum(vec) != summ:
				cnf.append(map(lambda ((x,y),n): -i(x,y,n), zip(pos, vec)))
				# break

def example_killer_sudoku():
	cnf = []

	gen_sudoku_basis(cnf)

	d = """
+---+---+---+
|aab|ccd|eee|
|aab|ffd|ggh|
|iij|jkl|mmh|
+---+---+---+
|ooj|jkl|mmn|
|pqq|ttu|unn|
|prr|svv|wxy|
+---+---+---+
|pzz|sAB|wxy|
|EEE|AAB|DDy|
|FFA|AAC|CGG|
+---+---+---+
"""

	sums = "a15 b12 c8 d9 e17 f15 g13 h4 i11 j25 k6 l11 m16 n23 o12 p18 q6 r9 "
	sums +="s13 t11 u8 v11 w7 x9 y18 z4 A27 B11 C10 D11 E11 F15 G9"

	gen_from_areas(cnf, d, sums)

	print_sol(cnf)


if __name__ == '__main__':
	print "Sudoku example:"
	example_sudoku()

	print "hardest Sudoku:"
	hardest_sudoku()

	print "killer sudoku example:"
	example_killer_sudoku()
    