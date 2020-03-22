from sympy import *
from sympy.abc import x,y,z,a,b,c,f,t,k,n
from process_latex import process_sympy

f = Function('f')
theta = Symbol('theta')

# shorthand definitions
def _Add(a, b):
    return Add(a, b, evaluate=False)
def _Mul(a, b):
    return Mul(a, b, evaluate=False)
def _Pow(a, b):
    return Pow(a, b, evaluate=False)
def _Abs(a):
    return Abs(a, evaluate=False)
def _factorial(a):
    return factorial(a, evaluate=False)
def _log(a, b):
    return log(a, b, evaluate=False)


# These latex strings should parse to the corresponding
# SymPy expression
GOOD_PAIRS = [
    # NoTeX
    ("\\pi", pi),
    ("\\sin(\\pi)", sin(pi, evaluate=False)),
    ('\\exp(i\\pi)', exp(_Mul(I, pi), evaluate=False)),
    ('4 \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}', 4*Matrix([[1, 2], [3, 4]]))
]

# These bad latex strings should raise an exception when parsed
BAD_STRINGS = [
]

total = 0
passed = 0
for s, eq in GOOD_PAIRS:
    total += 1
    try:
        result = process_sympy(s)
        if result != eq:
            print("ERROR: \"%s\" did not parse to %s" % (s, eq))
            print("\tProduced: {}".format(result))
        else:
            passed += 1
    except Exception as e:
        print("ERROR: Exception when parsing \"%s\"" % s)
        print(f"\t{e}")
for s in BAD_STRINGS:
    total += 1
    try:
        process_sympy(s)
        print("ERROR: Exception should have been raised for \"%s\"" % s)
    except Exception:
        passed += 1 

print("%d/%d STRINGS PASSED" % (passed, total))
