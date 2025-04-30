"""
MIT License

Copyright (c) 2025 Oscar Riveros

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def bits(n, p):
    s = []
    while n:
        s = [n % 2 == 0] + s
        n //= 2
    s = (p - len(s)) * [True] + s
    return s


def sat_equation(cnf, n):
    sat = 0
    for j in range(len(cnf)):
        v = 0
        for i in range(n):
            v += int(cnf[j][n - 1 - i] > 0) * 2 ** i
        sat += 2 ** v
    return sat

"""
# Optimized
def sat_equation(cnf, n):
    sat = 0
    for j in range(len(cnf)):
        v = 0
        for i in range(n):
            v |= (cnf[j][n - 1 - i] > 0) << i
        sat |= 1 << v
    return sat
"""


if __name__ == '__main__':
    cnf = [(1, -2, 3), (1, -2, -3), (-1, 2, -3)]

    n = 3

    print(bits(sat_equation(cnf, n), 2 ** n))

    print("""
    (a|~b|c)&(a|~b|~c)&(~a|b|~c)
    a      b      c      value
    False  False  False  True
    False  False  True   True
    False  True   False  False
    False  True   True   False
    True   False  False  True
    True   False  True   False
    True   True   False  True
    True   True   True   True
    """)

    cnf = [(1, 2, 3, -4), (1, 2, -3, -4), (1, -2, 3, -4), (1, -2, -3, -4), (-1, 2, 3, -4), (-1, 2, -3, 4),
           (-1, -2, 3, 4), (-1, -2, -3, 4)]

    n = 4
    m = len(cnf)

    print(bits(sat_equation(cnf, n), 2 ** n))

    print("""
    (a|b|c|~d)&(a|b|~c|~d)&(a|~b|c|~d)&(a|~b|~c|~d)&(~a|b|c|~d)&(~a|b|~c|d)&(~a|~b|c|d)&(~a|~b|~c|d)
    a      b      c      d      value
    False  False  False  False  True
    False  False  False  True   False
    False  False  True   False  True
    False  False  True   True   False
    False  True   False  False  True
    False  True   False  True   False
    False  True   True   False  True
    False  True   True   True   False
    True   False  False  False  True
    True   False  False  True   False
    True   False  True   False  False
    True   False  True   True   True
    True   True   False  False  False
    True   True   False  True   True
    True   True   True   False  False
    True   True   True   True   True
    """)

    cnf = [(1, 2, 3, 4, 5), (1, 2, 3, -4, 5), (1, 2, 3, -4, -5), (1, 2, -3, 4, 5), (1, 2, -3, -4, 5),
           (1, 2, -3, -4, -5), (1, -2, 3, 4, 5), (1, -2, 3, -4, 5), (1, -2, 3, -4, -5), (1, -2, -3, 4, 5),
           (1, -2, -3, -4, 5), (1, -2, -3, -4, -5), (-1, 2, 3, 4, 5), (-1, 2, 3, -4, 5), (-1, 2, 3, -4, -5),
           (-1, 2, -3, 4, -5), (-1, -2, 3, 4, -5), (-1, -2, -3, 4, -5)]

    n = 5
    m = len(cnf)

    print(bits(sat_equation(cnf, n), 2 ** n))

    print("""
    (a|b|c|d|e)&(a|b|c|~d|e)&(a|b|c|~d|~e)&(a|b|~c|d|e)&(a|b|~c|~d|e)&(a|b|~c|~d|~e)&(a|~b|c|d|e)&(a|~b|c|~d|e)&(a|~b|c|~d|~e)&(a|~b|~c|d|e)&(a|~b|~c|~d|e)&(a|~b|~c|~d|~e)&(~a|b|c|d|e)&(~a|b|c|~d|e)&(~a|b|c|~d|~e)&(~a|b|~c|d|~e)&(~a|~b|c|d|~e)&(~a|~b|~c|d|~e)
    a      b      c      d      e      value
    False  False  False  False  False  False
    False  False  False  False  True   True
    False  False  False  True   False  False
    False  False  False  True   True   False
    False  False  True   False  False  False
    False  False  True   False  True   True
    False  False  True   True   False  False
    False  False  True   True   True   False
    False  True   False  False  False  False
    False  True   False  False  True   True
    False  True   False  True   False  False
    False  True   False  True   True   False
    False  True   True   False  False  False
    False  True   True   False  True   True
    False  True   True   True   False  False
    False  True   True   True   True   False
    True   False  False  False  False  False
    True   False  False  False  True   True
    True   False  False  True   False  False
    True   False  False  True   True   False
    True   False  True   False  False  True
    True   False  True   False  True   False
    True   False  True   True   False  True
    True   False  True   True   True   True
    True   True   False  False  False  True
    True   True   False  False  True   False
    True   True   False  True   False  True
    True   True   False  True   True   True
    True   True   True   False  False  True
    True   True   True   False  True   False
    True   True   True   True   False  True
    True   True   True   True   True   True
    """)

    cnf = [(1, 2, 3, 4), (1, 2, 3, -4), (1, 2, -3, 4), (1, 2, -3, -4), (1, -2, 3, 4), (1, -2, 3, -4), (1, -2, -3, 4),
           (1, -2, -3, -4), (-1, 2, 3, 4), (-1, 2, 3, -4), (-1, 2, -3, 4), (-1, 2, -3, -4), (-1, -2, 3, 4),
           (-1, -2, 3, -4), (-1, -2, -3, 4), (-1, -2, -3, -4)]

    n = 4
    m = len(cnf)

    print(bits(sat_equation(cnf, n), 2 ** n))

    print("""
    (a|b|c|d)&(a|b|c|~d)&(a|b|~c|d)&(a|b|~c|~d)&(a|~b|c|d)&(a|~b|c|~d)&(a|~b|~c|d)&(a|~b|~c|~d)&(~a|b|c|d)&(~a|b|c|~d)&(~a|b|~c|d)&(~a|b|~c|~d)&(~a|~b|c|d)&(~a|~b|c|~d)&(~a|~b|~c|d)&(~a|~b|~c|~d)
    a      b      c      d      value
    False  False  False  False  False
    False  False  False  True   False
    False  False  True   False  False
    False  False  True   True   False
    False  True   False  False  False
    False  True   False  True   False
    False  True   True   False  False
    False  True   True   True   False
    True   False  False  False  False
    True   False  False  True   False
    True   False  True   False  False
    True   False  True   True   False
    True   True   False  False  False
    True   True   False  True   False
    True   True   True   False  False
    True   True   True   True   False
    """)

    cnf = [(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, -6), (1, 2, 3, 4, -5, -6), (1, 2, 3, -4, 5, 6), (1, 2, 3, -4, 5, -6),
           (1, 2, 3, -4, -5, 6), (1, 2, 3, -4, -5, -6), (1, 2, -3, 4, 5, 6), (1, 2, -3, 4, 5, -6), (1, 2, -3, 4, -5, 6),
           (1, 2, -3, 4, -5, -6), (1, 2, -3, -4, 5, 6), (1, 2, -3, -4, 5, -6), (1, 2, -3, -4, -5, 6),
           (1, 2, -3, -4, -5, -6), (1, -2, 3, 4, 5, 6), (1, -2, 3, 4, 5, -6), (1, -2, 3, 4, -5, 6),
           (1, -2, 3, 4, -5, -6), (1, -2, 3, -4, 5, 6), (1, -2, 3, -4, 5, -6), (1, -2, 3, -4, -5, 6),
           (1, -2, 3, -4, -5, -6), (1, -2, -3, 4, 5, 6), (1, -2, -3, 4, 5, -6), (1, -2, -3, 4, -5, 6),
           (1, -2, -3, 4, -5, -6), (1, -2, -3, -4, 5, 6), (1, -2, -3, -4, 5, -6), (1, -2, -3, -4, -5, 6),
           (1, -2, -3, -4, -5, -6), (-1, 2, 3, 4, 5, 6), (-1, 2, 3, 4, 5, -6), (-1, 2, 3, 4, -5, 6),
           (-1, 2, 3, 4, -5, -6), (-1, 2, 3, -4, 5, 6), (-1, 2, 3, -4, 5, -6), (-1, 2, 3, -4, -5, 6),
           (-1, 2, 3, -4, -5, -6), (-1, 2, -3, 4, 5, 6), (-1, 2, -3, 4, 5, -6), (-1, 2, -3, 4, -5, 6),
           (-1, 2, -3, 4, -5, -6), (-1, 2, -3, -4, 5, 6), (-1, 2, -3, -4, 5, -6), (-1, 2, -3, -4, -5, 6),
           (-1, 2, -3, -4, -5, -6), (-1, -2, 3, 4, 5, 6), (-1, -2, 3, 4, 5, -6), (-1, -2, 3, 4, -5, 6),
           (-1, -2, 3, 4, -5, -6), (-1, -2, 3, -4, 5, 6), (-1, -2, 3, -4, 5, -6), (-1, -2, 3, -4, -5, 6),
           (-1, -2, 3, -4, -5, -6), (-1, -2, -3, 4, 5, 6), (-1, -2, -3, 4, 5, -6), (-1, -2, -3, 4, -5, 6),
           (-1, -2, -3, 4, -5, -6), (-1, -2, -3, -4, 5, 6), (-1, -2, -3, -4, 5, -6), (-1, -2, -3, -4, -5, 6),
           (-1, -2, -3, -4, -5, -6)]

    n = 6
    m = len(cnf)

    print(bits(sat_equation(cnf, n), 2 ** n))

    print("""
    (a|b|c|d|e|f)&(a|b|c|d|e|~f)&(a|b|c|d|~e|~f)&(a|b|c|~d|e|f)&(a|b|c|~d|e|~f)&(a|b|c|~d|~e|f)&(a|b|c|~d|~e|~f)&(a|b|~c|d|e|f)&(a|b|~c|d|e|~f)&(a|b|~c|d|~e|f)&(a|b|~c|d|~e|~f)&(a|b|~c|~d|e|f)&(a|b|~c|~d|e|~f)&(a|b|~c|~d|~e|f)&(a|b|~c|~d|~e|~f)&(a|~b|c|d|e|f)&(a|~b|c|d|e|~f)&(a|~b|c|d|~e|f)&(a|~b|c|d|~e|~f)&(a|~b|c|~d|e|f)&(a|~b|c|~d|e|~f)&(a|~b|c|~d|~e|f)&(a|~b|c|~d|~e|~f)&(a|~b|~c|d|e|f)&(a|~b|~c|d|e|~f)&(a|~b|~c|d|~e|f)&(a|~b|~c|d|~e|~f)&(a|~b|~c|~d|e|f)&(a|~b|~c|~d|e|~f)&(a|~b|~c|~d|~e|f)&(a|~b|~c|~d|~e|~f)&(~a|b|c|d|e|f)&(~a|b|c|d|e|~f)&(~a|b|c|d|~e|f)&(~a|b|c|d|~e|~f)&(~a|b|c|~d|e|f)&(~a|b|c|~d|e|~f)&(~a|b|c|~d|~e|f)&(~a|b|c|~d|~e|~f)&(~a|b|~c|d|e|f)&(~a|b|~c|d|e|~f)&(~a|b|~c|d|~e|f)&(~a|b|~c|d|~e|~f)&(~a|b|~c|~d|e|f)&(~a|b|~c|~d|e|~f)&(~a|b|~c|~d|~e|f)&(~a|b|~c|~d|~e|~f)&(~a|~b|c|d|e|f)&(~a|~b|c|d|e|~f)&(~a|~b|c|d|~e|f)&(~a|~b|c|d|~e|~f)&(~a|~b|c|~d|e|f)&(~a|~b|c|~d|e|~f)&(~a|~b|c|~d|~e|f)&(~a|~b|c|~d|~e|~f)&(~a|~b|~c|d|e|f)&(~a|~b|~c|d|e|~f)&(~a|~b|~c|d|~e|f)&(~a|~b|~c|d|~e|~f)&(~a|~b|~c|~d|e|f)&(~a|~b|~c|~d|e|~f)&(~a|~b|~c|~d|~e|f)&(~a|~b|~c|~d|~e|~f)
    a      b      c      d      e      f      value
    False  False  False  False  False  False  False
    False  False  False  False  False  True   False
    False  False  False  False  True   False  True
    False  False  False  False  True   True   False
    False  False  False  True   False  False  False
    False  False  False  True   False  True   False
    False  False  False  True   True   False  False
    False  False  False  True   True   True   False
    False  False  True   False  False  False  False
    False  False  True   False  False  True   False
    False  False  True   False  True   False  False
    False  False  True   False  True   True   False
    False  False  True   True   False  False  False
    False  False  True   True   False  True   False
    False  False  True   True   True   False  False
    False  False  True   True   True   True   False
    False  True   False  False  False  False  False
    False  True   False  False  False  True   False
    False  True   False  False  True   False  False
    False  True   False  False  True   True   False
    False  True   False  True   False  False  False
    False  True   False  True   False  True   False
    False  True   False  True   True   False  False
    False  True   False  True   True   True   False
    False  True   True   False  False  False  False
    False  True   True   False  False  True   False
    False  True   True   False  True   False  False
    False  True   True   False  True   True   False
    False  True   True   True   False  False  False
    False  True   True   True   False  True   False
    False  True   True   True   True   False  False
    False  True   True   True   True   True   False
    True   False  False  False  False  False  False
    True   False  False  False  False  True   False
    True   False  False  False  True   False  False
    True   False  False  False  True   True   False
    True   False  False  True   False  False  False
    True   False  False  True   False  True   False
    True   False  False  True   True   False  False
    True   False  False  True   True   True   False
    True   False  True   False  False  False  False
    True   False  True   False  False  True   False
    True   False  True   False  True   False  False
    True   False  True   False  True   True   False
    True   False  True   True   False  False  False
    True   False  True   True   False  True   False
    True   False  True   True   True   False  False
    True   False  True   True   True   True   False
    True   True   False  False  False  False  False
    True   True   False  False  False  True   False
    True   True   False  False  True   False  False
    True   True   False  False  True   True   False
    True   True   False  True   False  False  False
    True   True   False  True   False  True   False
    True   True   False  True   True   False  False
    True   True   False  True   True   True   False
    True   True   True   False  False  False  False
    True   True   True   False  False  True   False
    True   True   True   False  True   False  False
    True   True   True   False  True   True   False
    True   True   True   True   False  False  False
    True   True   True   True   False  True   False
    True   True   True   True   True   False  False
    True   True   True   True   True   True   False
    """)

    cnf = [(1, 2, 3, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, -9), (1, 2, 3, 4, 5, 6, 7, -8, 9),
           (1, 2, 3, 4, 5, 6, 7, -8, -9), (1, 2, 3, 4, 5, 6, -7, 8, 9), (1, 2, 3, 4, 5, 6, -7, 8, -9),
           (1, 2, 3, 4, 5, 6, -7, -8, 9), (1, 2, 3, 4, 5, 6, -7, -8, -9), (1, 2, 3, 4, 5, -6, 7, 8, 9),
           (1, 2, 3, 4, 5, -6, 7, 8, -9), (1, 2, 3, 4, 5, -6, 7, -8, 9), (1, 2, 3, 4, 5, -6, 7, -8, -9),
           (1, 2, 3, 4, 5, -6, -7, 8, 9), (1, 2, 3, 4, 5, -6, -7, 8, -9), (1, 2, 3, 4, 5, -6, -7, -8, 9),
           (1, 2, 3, 4, 5, -6, -7, -8, -9), (1, 2, 3, 4, -5, 6, 7, 8, 9), (1, 2, 3, 4, -5, 6, 7, 8, -9),
           (1, 2, 3, 4, -5, 6, 7, -8, 9), (1, 2, 3, 4, -5, 6, 7, -8, -9), (1, 2, 3, 4, -5, 6, -7, 8, 9),
           (1, 2, 3, 4, -5, 6, -7, 8, -9), (1, 2, 3, 4, -5, 6, -7, -8, 9), (1, 2, 3, 4, -5, 6, -7, -8, -9),
           (1, 2, 3, 4, -5, -6, 7, 8, 9), (1, 2, 3, 4, -5, -6, 7, 8, -9), (1, 2, 3, 4, -5, -6, 7, -8, 9),
           (1, 2, 3, 4, -5, -6, 7, -8, -9), (1, 2, 3, 4, -5, -6, -7, 8, 9), (1, 2, 3, 4, -5, -6, -7, 8, -9),
           (1, 2, 3, 4, -5, -6, -7, -8, 9), (1, 2, 3, 4, -5, -6, -7, -8, -9), (1, 2, 3, -4, 5, 6, 7, 8, 9),
           (1, 2, 3, -4, 5, 6, 7, 8, -9), (1, 2, 3, -4, 5, 6, 7, -8, 9), (1, 2, 3, -4, 5, 6, 7, -8, -9),
           (1, 2, 3, -4, 5, 6, -7, 8, 9), (1, 2, 3, -4, 5, 6, -7, 8, -9), (1, 2, 3, -4, 5, 6, -7, -8, 9),
           (1, 2, 3, -4, 5, 6, -7, -8, -9), (1, 2, 3, -4, 5, -6, 7, 8, 9), (1, 2, 3, -4, 5, -6, 7, 8, -9),
           (1, 2, 3, -4, 5, -6, 7, -8, 9), (1, 2, 3, -4, 5, -6, 7, -8, -9), (1, 2, 3, -4, 5, -6, -7, 8, 9),
           (1, 2, 3, -4, 5, -6, -7, 8, -9), (1, 2, 3, -4, 5, -6, -7, -8, 9), (1, 2, 3, -4, 5, -6, -7, -8, -9),
           (1, 2, 3, -4, -5, 6, 7, 8, 9), (1, 2, 3, -4, -5, 6, 7, 8, -9), (1, 2, 3, -4, -5, 6, 7, -8, 9),
           (1, 2, 3, -4, -5, 6, 7, -8, -9), (1, 2, 3, -4, -5, 6, -7, 8, 9), (1, 2, 3, -4, -5, 6, -7, 8, -9),
           (1, 2, 3, -4, -5, 6, -7, -8, 9), (1, 2, 3, -4, -5, 6, -7, -8, -9), (1, 2, 3, -4, -5, -6, 7, 8, 9),
           (1, 2, 3, -4, -5, -6, 7, 8, -9), (1, 2, 3, -4, -5, -6, 7, -8, 9), (1, 2, 3, -4, -5, -6, 7, -8, -9),
           (1, 2, 3, -4, -5, -6, -7, 8, 9), (1, 2, 3, -4, -5, -6, -7, 8, -9), (1, 2, 3, -4, -5, -6, -7, -8, 9),
           (1, 2, 3, -4, -5, -6, -7, -8, -9), (1, 2, -3, 4, 5, 6, 7, 8, 9), (1, 2, -3, 4, 5, 6, 7, 8, -9),
           (1, 2, -3, 4, 5, 6, 7, -8, 9), (1, 2, -3, 4, 5, 6, 7, -8, -9), (1, 2, -3, 4, 5, 6, -7, 8, 9),
           (1, 2, -3, 4, 5, 6, -7, 8, -9), (1, 2, -3, 4, 5, 6, -7, -8, 9), (1, 2, -3, 4, 5, 6, -7, -8, -9),
           (1, 2, -3, 4, 5, -6, 7, 8, 9), (1, 2, -3, 4, 5, -6, 7, 8, -9), (1, 2, -3, 4, 5, -6, 7, -8, 9),
           (1, 2, -3, 4, 5, -6, 7, -8, -9), (1, 2, -3, 4, 5, -6, -7, 8, 9), (1, 2, -3, 4, 5, -6, -7, 8, -9),
           (1, 2, -3, 4, 5, -6, -7, -8, 9), (1, 2, -3, 4, 5, -6, -7, -8, -9), (1, 2, -3, 4, -5, 6, 7, 8, 9),
           (1, 2, -3, 4, -5, 6, 7, 8, -9), (1, 2, -3, 4, -5, 6, 7, -8, 9), (1, 2, -3, 4, -5, 6, 7, -8, -9),
           (1, 2, -3, 4, -5, 6, -7, 8, 9), (1, 2, -3, 4, -5, 6, -7, 8, -9), (1, 2, -3, 4, -5, 6, -7, -8, 9),
           (1, 2, -3, 4, -5, 6, -7, -8, -9), (1, 2, -3, 4, -5, -6, 7, 8, 9), (1, 2, -3, 4, -5, -6, 7, 8, -9),
           (1, 2, -3, 4, -5, -6, 7, -8, 9), (1, 2, -3, 4, -5, -6, 7, -8, -9), (1, 2, -3, 4, -5, -6, -7, 8, 9),
           (1, 2, -3, 4, -5, -6, -7, 8, -9), (1, 2, -3, 4, -5, -6, -7, -8, 9), (1, 2, -3, 4, -5, -6, -7, -8, -9),
           (1, 2, -3, -4, 5, 6, 7, 8, 9), (1, 2, -3, -4, 5, 6, 7, 8, -9), (1, 2, -3, -4, 5, 6, 7, -8, 9),
           (1, 2, -3, -4, 5, 6, 7, -8, -9), (1, 2, -3, -4, 5, 6, -7, 8, 9), (1, 2, -3, -4, 5, 6, -7, 8, -9),
           (1, 2, -3, -4, 5, 6, -7, -8, 9), (1, 2, -3, -4, 5, 6, -7, -8, -9), (1, 2, -3, -4, 5, -6, 7, 8, 9),
           (1, 2, -3, -4, 5, -6, 7, 8, -9), (1, 2, -3, -4, 5, -6, 7, -8, 9), (1, 2, -3, -4, 5, -6, 7, -8, -9),
           (1, 2, -3, -4, 5, -6, -7, 8, 9), (1, 2, -3, -4, 5, -6, -7, 8, -9), (1, 2, -3, -4, 5, -6, -7, -8, 9),
           (1, 2, -3, -4, 5, -6, -7, -8, -9), (1, 2, -3, -4, -5, 6, 7, 8, 9), (1, 2, -3, -4, -5, 6, 7, 8, -9),
           (1, 2, -3, -4, -5, 6, 7, -8, 9), (1, 2, -3, -4, -5, 6, 7, -8, -9), (1, 2, -3, -4, -5, 6, -7, 8, 9),
           (1, 2, -3, -4, -5, 6, -7, 8, -9), (1, 2, -3, -4, -5, 6, -7, -8, 9), (1, 2, -3, -4, -5, 6, -7, -8, -9),
           (1, 2, -3, -4, -5, -6, 7, 8, 9), (1, 2, -3, -4, -5, -6, 7, 8, -9), (1, 2, -3, -4, -5, -6, 7, -8, 9),
           (1, 2, -3, -4, -5, -6, 7, -8, -9), (1, 2, -3, -4, -5, -6, -7, 8, 9), (1, 2, -3, -4, -5, -6, -7, 8, -9),
           (1, 2, -3, -4, -5, -6, -7, -8, 9), (1, 2, -3, -4, -5, -6, -7, -8, -9), (1, -2, 3, 4, 5, 6, 7, 8, 9),
           (1, -2, 3, 4, 5, 6, 7, 8, -9), (1, -2, 3, 4, 5, 6, 7, -8, 9), (1, -2, 3, 4, 5, 6, 7, -8, -9),
           (1, -2, 3, 4, 5, 6, -7, 8, 9), (1, -2, 3, 4, 5, 6, -7, 8, -9), (1, -2, 3, 4, 5, 6, -7, -8, 9),
           (1, -2, 3, 4, 5, 6, -7, -8, -9), (1, -2, 3, 4, 5, -6, 7, 8, 9), (1, -2, 3, 4, 5, -6, 7, 8, -9),
           (1, -2, 3, 4, 5, -6, 7, -8, 9), (1, -2, 3, 4, 5, -6, 7, -8, -9), (1, -2, 3, 4, 5, -6, -7, 8, 9),
           (1, -2, 3, 4, 5, -6, -7, 8, -9), (1, -2, 3, 4, 5, -6, -7, -8, 9), (1, -2, 3, 4, 5, -6, -7, -8, -9),
           (1, -2, 3, 4, -5, 6, 7, 8, 9), (1, -2, 3, 4, -5, 6, 7, 8, -9), (1, -2, 3, 4, -5, 6, 7, -8, 9),
           (1, -2, 3, 4, -5, 6, 7, -8, -9), (1, -2, 3, 4, -5, 6, -7, 8, 9), (1, -2, 3, 4, -5, 6, -7, 8, -9),
           (1, -2, 3, 4, -5, 6, -7, -8, 9), (1, -2, 3, 4, -5, 6, -7, -8, -9), (1, -2, 3, 4, -5, -6, 7, 8, 9),
           (1, -2, 3, 4, -5, -6, 7, 8, -9), (1, -2, 3, 4, -5, -6, 7, -8, 9), (1, -2, 3, 4, -5, -6, 7, -8, -9),
           (1, -2, 3, 4, -5, -6, -7, 8, 9), (1, -2, 3, 4, -5, -6, -7, 8, -9), (1, -2, 3, 4, -5, -6, -7, -8, 9),
           (1, -2, 3, 4, -5, -6, -7, -8, -9), (1, -2, 3, -4, 5, 6, 7, 8, 9), (1, -2, 3, -4, 5, 6, 7, 8, -9),
           (1, -2, 3, -4, 5, 6, 7, -8, 9), (1, -2, 3, -4, 5, 6, 7, -8, -9), (1, -2, 3, -4, 5, 6, -7, 8, 9),
           (1, -2, 3, -4, 5, 6, -7, 8, -9), (1, -2, 3, -4, 5, 6, -7, -8, 9), (1, -2, 3, -4, 5, 6, -7, -8, -9),
           (1, -2, 3, -4, 5, -6, 7, 8, 9), (1, -2, 3, -4, 5, -6, 7, 8, -9), (1, -2, 3, -4, 5, -6, 7, -8, 9),
           (1, -2, 3, -4, 5, -6, 7, -8, -9), (1, -2, 3, -4, 5, -6, -7, 8, 9), (1, -2, 3, -4, 5, -6, -7, 8, -9),
           (1, -2, 3, -4, 5, -6, -7, -8, 9), (1, -2, 3, -4, 5, -6, -7, -8, -9), (1, -2, 3, -4, -5, 6, 7, 8, 9),
           (1, -2, 3, -4, -5, 6, 7, 8, -9), (1, -2, 3, -4, -5, 6, 7, -8, 9), (1, -2, 3, -4, -5, 6, 7, -8, -9),
           (1, -2, 3, -4, -5, 6, -7, 8, 9), (1, -2, 3, -4, -5, 6, -7, 8, -9), (1, -2, 3, -4, -5, 6, -7, -8, 9),
           (1, -2, 3, -4, -5, 6, -7, -8, -9), (1, -2, 3, -4, -5, -6, 7, 8, 9), (1, -2, 3, -4, -5, -6, 7, 8, -9),
           (1, -2, 3, -4, -5, -6, 7, -8, 9), (1, -2, 3, -4, -5, -6, 7, -8, -9), (1, -2, 3, -4, -5, -6, -7, 8, 9),
           (1, -2, 3, -4, -5, -6, -7, 8, -9), (1, -2, 3, -4, -5, -6, -7, -8, 9), (1, -2, 3, -4, -5, -6, -7, -8, -9),
           (1, -2, -3, 4, 5, 6, 7, 8, 9), (1, -2, -3, 4, 5, 6, 7, 8, -9), (1, -2, -3, 4, 5, 6, 7, -8, 9),
           (1, -2, -3, 4, 5, 6, 7, -8, -9), (1, -2, -3, 4, 5, 6, -7, 8, 9), (1, -2, -3, 4, 5, 6, -7, 8, -9),
           (1, -2, -3, 4, 5, 6, -7, -8, 9), (1, -2, -3, 4, 5, 6, -7, -8, -9), (1, -2, -3, 4, 5, -6, 7, 8, 9),
           (1, -2, -3, 4, 5, -6, 7, 8, -9), (1, -2, -3, 4, 5, -6, 7, -8, 9), (1, -2, -3, 4, 5, -6, 7, -8, -9),
           (1, -2, -3, 4, 5, -6, -7, 8, 9), (1, -2, -3, 4, 5, -6, -7, 8, -9), (1, -2, -3, 4, 5, -6, -7, -8, 9),
           (1, -2, -3, 4, 5, -6, -7, -8, -9), (1, -2, -3, 4, -5, 6, 7, 8, 9), (1, -2, -3, 4, -5, 6, 7, 8, -9),
           (1, -2, -3, 4, -5, 6, 7, -8, 9), (1, -2, -3, 4, -5, 6, 7, -8, -9), (1, -2, -3, 4, -5, 6, -7, 8, 9),
           (1, -2, -3, 4, -5, 6, -7, 8, -9), (1, -2, -3, 4, -5, 6, -7, -8, 9), (1, -2, -3, 4, -5, 6, -7, -8, -9),
           (1, -2, -3, 4, -5, -6, 7, 8, 9), (1, -2, -3, 4, -5, -6, 7, 8, -9), (1, -2, -3, 4, -5, -6, 7, -8, 9),
           (1, -2, -3, 4, -5, -6, 7, -8, -9), (1, -2, -3, 4, -5, -6, -7, 8, 9), (1, -2, -3, 4, -5, -6, -7, 8, -9),
           (1, -2, -3, 4, -5, -6, -7, -8, 9), (1, -2, -3, 4, -5, -6, -7, -8, -9), (1, -2, -3, -4, 5, 6, 7, 8, 9),
           (1, -2, -3, -4, 5, 6, 7, 8, -9), (1, -2, -3, -4, 5, 6, 7, -8, 9), (1, -2, -3, -4, 5, 6, 7, -8, -9),
           (1, -2, -3, -4, 5, 6, -7, 8, 9), (1, -2, -3, -4, 5, 6, -7, 8, -9), (1, -2, -3, -4, 5, 6, -7, -8, 9),
           (1, -2, -3, -4, 5, 6, -7, -8, -9), (1, -2, -3, -4, 5, -6, 7, 8, 9), (1, -2, -3, -4, 5, -6, 7, 8, -9),
           (1, -2, -3, -4, 5, -6, 7, -8, 9), (1, -2, -3, -4, 5, -6, 7, -8, -9), (1, -2, -3, -4, 5, -6, -7, 8, 9),
           (1, -2, -3, -4, 5, -6, -7, 8, -9), (1, -2, -3, -4, 5, -6, -7, -8, 9), (1, -2, -3, -4, 5, -6, -7, -8, -9),
           (1, -2, -3, -4, -5, 6, 7, 8, 9), (1, -2, -3, -4, -5, 6, 7, 8, -9), (1, -2, -3, -4, -5, 6, 7, -8, 9),
           (1, -2, -3, -4, -5, 6, 7, -8, -9), (1, -2, -3, -4, -5, 6, -7, 8, 9), (1, -2, -3, -4, -5, 6, -7, 8, -9),
           (1, -2, -3, -4, -5, 6, -7, -8, 9), (1, -2, -3, -4, -5, 6, -7, -8, -9), (1, -2, -3, -4, -5, -6, 7, 8, 9),
           (1, -2, -3, -4, -5, -6, 7, 8, -9), (1, -2, -3, -4, -5, -6, 7, -8, 9), (1, -2, -3, -4, -5, -6, 7, -8, -9),
           (1, -2, -3, -4, -5, -6, -7, 8, 9), (1, -2, -3, -4, -5, -6, -7, 8, -9), (1, -2, -3, -4, -5, -6, -7, -8, 9),
           (1, -2, -3, -4, -5, -6, -7, -8, -9), (-1, 2, 3, 4, 5, 6, 7, 8, 9), (-1, 2, 3, 4, 5, 6, 7, 8, -9),
           (-1, 2, 3, 4, 5, 6, 7, -8, 9), (-1, 2, 3, 4, 5, 6, 7, -8, -9), (-1, 2, 3, 4, 5, 6, -7, 8, 9),
           (-1, 2, 3, 4, 5, 6, -7, 8, -9), (-1, 2, 3, 4, 5, 6, -7, -8, 9), (-1, 2, 3, 4, 5, 6, -7, -8, -9),
           (-1, 2, 3, 4, 5, -6, 7, 8, -9), (-1, 2, 3, 4, 5, -6, 7, -8, 9), (-1, 2, 3, 4, 5, -6, 7, -8, -9),
           (-1, 2, 3, 4, 5, -6, -7, 8, -9), (-1, 2, 3, 4, 5, -6, -7, -8, 9), (-1, 2, 3, 4, 5, -6, -7, -8, -9),
           (-1, 2, 3, 4, -5, 6, 7, 8, 9), (-1, 2, 3, 4, -5, 6, 7, 8, -9), (-1, 2, 3, 4, -5, 6, 7, -8, 9),
           (-1, 2, 3, 4, -5, 6, 7, -8, -9), (-1, 2, 3, 4, -5, 6, -7, 8, 9), (-1, 2, 3, 4, -5, 6, -7, 8, -9),
           (-1, 2, 3, 4, -5, 6, -7, -8, 9), (-1, 2, 3, 4, -5, 6, -7, -8, -9), (-1, 2, 3, 4, -5, -6, 7, 8, -9),
           (-1, 2, 3, 4, -5, -6, 7, -8, 9), (-1, 2, 3, 4, -5, -6, 7, -8, -9), (-1, 2, 3, 4, -5, -6, -7, 8, -9),
           (-1, 2, 3, 4, -5, -6, -7, -8, 9), (-1, 2, 3, 4, -5, -6, -7, -8, -9), (-1, 2, 3, -4, 5, 6, 7, 8, 9),
           (-1, 2, 3, -4, 5, 6, 7, 8, -9), (-1, 2, 3, -4, 5, 6, 7, -8, 9), (-1, 2, 3, -4, 5, 6, 7, -8, -9),
           (-1, 2, 3, -4, 5, 6, -7, 8, 9), (-1, 2, 3, -4, 5, 6, -7, 8, -9), (-1, 2, 3, -4, 5, 6, -7, -8, 9),
           (-1, 2, 3, -4, 5, 6, -7, -8, -9), (-1, 2, 3, -4, 5, -6, 7, 8, -9), (-1, 2, 3, -4, 5, -6, 7, -8, 9),
           (-1, 2, 3, -4, 5, -6, 7, -8, -9), (-1, 2, 3, -4, 5, -6, -7, 8, -9), (-1, 2, 3, -4, 5, -6, -7, -8, 9),
           (-1, 2, 3, -4, 5, -6, -7, -8, -9), (-1, 2, 3, -4, -5, 6, 7, 8, 9), (-1, 2, 3, -4, -5, 6, 7, 8, -9),
           (-1, 2, 3, -4, -5, 6, 7, -8, 9), (-1, 2, 3, -4, -5, 6, 7, -8, -9), (-1, 2, 3, -4, -5, 6, -7, 8, 9),
           (-1, 2, 3, -4, -5, 6, -7, 8, -9), (-1, 2, 3, -4, -5, 6, -7, -8, 9), (-1, 2, 3, -4, -5, 6, -7, -8, -9),
           (-1, 2, 3, -4, -5, -6, 7, 8, -9), (-1, 2, 3, -4, -5, -6, 7, -8, 9), (-1, 2, 3, -4, -5, -6, 7, -8, -9),
           (-1, 2, 3, -4, -5, -6, -7, 8, -9), (-1, 2, 3, -4, -5, -6, -7, -8, 9), (-1, 2, 3, -4, -5, -6, -7, -8, -9),
           (-1, 2, -3, 4, 5, 6, 7, 8, 9), (-1, 2, -3, 4, 5, 6, 7, 8, -9), (-1, 2, -3, 4, 5, 6, 7, -8, 9),
           (-1, 2, -3, 4, 5, 6, 7, -8, -9), (-1, 2, -3, 4, 5, 6, -7, 8, 9), (-1, 2, -3, 4, 5, 6, -7, 8, -9),
           (-1, 2, -3, 4, 5, 6, -7, -8, 9), (-1, 2, -3, 4, 5, 6, -7, -8, -9), (-1, 2, -3, 4, 5, -6, 7, 8, -9),
           (-1, 2, -3, 4, 5, -6, 7, -8, 9), (-1, 2, -3, 4, 5, -6, 7, -8, -9), (-1, 2, -3, 4, 5, -6, -7, 8, -9),
           (-1, 2, -3, 4, 5, -6, -7, -8, 9), (-1, 2, -3, 4, 5, -6, -7, -8, -9), (-1, 2, -3, 4, -5, 6, 7, 8, 9),
           (-1, 2, -3, 4, -5, 6, 7, 8, -9), (-1, 2, -3, 4, -5, 6, 7, -8, 9), (-1, 2, -3, 4, -5, 6, 7, -8, -9),
           (-1, 2, -3, 4, -5, 6, -7, 8, 9), (-1, 2, -3, 4, -5, 6, -7, 8, -9), (-1, 2, -3, 4, -5, 6, -7, -8, 9),
           (-1, 2, -3, 4, -5, 6, -7, -8, -9), (-1, 2, -3, 4, -5, -6, 7, 8, -9), (-1, 2, -3, 4, -5, -6, 7, -8, 9),
           (-1, 2, -3, 4, -5, -6, 7, -8, -9), (-1, 2, -3, 4, -5, -6, -7, 8, -9), (-1, 2, -3, 4, -5, -6, -7, -8, 9),
           (-1, 2, -3, 4, -5, -6, -7, -8, -9), (-1, 2, -3, -4, 5, 6, 7, 8, 9), (-1, 2, -3, -4, 5, 6, 7, 8, -9),
           (-1, 2, -3, -4, 5, 6, 7, -8, 9), (-1, 2, -3, -4, 5, 6, 7, -8, -9), (-1, 2, -3, -4, 5, 6, -7, 8, 9),
           (-1, 2, -3, -4, 5, 6, -7, 8, -9), (-1, 2, -3, -4, 5, 6, -7, -8, 9), (-1, 2, -3, -4, 5, 6, -7, -8, -9),
           (-1, 2, -3, -4, 5, -6, 7, 8, -9), (-1, 2, -3, -4, 5, -6, 7, -8, 9), (-1, 2, -3, -4, 5, -6, 7, -8, -9),
           (-1, 2, -3, -4, 5, -6, -7, 8, -9), (-1, 2, -3, -4, 5, -6, -7, -8, 9), (-1, 2, -3, -4, 5, -6, -7, -8, -9),
           (-1, 2, -3, -4, -5, 6, 7, 8, 9), (-1, 2, -3, -4, -5, 6, 7, 8, -9), (-1, 2, -3, -4, -5, 6, 7, -8, 9),
           (-1, 2, -3, -4, -5, 6, 7, -8, -9), (-1, 2, -3, -4, -5, 6, -7, 8, 9), (-1, 2, -3, -4, -5, 6, -7, 8, -9),
           (-1, 2, -3, -4, -5, 6, -7, -8, 9), (-1, 2, -3, -4, -5, 6, -7, -8, -9), (-1, 2, -3, -4, -5, -6, 7, 8, -9),
           (-1, 2, -3, -4, -5, -6, 7, -8, 9), (-1, 2, -3, -4, -5, -6, 7, -8, -9), (-1, 2, -3, -4, -5, -6, -7, 8, -9),
           (-1, 2, -3, -4, -5, -6, -7, -8, 9), (-1, 2, -3, -4, -5, -6, -7, -8, -9), (-1, -2, 3, 4, 5, 6, 7, 8, 9),
           (-1, -2, 3, 4, 5, 6, 7, 8, -9), (-1, -2, 3, 4, 5, 6, 7, -8, 9), (-1, -2, 3, 4, 5, 6, 7, -8, -9),
           (-1, -2, 3, 4, 5, 6, -7, 8, 9), (-1, -2, 3, 4, 5, 6, -7, 8, -9), (-1, -2, 3, 4, 5, 6, -7, -8, 9),
           (-1, -2, 3, 4, 5, 6, -7, -8, -9), (-1, -2, 3, 4, 5, -6, 7, 8, -9), (-1, -2, 3, 4, 5, -6, 7, -8, 9),
           (-1, -2, 3, 4, 5, -6, 7, -8, -9), (-1, -2, 3, 4, 5, -6, -7, 8, -9), (-1, -2, 3, 4, 5, -6, -7, -8, 9),
           (-1, -2, 3, 4, 5, -6, -7, -8, -9), (-1, -2, 3, 4, -5, 6, 7, 8, 9), (-1, -2, 3, 4, -5, 6, 7, 8, -9),
           (-1, -2, 3, 4, -5, 6, 7, -8, 9), (-1, -2, 3, 4, -5, 6, 7, -8, -9), (-1, -2, 3, 4, -5, 6, -7, 8, 9),
           (-1, -2, 3, 4, -5, 6, -7, 8, -9), (-1, -2, 3, 4, -5, 6, -7, -8, 9), (-1, -2, 3, 4, -5, 6, -7, -8, -9),
           (-1, -2, 3, 4, -5, -6, 7, 8, -9), (-1, -2, 3, 4, -5, -6, 7, -8, 9), (-1, -2, 3, 4, -5, -6, 7, -8, -9),
           (-1, -2, 3, 4, -5, -6, -7, 8, -9), (-1, -2, 3, 4, -5, -6, -7, -8, 9), (-1, -2, 3, 4, -5, -6, -7, -8, -9),
           (-1, -2, 3, -4, 5, 6, 7, 8, 9), (-1, -2, 3, -4, 5, 6, 7, 8, -9), (-1, -2, 3, -4, 5, 6, 7, -8, 9),
           (-1, -2, 3, -4, 5, 6, 7, -8, -9), (-1, -2, 3, -4, 5, 6, -7, 8, 9), (-1, -2, 3, -4, 5, 6, -7, 8, -9),
           (-1, -2, 3, -4, 5, 6, -7, -8, 9), (-1, -2, 3, -4, 5, 6, -7, -8, -9), (-1, -2, 3, -4, 5, -6, 7, 8, -9),
           (-1, -2, 3, -4, 5, -6, 7, -8, 9), (-1, -2, 3, -4, 5, -6, 7, -8, -9), (-1, -2, 3, -4, 5, -6, -7, 8, -9),
           (-1, -2, 3, -4, 5, -6, -7, -8, 9), (-1, -2, 3, -4, 5, -6, -7, -8, -9), (-1, -2, 3, -4, -5, 6, 7, 8, 9),
           (-1, -2, 3, -4, -5, 6, 7, 8, -9), (-1, -2, 3, -4, -5, 6, 7, -8, 9), (-1, -2, 3, -4, -5, 6, 7, -8, -9),
           (-1, -2, 3, -4, -5, 6, -7, 8, 9), (-1, -2, 3, -4, -5, 6, -7, 8, -9), (-1, -2, 3, -4, -5, 6, -7, -8, 9),
           (-1, -2, 3, -4, -5, 6, -7, -8, -9), (-1, -2, 3, -4, -5, -6, 7, 8, -9), (-1, -2, 3, -4, -5, -6, 7, -8, 9),
           (-1, -2, 3, -4, -5, -6, 7, -8, -9), (-1, -2, 3, -4, -5, -6, -7, 8, -9), (-1, -2, 3, -4, -5, -6, -7, -8, 9),
           (-1, -2, 3, -4, -5, -6, -7, -8, -9), (-1, -2, -3, 4, 5, 6, 7, 8, 9), (-1, -2, -3, 4, 5, 6, 7, 8, -9),
           (-1, -2, -3, 4, 5, 6, 7, -8, 9), (-1, -2, -3, 4, 5, 6, 7, -8, -9), (-1, -2, -3, 4, 5, 6, -7, 8, 9),
           (-1, -2, -3, 4, 5, 6, -7, 8, -9), (-1, -2, -3, 4, 5, 6, -7, -8, 9), (-1, -2, -3, 4, 5, 6, -7, -8, -9),
           (-1, -2, -3, 4, 5, -6, 7, 8, -9), (-1, -2, -3, 4, 5, -6, 7, -8, 9), (-1, -2, -3, 4, 5, -6, 7, -8, -9),
           (-1, -2, -3, 4, 5, -6, -7, 8, -9), (-1, -2, -3, 4, 5, -6, -7, -8, 9), (-1, -2, -3, 4, 5, -6, -7, -8, -9),
           (-1, -2, -3, 4, -5, 6, 7, 8, 9), (-1, -2, -3, 4, -5, 6, 7, 8, -9), (-1, -2, -3, 4, -5, 6, 7, -8, 9),
           (-1, -2, -3, 4, -5, 6, 7, -8, -9), (-1, -2, -3, 4, -5, 6, -7, 8, 9), (-1, -2, -3, 4, -5, 6, -7, 8, -9),
           (-1, -2, -3, 4, -5, 6, -7, -8, 9), (-1, -2, -3, 4, -5, 6, -7, -8, -9), (-1, -2, -3, 4, -5, -6, 7, 8, -9),
           (-1, -2, -3, 4, -5, -6, 7, -8, 9), (-1, -2, -3, 4, -5, -6, 7, -8, -9), (-1, -2, -3, 4, -5, -6, -7, 8, -9),
           (-1, -2, -3, 4, -5, -6, -7, -8, 9), (-1, -2, -3, 4, -5, -6, -7, -8, -9), (-1, -2, -3, -4, 5, 6, 7, 8, 9),
           (-1, -2, -3, -4, 5, 6, 7, 8, -9), (-1, -2, -3, -4, 5, 6, 7, -8, 9), (-1, -2, -3, -4, 5, 6, 7, -8, -9),
           (-1, -2, -3, -4, 5, 6, -7, 8, 9), (-1, -2, -3, -4, 5, 6, -7, 8, -9), (-1, -2, -3, -4, 5, 6, -7, -8, 9),
           (-1, -2, -3, -4, 5, 6, -7, -8, -9), (-1, -2, -3, -4, 5, -6, 7, 8, -9), (-1, -2, -3, -4, 5, -6, 7, -8, 9),
           (-1, -2, -3, -4, 5, -6, 7, -8, -9), (-1, -2, -3, -4, 5, -6, -7, 8, -9), (-1, -2, -3, -4, 5, -6, -7, -8, 9),
           (-1, -2, -3, -4, 5, -6, -7, -8, -9), (-1, -2, -3, -4, -5, 6, 7, 8, 9), (-1, -2, -3, -4, -5, 6, 7, 8, -9),
           (-1, -2, -3, -4, -5, 6, 7, -8, 9), (-1, -2, -3, -4, -5, 6, 7, -8, -9), (-1, -2, -3, -4, -5, 6, -7, 8, 9),
           (-1, -2, -3, -4, -5, 6, -7, 8, -9), (-1, -2, -3, -4, -5, 6, -7, -8, 9), (-1, -2, -3, -4, -5, 6, -7, -8, -9),
           (-1, -2, -3, -4, -5, -6, 7, 8, -9), (-1, -2, -3, -4, -5, -6, 7, -8, 9), (-1, -2, -3, -4, -5, -6, 7, -8, -9),
           (-1, -2, -3, -4, -5, -6, -7, 8, -9), (-1, -2, -3, -4, -5, -6, -7, -8, 9),
           (-1, -2, -3, -4, -5, -6, -7, -8, -9)]

    n = 9
    m = len(cnf)

    print(bits(sat_equation(cnf, n), 2 ** n))

    print("""
    (a|b|c|d|e|f|g|h|i)&(a|b|c|d|e|f|g|h|~i)&(a|b|c|d|e|f|g|~h|i)&(a|b|c|d|e|f|g|~h|~i)&(a|b|c|d|e|f|~g|h|i)&(a|b|c|d|e|f|~g|h|~i)&(a|b|c|d|e|f|~g|~h|i)&(a|b|c|d|e|f|~g|~h|~i)&(a|b|c|d|e|~f|g|h|i)&(a|b|c|d|e|~f|g|h|~i)&(a|b|c|d|e|~f|g|~h|i)&(a|b|c|d|e|~f|g|~h|~i)&(a|b|c|d|e|~f|~g|h|i)&(a|b|c|d|e|~f|~g|h|~i)&(a|b|c|d|e|~f|~g|~h|i)&(a|b|c|d|e|~f|~g|~h|~i)&(a|b|c|d|~e|f|g|h|i)&(a|b|c|d|~e|f|g|h|~i)&(a|b|c|d|~e|f|g|~h|i)&(a|b|c|d|~e|f|g|~h|~i)&(a|b|c|d|~e|f|~g|h|i)&(a|b|c|d|~e|f|~g|h|~i)&(a|b|c|d|~e|f|~g|~h|i)&(a|b|c|d|~e|f|~g|~h|~i)&(a|b|c|d|~e|~f|g|h|i)&(a|b|c|d|~e|~f|g|h|~i)&(a|b|c|d|~e|~f|g|~h|i)&(a|b|c|d|~e|~f|g|~h|~i)&(a|b|c|d|~e|~f|~g|h|i)&(a|b|c|d|~e|~f|~g|h|~i)&(a|b|c|d|~e|~f|~g|~h|i)&(a|b|c|d|~e|~f|~g|~h|~i)&(a|b|c|~d|e|f|g|h|i)&(a|b|c|~d|e|f|g|h|~i)&(a|b|c|~d|e|f|g|~h|i)&(a|b|c|~d|e|f|g|~h|~i)&(a|b|c|~d|e|f|~g|h|i)&(a|b|c|~d|e|f|~g|h|~i)&(a|b|c|~d|e|f|~g|~h|i)&(a|b|c|~d|e|f|~g|~h|~i)&(a|b|c|~d|e|~f|g|h|i)&(a|b|c|~d|e|~f|g|h|~i)&(a|b|c|~d|e|~f|g|~h|i)&(a|b|c|~d|e|~f|g|~h|~i)&(a|b|c|~d|e|~f|~g|h|i)&(a|b|c|~d|e|~f|~g|h|~i)&(a|b|c|~d|e|~f|~g|~h|i)&(a|b|c|~d|e|~f|~g|~h|~i)&(a|b|c|~d|~e|f|g|h|i)&(a|b|c|~d|~e|f|g|h|~i)&(a|b|c|~d|~e|f|g|~h|i)&(a|b|c|~d|~e|f|g|~h|~i)&(a|b|c|~d|~e|f|~g|h|i)&(a|b|c|~d|~e|f|~g|h|~i)&(a|b|c|~d|~e|f|~g|~h|i)&(a|b|c|~d|~e|f|~g|~h|~i)&(a|b|c|~d|~e|~f|g|h|i)&(a|b|c|~d|~e|~f|g|h|~i)&(a|b|c|~d|~e|~f|g|~h|i)&(a|b|c|~d|~e|~f|g|~h|~i)&(a|b|c|~d|~e|~f|~g|h|i)&(a|b|c|~d|~e|~f|~g|h|~i)&(a|b|c|~d|~e|~f|~g|~h|i)&(a|b|c|~d|~e|~f|~g|~h|~i)&(a|b|~c|d|e|f|g|h|i)&(a|b|~c|d|e|f|g|h|~i)&(a|b|~c|d|e|f|g|~h|i)&(a|b|~c|d|e|f|g|~h|~i)&(a|b|~c|d|e|f|~g|h|i)&(a|b|~c|d|e|f|~g|h|~i)&(a|b|~c|d|e|f|~g|~h|i)&(a|b|~c|d|e|f|~g|~h|~i)&(a|b|~c|d|e|~f|g|h|i)&(a|b|~c|d|e|~f|g|h|~i)&(a|b|~c|d|e|~f|g|~h|i)&(a|b|~c|d|e|~f|g|~h|~i)&(a|b|~c|d|e|~f|~g|h|i)&(a|b|~c|d|e|~f|~g|h|~i)&(a|b|~c|d|e|~f|~g|~h|i)&(a|b|~c|d|e|~f|~g|~h|~i)&(a|b|~c|d|~e|f|g|h|i)&(a|b|~c|d|~e|f|g|h|~i)&(a|b|~c|d|~e|f|g|~h|i)&(a|b|~c|d|~e|f|g|~h|~i)&(a|b|~c|d|~e|f|~g|h|i)&(a|b|~c|d|~e|f|~g|h|~i)&(a|b|~c|d|~e|f|~g|~h|i)&(a|b|~c|d|~e|f|~g|~h|~i)&(a|b|~c|d|~e|~f|g|h|i)&(a|b|~c|d|~e|~f|g|h|~i)&(a|b|~c|d|~e|~f|g|~h|i)&(a|b|~c|d|~e|~f|g|~h|~i)&(a|b|~c|d|~e|~f|~g|h|i)&(a|b|~c|d|~e|~f|~g|h|~i)&(a|b|~c|d|~e|~f|~g|~h|i)&(a|b|~c|d|~e|~f|~g|~h|~i)&(a|b|~c|~d|e|f|g|h|i)&(a|b|~c|~d|e|f|g|h|~i)&(a|b|~c|~d|e|f|g|~h|i)&(a|b|~c|~d|e|f|g|~h|~i)&(a|b|~c|~d|e|f|~g|h|i)&(a|b|~c|~d|e|f|~g|h|~i)&(a|b|~c|~d|e|f|~g|~h|i)&(a|b|~c|~d|e|f|~g|~h|~i)&(a|b|~c|~d|e|~f|g|h|i)&(a|b|~c|~d|e|~f|g|h|~i)&(a|b|~c|~d|e|~f|g|~h|i)&(a|b|~c|~d|e|~f|g|~h|~i)&(a|b|~c|~d|e|~f|~g|h|i)&(a|b|~c|~d|e|~f|~g|h|~i)&(a|b|~c|~d|e|~f|~g|~h|i)&(a|b|~c|~d|e|~f|~g|~h|~i)&(a|b|~c|~d|~e|f|g|h|i)&(a|b|~c|~d|~e|f|g|h|~i)&(a|b|~c|~d|~e|f|g|~h|i)&(a|b|~c|~d|~e|f|g|~h|~i)&(a|b|~c|~d|~e|f|~g|h|i)&(a|b|~c|~d|~e|f|~g|h|~i)&(a|b|~c|~d|~e|f|~g|~h|i)&(a|b|~c|~d|~e|f|~g|~h|~i)&(a|b|~c|~d|~e|~f|g|h|i)&(a|b|~c|~d|~e|~f|g|h|~i)&(a|b|~c|~d|~e|~f|g|~h|i)&(a|b|~c|~d|~e|~f|g|~h|~i)&(a|b|~c|~d|~e|~f|~g|h|i)&(a|b|~c|~d|~e|~f|~g|h|~i)&(a|b|~c|~d|~e|~f|~g|~h|i)&(a|b|~c|~d|~e|~f|~g|~h|~i)&(a|~b|c|d|e|f|g|h|i)&(a|~b|c|d|e|f|g|h|~i)&(a|~b|c|d|e|f|g|~h|i)&(a|~b|c|d|e|f|g|~h|~i)&(a|~b|c|d|e|f|~g|h|i)&(a|~b|c|d|e|f|~g|h|~i)&(a|~b|c|d|e|f|~g|~h|i)&(a|~b|c|d|e|f|~g|~h|~i)&(a|~b|c|d|e|~f|g|h|i)&(a|~b|c|d|e|~f|g|h|~i)&(a|~b|c|d|e|~f|g|~h|i)&(a|~b|c|d|e|~f|g|~h|~i)&(a|~b|c|d|e|~f|~g|h|i)&(a|~b|c|d|e|~f|~g|h|~i)&(a|~b|c|d|e|~f|~g|~h|i)&(a|~b|c|d|e|~f|~g|~h|~i)&(a|~b|c|d|~e|f|g|h|i)&(a|~b|c|d|~e|f|g|h|~i)&(a|~b|c|d|~e|f|g|~h|i)&(a|~b|c|d|~e|f|g|~h|~i)&(a|~b|c|d|~e|f|~g|h|i)&(a|~b|c|d|~e|f|~g|h|~i)&(a|~b|c|d|~e|f|~g|~h|i)&(a|~b|c|d|~e|f|~g|~h|~i)&(a|~b|c|d|~e|~f|g|h|i)&(a|~b|c|d|~e|~f|g|h|~i)&(a|~b|c|d|~e|~f|g|~h|i)&(a|~b|c|d|~e|~f|g|~h|~i)&(a|~b|c|d|~e|~f|~g|h|i)&(a|~b|c|d|~e|~f|~g|h|~i)&(a|~b|c|d|~e|~f|~g|~h|i)&(a|~b|c|d|~e|~f|~g|~h|~i)&(a|~b|c|~d|e|f|g|h|i)&(a|~b|c|~d|e|f|g|h|~i)&(a|~b|c|~d|e|f|g|~h|i)&(a|~b|c|~d|e|f|g|~h|~i)&(a|~b|c|~d|e|f|~g|h|i)&(a|~b|c|~d|e|f|~g|h|~i)&(a|~b|c|~d|e|f|~g|~h|i)&(a|~b|c|~d|e|f|~g|~h|~i)&(a|~b|c|~d|e|~f|g|h|i)&(a|~b|c|~d|e|~f|g|h|~i)&(a|~b|c|~d|e|~f|g|~h|i)&(a|~b|c|~d|e|~f|g|~h|~i)&(a|~b|c|~d|e|~f|~g|h|i)&(a|~b|c|~d|e|~f|~g|h|~i)&(a|~b|c|~d|e|~f|~g|~h|i)&(a|~b|c|~d|e|~f|~g|~h|~i)&(a|~b|c|~d|~e|f|g|h|i)&(a|~b|c|~d|~e|f|g|h|~i)&(a|~b|c|~d|~e|f|g|~h|i)&(a|~b|c|~d|~e|f|g|~h|~i)&(a|~b|c|~d|~e|f|~g|h|i)&(a|~b|c|~d|~e|f|~g|h|~i)&(a|~b|c|~d|~e|f|~g|~h|i)&(a|~b|c|~d|~e|f|~g|~h|~i)&(a|~b|c|~d|~e|~f|g|h|i)&(a|~b|c|~d|~e|~f|g|h|~i)&(a|~b|c|~d|~e|~f|g|~h|i)&(a|~b|c|~d|~e|~f|g|~h|~i)&(a|~b|c|~d|~e|~f|~g|h|i)&(a|~b|c|~d|~e|~f|~g|h|~i)&(a|~b|c|~d|~e|~f|~g|~h|i)&(a|~b|c|~d|~e|~f|~g|~h|~i)&(a|~b|~c|d|e|f|g|h|i)&(a|~b|~c|d|e|f|g|h|~i)&(a|~b|~c|d|e|f|g|~h|i)&(a|~b|~c|d|e|f|g|~h|~i)&(a|~b|~c|d|e|f|~g|h|i)&(a|~b|~c|d|e|f|~g|h|~i)&(a|~b|~c|d|e|f|~g|~h|i)&(a|~b|~c|d|e|f|~g|~h|~i)&(a|~b|~c|d|e|~f|g|h|i)&(a|~b|~c|d|e|~f|g|h|~i)&(a|~b|~c|d|e|~f|g|~h|i)&(a|~b|~c|d|e|~f|g|~h|~i)&(a|~b|~c|d|e|~f|~g|h|i)&(a|~b|~c|d|e|~f|~g|h|~i)&(a|~b|~c|d|e|~f|~g|~h|i)&(a|~b|~c|d|e|~f|~g|~h|~i)&(a|~b|~c|d|~e|f|g|h|i)&(a|~b|~c|d|~e|f|g|h|~i)&(a|~b|~c|d|~e|f|g|~h|i)&(a|~b|~c|d|~e|f|g|~h|~i)&(a|~b|~c|d|~e|f|~g|h|i)&(a|~b|~c|d|~e|f|~g|h|~i)&(a|~b|~c|d|~e|f|~g|~h|i)&(a|~b|~c|d|~e|f|~g|~h|~i)&(a|~b|~c|d|~e|~f|g|h|i)&(a|~b|~c|d|~e|~f|g|h|~i)&(a|~b|~c|d|~e|~f|g|~h|i)&(a|~b|~c|d|~e|~f|g|~h|~i)&(a|~b|~c|d|~e|~f|~g|h|i)&(a|~b|~c|d|~e|~f|~g|h|~i)&(a|~b|~c|d|~e|~f|~g|~h|i)&(a|~b|~c|d|~e|~f|~g|~h|~i)&(a|~b|~c|~d|e|f|g|h|i)&(a|~b|~c|~d|e|f|g|h|~i)&(a|~b|~c|~d|e|f|g|~h|i)&(a|~b|~c|~d|e|f|g|~h|~i)&(a|~b|~c|~d|e|f|~g|h|i)&(a|~b|~c|~d|e|f|~g|h|~i)&(a|~b|~c|~d|e|f|~g|~h|i)&(a|~b|~c|~d|e|f|~g|~h|~i)&(a|~b|~c|~d|e|~f|g|h|i)&(a|~b|~c|~d|e|~f|g|h|~i)&(a|~b|~c|~d|e|~f|g|~h|i)&(a|~b|~c|~d|e|~f|g|~h|~i)&(a|~b|~c|~d|e|~f|~g|h|i)&(a|~b|~c|~d|e|~f|~g|h|~i)&(a|~b|~c|~d|e|~f|~g|~h|i)&(a|~b|~c|~d|e|~f|~g|~h|~i)&(a|~b|~c|~d|~e|f|g|h|i)&(a|~b|~c|~d|~e|f|g|h|~i)&(a|~b|~c|~d|~e|f|g|~h|i)&(a|~b|~c|~d|~e|f|g|~h|~i)&(a|~b|~c|~d|~e|f|~g|h|i)&(a|~b|~c|~d|~e|f|~g|h|~i)&(a|~b|~c|~d|~e|f|~g|~h|i)&(a|~b|~c|~d|~e|f|~g|~h|~i)&(a|~b|~c|~d|~e|~f|g|h|i)&(a|~b|~c|~d|~e|~f|g|h|~i)&(a|~b|~c|~d|~e|~f|g|~h|i)&(a|~b|~c|~d|~e|~f|g|~h|~i)&(a|~b|~c|~d|~e|~f|~g|h|i)&(a|~b|~c|~d|~e|~f|~g|h|~i)&(a|~b|~c|~d|~e|~f|~g|~h|i)&(a|~b|~c|~d|~e|~f|~g|~h|~i)&(~a|b|c|d|e|f|g|h|i)&(~a|b|c|d|e|f|g|h|~i)&(~a|b|c|d|e|f|g|~h|i)&(~a|b|c|d|e|f|g|~h|~i)&(~a|b|c|d|e|f|~g|h|i)&(~a|b|c|d|e|f|~g|h|~i)&(~a|b|c|d|e|f|~g|~h|i)&(~a|b|c|d|e|f|~g|~h|~i)&(~a|b|c|d|e|~f|g|h|~i)&(~a|b|c|d|e|~f|g|~h|i)&(~a|b|c|d|e|~f|g|~h|~i)&(~a|b|c|d|e|~f|~g|h|~i)&(~a|b|c|d|e|~f|~g|~h|i)&(~a|b|c|d|e|~f|~g|~h|~i)&(~a|b|c|d|~e|f|g|h|i)&(~a|b|c|d|~e|f|g|h|~i)&(~a|b|c|d|~e|f|g|~h|i)&(~a|b|c|d|~e|f|g|~h|~i)&(~a|b|c|d|~e|f|~g|h|i)&(~a|b|c|d|~e|f|~g|h|~i)&(~a|b|c|d|~e|f|~g|~h|i)&(~a|b|c|d|~e|f|~g|~h|~i)&(~a|b|c|d|~e|~f|g|h|~i)&(~a|b|c|d|~e|~f|g|~h|i)&(~a|b|c|d|~e|~f|g|~h|~i)&(~a|b|c|d|~e|~f|~g|h|~i)&(~a|b|c|d|~e|~f|~g|~h|i)&(~a|b|c|d|~e|~f|~g|~h|~i)&(~a|b|c|~d|e|f|g|h|i)&(~a|b|c|~d|e|f|g|h|~i)&(~a|b|c|~d|e|f|g|~h|i)&(~a|b|c|~d|e|f|g|~h|~i)&(~a|b|c|~d|e|f|~g|h|i)&(~a|b|c|~d|e|f|~g|h|~i)&(~a|b|c|~d|e|f|~g|~h|i)&(~a|b|c|~d|e|f|~g|~h|~i)&(~a|b|c|~d|e|~f|g|h|~i)&(~a|b|c|~d|e|~f|g|~h|i)&(~a|b|c|~d|e|~f|g|~h|~i)&(~a|b|c|~d|e|~f|~g|h|~i)&(~a|b|c|~d|e|~f|~g|~h|i)&(~a|b|c|~d|e|~f|~g|~h|~i)&(~a|b|c|~d|~e|f|g|h|i)&(~a|b|c|~d|~e|f|g|h|~i)&(~a|b|c|~d|~e|f|g|~h|i)&(~a|b|c|~d|~e|f|g|~h|~i)&(~a|b|c|~d|~e|f|~g|h|i)&(~a|b|c|~d|~e|f|~g|h|~i)&(~a|b|c|~d|~e|f|~g|~h|i)&(~a|b|c|~d|~e|f|~g|~h|~i)&(~a|b|c|~d|~e|~f|g|h|~i)&(~a|b|c|~d|~e|~f|g|~h|i)&(~a|b|c|~d|~e|~f|g|~h|~i)&(~a|b|c|~d|~e|~f|~g|h|~i)&(~a|b|c|~d|~e|~f|~g|~h|i)&(~a|b|c|~d|~e|~f|~g|~h|~i)&(~a|b|~c|d|e|f|g|h|i)&(~a|b|~c|d|e|f|g|h|~i)&(~a|b|~c|d|e|f|g|~h|i)&(~a|b|~c|d|e|f|g|~h|~i)&(~a|b|~c|d|e|f|~g|h|i)&(~a|b|~c|d|e|f|~g|h|~i)&(~a|b|~c|d|e|f|~g|~h|i)&(~a|b|~c|d|e|f|~g|~h|~i)&(~a|b|~c|d|e|~f|g|h|~i)&(~a|b|~c|d|e|~f|g|~h|i)&(~a|b|~c|d|e|~f|g|~h|~i)&(~a|b|~c|d|e|~f|~g|h|~i)&(~a|b|~c|d|e|~f|~g|~h|i)&(~a|b|~c|d|e|~f|~g|~h|~i)&(~a|b|~c|d|~e|f|g|h|i)&(~a|b|~c|d|~e|f|g|h|~i)&(~a|b|~c|d|~e|f|g|~h|i)&(~a|b|~c|d|~e|f|g|~h|~i)&(~a|b|~c|d|~e|f|~g|h|i)&(~a|b|~c|d|~e|f|~g|h|~i)&(~a|b|~c|d|~e|f|~g|~h|i)&(~a|b|~c|d|~e|f|~g|~h|~i)&(~a|b|~c|d|~e|~f|g|h|~i)&(~a|b|~c|d|~e|~f|g|~h|i)&(~a|b|~c|d|~e|~f|g|~h|~i)&(~a|b|~c|d|~e|~f|~g|h|~i)&(~a|b|~c|d|~e|~f|~g|~h|i)&(~a|b|~c|d|~e|~f|~g|~h|~i)&(~a|b|~c|~d|e|f|g|h|i)&(~a|b|~c|~d|e|f|g|h|~i)&(~a|b|~c|~d|e|f|g|~h|i)&(~a|b|~c|~d|e|f|g|~h|~i)&(~a|b|~c|~d|e|f|~g|h|i)&(~a|b|~c|~d|e|f|~g|h|~i)&(~a|b|~c|~d|e|f|~g|~h|i)&(~a|b|~c|~d|e|f|~g|~h|~i)&(~a|b|~c|~d|e|~f|g|h|~i)&(~a|b|~c|~d|e|~f|g|~h|i)&(~a|b|~c|~d|e|~f|g|~h|~i)&(~a|b|~c|~d|e|~f|~g|h|~i)&(~a|b|~c|~d|e|~f|~g|~h|i)&(~a|b|~c|~d|e|~f|~g|~h|~i)&(~a|b|~c|~d|~e|f|g|h|i)&(~a|b|~c|~d|~e|f|g|h|~i)&(~a|b|~c|~d|~e|f|g|~h|i)&(~a|b|~c|~d|~e|f|g|~h|~i)&(~a|b|~c|~d|~e|f|~g|h|i)&(~a|b|~c|~d|~e|f|~g|h|~i)&(~a|b|~c|~d|~e|f|~g|~h|i)&(~a|b|~c|~d|~e|f|~g|~h|~i)&(~a|b|~c|~d|~e|~f|g|h|~i)&(~a|b|~c|~d|~e|~f|g|~h|i)&(~a|b|~c|~d|~e|~f|g|~h|~i)&(~a|b|~c|~d|~e|~f|~g|h|~i)&(~a|b|~c|~d|~e|~f|~g|~h|i)&(~a|b|~c|~d|~e|~f|~g|~h|~i)&(~a|~b|c|d|e|f|g|h|i)&(~a|~b|c|d|e|f|g|h|~i)&(~a|~b|c|d|e|f|g|~h|i)&(~a|~b|c|d|e|f|g|~h|~i)&(~a|~b|c|d|e|f|~g|h|i)&(~a|~b|c|d|e|f|~g|h|~i)&(~a|~b|c|d|e|f|~g|~h|i)&(~a|~b|c|d|e|f|~g|~h|~i)&(~a|~b|c|d|e|~f|g|h|~i)&(~a|~b|c|d|e|~f|g|~h|i)&(~a|~b|c|d|e|~f|g|~h|~i)&(~a|~b|c|d|e|~f|~g|h|~i)&(~a|~b|c|d|e|~f|~g|~h|i)&(~a|~b|c|d|e|~f|~g|~h|~i)&(~a|~b|c|d|~e|f|g|h|i)&(~a|~b|c|d|~e|f|g|h|~i)&(~a|~b|c|d|~e|f|g|~h|i)&(~a|~b|c|d|~e|f|g|~h|~i)&(~a|~b|c|d|~e|f|~g|h|i)&(~a|~b|c|d|~e|f|~g|h|~i)&(~a|~b|c|d|~e|f|~g|~h|i)&(~a|~b|c|d|~e|f|~g|~h|~i)&(~a|~b|c|d|~e|~f|g|h|~i)&(~a|~b|c|d|~e|~f|g|~h|i)&(~a|~b|c|d|~e|~f|g|~h|~i)&(~a|~b|c|d|~e|~f|~g|h|~i)&(~a|~b|c|d|~e|~f|~g|~h|i)&(~a|~b|c|d|~e|~f|~g|~h|~i)&(~a|~b|c|~d|e|f|g|h|i)&(~a|~b|c|~d|e|f|g|h|~i)&(~a|~b|c|~d|e|f|g|~h|i)&(~a|~b|c|~d|e|f|g|~h|~i)&(~a|~b|c|~d|e|f|~g|h|i)&(~a|~b|c|~d|e|f|~g|h|~i)&(~a|~b|c|~d|e|f|~g|~h|i)&(~a|~b|c|~d|e|f|~g|~h|~i)&(~a|~b|c|~d|e|~f|g|h|~i)&(~a|~b|c|~d|e|~f|g|~h|i)&(~a|~b|c|~d|e|~f|g|~h|~i)&(~a|~b|c|~d|e|~f|~g|h|~i)&(~a|~b|c|~d|e|~f|~g|~h|i)&(~a|~b|c|~d|e|~f|~g|~h|~i)&(~a|~b|c|~d|~e|f|g|h|i)&(~a|~b|c|~d|~e|f|g|h|~i)&(~a|~b|c|~d|~e|f|g|~h|i)&(~a|~b|c|~d|~e|f|g|~h|~i)&(~a|~b|c|~d|~e|f|~g|h|i)&(~a|~b|c|~d|~e|f|~g|h|~i)&(~a|~b|c|~d|~e|f|~g|~h|i)&(~a|~b|c|~d|~e|f|~g|~h|~i)&(~a|~b|c|~d|~e|~f|g|h|~i)&(~a|~b|c|~d|~e|~f|g|~h|i)&(~a|~b|c|~d|~e|~f|g|~h|~i)&(~a|~b|c|~d|~e|~f|~g|h|~i)&(~a|~b|c|~d|~e|~f|~g|~h|i)&(~a|~b|c|~d|~e|~f|~g|~h|~i)&(~a|~b|~c|d|e|f|g|h|i)&(~a|~b|~c|d|e|f|g|h|~i)&(~a|~b|~c|d|e|f|g|~h|i)&(~a|~b|~c|d|e|f|g|~h|~i)&(~a|~b|~c|d|e|f|~g|h|i)&(~a|~b|~c|d|e|f|~g|h|~i)&(~a|~b|~c|d|e|f|~g|~h|i)&(~a|~b|~c|d|e|f|~g|~h|~i)&(~a|~b|~c|d|e|~f|g|h|~i)&(~a|~b|~c|d|e|~f|g|~h|i)&(~a|~b|~c|d|e|~f|g|~h|~i)&(~a|~b|~c|d|e|~f|~g|h|~i)&(~a|~b|~c|d|e|~f|~g|~h|i)&(~a|~b|~c|d|e|~f|~g|~h|~i)&(~a|~b|~c|d|~e|f|g|h|i)&(~a|~b|~c|d|~e|f|g|h|~i)&(~a|~b|~c|d|~e|f|g|~h|i)&(~a|~b|~c|d|~e|f|g|~h|~i)&(~a|~b|~c|d|~e|f|~g|h|i)&(~a|~b|~c|d|~e|f|~g|h|~i)&(~a|~b|~c|d|~e|f|~g|~h|i)&(~a|~b|~c|d|~e|f|~g|~h|~i)&(~a|~b|~c|d|~e|~f|g|h|~i)&(~a|~b|~c|d|~e|~f|g|~h|i)&(~a|~b|~c|d|~e|~f|g|~h|~i)&(~a|~b|~c|d|~e|~f|~g|h|~i)&(~a|~b|~c|d|~e|~f|~g|~h|i)&(~a|~b|~c|d|~e|~f|~g|~h|~i)&(~a|~b|~c|~d|e|f|g|h|i)&(~a|~b|~c|~d|e|f|g|h|~i)&(~a|~b|~c|~d|e|f|g|~h|i)&(~a|~b|~c|~d|e|f|g|~h|~i)&(~a|~b|~c|~d|e|f|~g|h|i)&(~a|~b|~c|~d|e|f|~g|h|~i)&(~a|~b|~c|~d|e|f|~g|~h|i)&(~a|~b|~c|~d|e|f|~g|~h|~i)&(~a|~b|~c|~d|e|~f|g|h|~i)&(~a|~b|~c|~d|e|~f|g|~h|i)&(~a|~b|~c|~d|e|~f|g|~h|~i)&(~a|~b|~c|~d|e|~f|~g|h|~i)&(~a|~b|~c|~d|e|~f|~g|~h|i)&(~a|~b|~c|~d|e|~f|~g|~h|~i)&(~a|~b|~c|~d|~e|f|g|h|i)&(~a|~b|~c|~d|~e|f|g|h|~i)&(~a|~b|~c|~d|~e|f|g|~h|i)&(~a|~b|~c|~d|~e|f|g|~h|~i)&(~a|~b|~c|~d|~e|f|~g|h|i)&(~a|~b|~c|~d|~e|f|~g|h|~i)&(~a|~b|~c|~d|~e|f|~g|~h|i)&(~a|~b|~c|~d|~e|f|~g|~h|~i)&(~a|~b|~c|~d|~e|~f|g|h|~i)&(~a|~b|~c|~d|~e|~f|g|~h|i)&(~a|~b|~c|~d|~e|~f|g|~h|~i)&(~a|~b|~c|~d|~e|~f|~g|h|~i)&(~a|~b|~c|~d|~e|~f|~g|~h|i)&(~a|~b|~c|~d|~e|~f|~g|~h|~i)
    a      b      c      d      e      f      g      h      i      value
    False  False  False  False  False  False  False  False  False  False
    False  False  False  False  False  False  False  False  True   False
    False  False  False  False  False  False  False  True   False  False
    False  False  False  False  False  False  False  True   True   False
    False  False  False  False  False  False  True   False  False  False
    False  False  False  False  False  False  True   False  True   False
    False  False  False  False  False  False  True   True   False  False
    False  False  False  False  False  False  True   True   True   False
    False  False  False  False  False  True   False  False  False  False
    False  False  False  False  False  True   False  False  True   False
    False  False  False  False  False  True   False  True   False  False
    False  False  False  False  False  True   False  True   True   False
    False  False  False  False  False  True   True   False  False  False
    False  False  False  False  False  True   True   False  True   False
    False  False  False  False  False  True   True   True   False  False
    False  False  False  False  False  True   True   True   True   False
    False  False  False  False  True   False  False  False  False  False
    False  False  False  False  True   False  False  False  True   False
    False  False  False  False  True   False  False  True   False  False
    False  False  False  False  True   False  False  True   True   False
    False  False  False  False  True   False  True   False  False  False
    False  False  False  False  True   False  True   False  True   False
    False  False  False  False  True   False  True   True   False  False
    False  False  False  False  True   False  True   True   True   False
    False  False  False  False  True   True   False  False  False  False
    False  False  False  False  True   True   False  False  True   False
    False  False  False  False  True   True   False  True   False  False
    False  False  False  False  True   True   False  True   True   False
    False  False  False  False  True   True   True   False  False  False
    False  False  False  False  True   True   True   False  True   False
    False  False  False  False  True   True   True   True   False  False
    False  False  False  False  True   True   True   True   True   False
    False  False  False  True   False  False  False  False  False  False
    False  False  False  True   False  False  False  False  True   False
    False  False  False  True   False  False  False  True   False  False
    False  False  False  True   False  False  False  True   True   False
    False  False  False  True   False  False  True   False  False  False
    False  False  False  True   False  False  True   False  True   False
    False  False  False  True   False  False  True   True   False  False
    False  False  False  True   False  False  True   True   True   False
    False  False  False  True   False  True   False  False  False  False
    False  False  False  True   False  True   False  False  True   False
    False  False  False  True   False  True   False  True   False  False
    False  False  False  True   False  True   False  True   True   False
    False  False  False  True   False  True   True   False  False  False
    False  False  False  True   False  True   True   False  True   False
    False  False  False  True   False  True   True   True   False  False
    False  False  False  True   False  True   True   True   True   False
    False  False  False  True   True   False  False  False  False  False
    False  False  False  True   True   False  False  False  True   False
    False  False  False  True   True   False  False  True   False  False
    False  False  False  True   True   False  False  True   True   False
    False  False  False  True   True   False  True   False  False  False
    False  False  False  True   True   False  True   False  True   False
    False  False  False  True   True   False  True   True   False  False
    False  False  False  True   True   False  True   True   True   False
    False  False  False  True   True   True   False  False  False  False
    False  False  False  True   True   True   False  False  True   False
    False  False  False  True   True   True   False  True   False  False
    False  False  False  True   True   True   False  True   True   False
    False  False  False  True   True   True   True   False  False  False
    False  False  False  True   True   True   True   False  True   False
    False  False  False  True   True   True   True   True   False  False
    False  False  False  True   True   True   True   True   True   False
    False  False  True   False  False  False  False  False  False  False
    False  False  True   False  False  False  False  False  True   False
    False  False  True   False  False  False  False  True   False  False
    False  False  True   False  False  False  False  True   True   False
    False  False  True   False  False  False  True   False  False  False
    False  False  True   False  False  False  True   False  True   False
    False  False  True   False  False  False  True   True   False  False
    False  False  True   False  False  False  True   True   True   False
    False  False  True   False  False  True   False  False  False  False
    False  False  True   False  False  True   False  False  True   False
    False  False  True   False  False  True   False  True   False  False
    False  False  True   False  False  True   False  True   True   False
    False  False  True   False  False  True   True   False  False  False
    False  False  True   False  False  True   True   False  True   False
    False  False  True   False  False  True   True   True   False  False
    False  False  True   False  False  True   True   True   True   False
    False  False  True   False  True   False  False  False  False  False
    False  False  True   False  True   False  False  False  True   False
    False  False  True   False  True   False  False  True   False  False
    False  False  True   False  True   False  False  True   True   False
    False  False  True   False  True   False  True   False  False  False
    False  False  True   False  True   False  True   False  True   False
    False  False  True   False  True   False  True   True   False  False
    False  False  True   False  True   False  True   True   True   False
    False  False  True   False  True   True   False  False  False  False
    False  False  True   False  True   True   False  False  True   False
    False  False  True   False  True   True   False  True   False  False
    False  False  True   False  True   True   False  True   True   False
    False  False  True   False  True   True   True   False  False  False
    False  False  True   False  True   True   True   False  True   False
    False  False  True   False  True   True   True   True   False  False
    False  False  True   False  True   True   True   True   True   False
    False  False  True   True   False  False  False  False  False  False
    False  False  True   True   False  False  False  False  True   False
    False  False  True   True   False  False  False  True   False  False
    False  False  True   True   False  False  False  True   True   False
    False  False  True   True   False  False  True   False  False  False
    False  False  True   True   False  False  True   False  True   False
    False  False  True   True   False  False  True   True   False  False
    False  False  True   True   False  False  True   True   True   False
    False  False  True   True   False  True   False  False  False  False
    False  False  True   True   False  True   False  False  True   False
    False  False  True   True   False  True   False  True   False  False
    False  False  True   True   False  True   False  True   True   False
    False  False  True   True   False  True   True   False  False  False
    False  False  True   True   False  True   True   False  True   False
    False  False  True   True   False  True   True   True   False  False
    False  False  True   True   False  True   True   True   True   False
    False  False  True   True   True   False  False  False  False  False
    False  False  True   True   True   False  False  False  True   False
    False  False  True   True   True   False  False  True   False  False
    False  False  True   True   True   False  False  True   True   False
    False  False  True   True   True   False  True   False  False  False
    False  False  True   True   True   False  True   False  True   False
    False  False  True   True   True   False  True   True   False  False
    False  False  True   True   True   False  True   True   True   False
    False  False  True   True   True   True   False  False  False  False
    False  False  True   True   True   True   False  False  True   False
    False  False  True   True   True   True   False  True   False  False
    False  False  True   True   True   True   False  True   True   False
    False  False  True   True   True   True   True   False  False  False
    False  False  True   True   True   True   True   False  True   False
    False  False  True   True   True   True   True   True   False  False
    False  False  True   True   True   True   True   True   True   False
    False  True   False  False  False  False  False  False  False  False
    False  True   False  False  False  False  False  False  True   False
    False  True   False  False  False  False  False  True   False  False
    False  True   False  False  False  False  False  True   True   False
    False  True   False  False  False  False  True   False  False  False
    False  True   False  False  False  False  True   False  True   False
    False  True   False  False  False  False  True   True   False  False
    False  True   False  False  False  False  True   True   True   False
    False  True   False  False  False  True   False  False  False  False
    False  True   False  False  False  True   False  False  True   False
    False  True   False  False  False  True   False  True   False  False
    False  True   False  False  False  True   False  True   True   False
    False  True   False  False  False  True   True   False  False  False
    False  True   False  False  False  True   True   False  True   False
    False  True   False  False  False  True   True   True   False  False
    False  True   False  False  False  True   True   True   True   False
    False  True   False  False  True   False  False  False  False  False
    False  True   False  False  True   False  False  False  True   False
    False  True   False  False  True   False  False  True   False  False
    False  True   False  False  True   False  False  True   True   False
    False  True   False  False  True   False  True   False  False  False
    False  True   False  False  True   False  True   False  True   False
    False  True   False  False  True   False  True   True   False  False
    False  True   False  False  True   False  True   True   True   False
    False  True   False  False  True   True   False  False  False  False
    False  True   False  False  True   True   False  False  True   False
    False  True   False  False  True   True   False  True   False  False
    False  True   False  False  True   True   False  True   True   False
    False  True   False  False  True   True   True   False  False  False
    False  True   False  False  True   True   True   False  True   False
    False  True   False  False  True   True   True   True   False  False
    False  True   False  False  True   True   True   True   True   False
    False  True   False  True   False  False  False  False  False  False
    False  True   False  True   False  False  False  False  True   False
    False  True   False  True   False  False  False  True   False  False
    False  True   False  True   False  False  False  True   True   False
    False  True   False  True   False  False  True   False  False  False
    False  True   False  True   False  False  True   False  True   False
    False  True   False  True   False  False  True   True   False  False
    False  True   False  True   False  False  True   True   True   False
    False  True   False  True   False  True   False  False  False  False
    False  True   False  True   False  True   False  False  True   False
    False  True   False  True   False  True   False  True   False  False
    False  True   False  True   False  True   False  True   True   False
    False  True   False  True   False  True   True   False  False  False
    False  True   False  True   False  True   True   False  True   False
    False  True   False  True   False  True   True   True   False  False
    False  True   False  True   False  True   True   True   True   False
    False  True   False  True   True   False  False  False  False  False
    False  True   False  True   True   False  False  False  True   False
    False  True   False  True   True   False  False  True   False  False
    False  True   False  True   True   False  False  True   True   False
    False  True   False  True   True   False  True   False  False  False
    False  True   False  True   True   False  True   False  True   False
    False  True   False  True   True   False  True   True   False  False
    False  True   False  True   True   False  True   True   True   False
    False  True   False  True   True   True   False  False  False  False
    False  True   False  True   True   True   False  False  True   False
    False  True   False  True   True   True   False  True   False  False
    False  True   False  True   True   True   False  True   True   False
    False  True   False  True   True   True   True   False  False  False
    False  True   False  True   True   True   True   False  True   False
    False  True   False  True   True   True   True   True   False  False
    False  True   False  True   True   True   True   True   True   False
    False  True   True   False  False  False  False  False  False  False
    False  True   True   False  False  False  False  False  True   False
    False  True   True   False  False  False  False  True   False  False
    False  True   True   False  False  False  False  True   True   False
    False  True   True   False  False  False  True   False  False  False
    False  True   True   False  False  False  True   False  True   False
    False  True   True   False  False  False  True   True   False  False
    False  True   True   False  False  False  True   True   True   False
    False  True   True   False  False  True   False  False  False  False
    False  True   True   False  False  True   False  False  True   False
    False  True   True   False  False  True   False  True   False  False
    False  True   True   False  False  True   False  True   True   False
    False  True   True   False  False  True   True   False  False  False
    False  True   True   False  False  True   True   False  True   False
    False  True   True   False  False  True   True   True   False  False
    False  True   True   False  False  True   True   True   True   False
    False  True   True   False  True   False  False  False  False  False
    False  True   True   False  True   False  False  False  True   False
    False  True   True   False  True   False  False  True   False  False
    False  True   True   False  True   False  False  True   True   False
    False  True   True   False  True   False  True   False  False  False
    False  True   True   False  True   False  True   False  True   False
    False  True   True   False  True   False  True   True   False  False
    False  True   True   False  True   False  True   True   True   False
    False  True   True   False  True   True   False  False  False  False
    False  True   True   False  True   True   False  False  True   False
    False  True   True   False  True   True   False  True   False  False
    False  True   True   False  True   True   False  True   True   False
    False  True   True   False  True   True   True   False  False  False
    False  True   True   False  True   True   True   False  True   False
    False  True   True   False  True   True   True   True   False  False
    False  True   True   False  True   True   True   True   True   False
    False  True   True   True   False  False  False  False  False  False
    False  True   True   True   False  False  False  False  True   False
    False  True   True   True   False  False  False  True   False  False
    False  True   True   True   False  False  False  True   True   False
    False  True   True   True   False  False  True   False  False  False
    False  True   True   True   False  False  True   False  True   False
    False  True   True   True   False  False  True   True   False  False
    False  True   True   True   False  False  True   True   True   False
    False  True   True   True   False  True   False  False  False  False
    False  True   True   True   False  True   False  False  True   False
    False  True   True   True   False  True   False  True   False  False
    False  True   True   True   False  True   False  True   True   False
    False  True   True   True   False  True   True   False  False  False
    False  True   True   True   False  True   True   False  True   False
    False  True   True   True   False  True   True   True   False  False
    False  True   True   True   False  True   True   True   True   False
    False  True   True   True   True   False  False  False  False  False
    False  True   True   True   True   False  False  False  True   False
    False  True   True   True   True   False  False  True   False  False
    False  True   True   True   True   False  False  True   True   False
    False  True   True   True   True   False  True   False  False  False
    False  True   True   True   True   False  True   False  True   False
    False  True   True   True   True   False  True   True   False  False
    False  True   True   True   True   False  True   True   True   False
    False  True   True   True   True   True   False  False  False  False
    False  True   True   True   True   True   False  False  True   False
    False  True   True   True   True   True   False  True   False  False
    False  True   True   True   True   True   False  True   True   False
    False  True   True   True   True   True   True   False  False  False
    False  True   True   True   True   True   True   False  True   False
    False  True   True   True   True   True   True   True   False  False
    False  True   True   True   True   True   True   True   True   False
    True   False  False  False  False  False  False  False  False  False
    True   False  False  False  False  False  False  False  True   False
    True   False  False  False  False  False  False  True   False  False
    True   False  False  False  False  False  False  True   True   False
    True   False  False  False  False  False  True   False  False  False
    True   False  False  False  False  False  True   False  True   False
    True   False  False  False  False  False  True   True   False  False
    True   False  False  False  False  False  True   True   True   False
    True   False  False  False  False  True   False  False  False  True
    True   False  False  False  False  True   False  False  True   False
    True   False  False  False  False  True   False  True   False  False
    True   False  False  False  False  True   False  True   True   False
    True   False  False  False  False  True   True   False  False  True
    True   False  False  False  False  True   True   False  True   False
    True   False  False  False  False  True   True   True   False  False
    True   False  False  False  False  True   True   True   True   False
    True   False  False  False  True   False  False  False  False  False
    True   False  False  False  True   False  False  False  True   False
    True   False  False  False  True   False  False  True   False  False
    True   False  False  False  True   False  False  True   True   False
    True   False  False  False  True   False  True   False  False  False
    True   False  False  False  True   False  True   False  True   False
    True   False  False  False  True   False  True   True   False  False
    True   False  False  False  True   False  True   True   True   False
    True   False  False  False  True   True   False  False  False  True
    True   False  False  False  True   True   False  False  True   False
    True   False  False  False  True   True   False  True   False  False
    True   False  False  False  True   True   False  True   True   False
    True   False  False  False  True   True   True   False  False  True
    True   False  False  False  True   True   True   False  True   False
    True   False  False  False  True   True   True   True   False  False
    True   False  False  False  True   True   True   True   True   False
    True   False  False  True   False  False  False  False  False  False
    True   False  False  True   False  False  False  False  True   False
    True   False  False  True   False  False  False  True   False  False
    True   False  False  True   False  False  False  True   True   False
    True   False  False  True   False  False  True   False  False  False
    True   False  False  True   False  False  True   False  True   False
    True   False  False  True   False  False  True   True   False  False
    True   False  False  True   False  False  True   True   True   False
    True   False  False  True   False  True   False  False  False  True
    True   False  False  True   False  True   False  False  True   False
    True   False  False  True   False  True   False  True   False  False
    True   False  False  True   False  True   False  True   True   False
    True   False  False  True   False  True   True   False  False  True
    True   False  False  True   False  True   True   False  True   False
    True   False  False  True   False  True   True   True   False  False
    True   False  False  True   False  True   True   True   True   False
    True   False  False  True   True   False  False  False  False  False
    True   False  False  True   True   False  False  False  True   False
    True   False  False  True   True   False  False  True   False  False
    True   False  False  True   True   False  False  True   True   False
    True   False  False  True   True   False  True   False  False  False
    True   False  False  True   True   False  True   False  True   False
    True   False  False  True   True   False  True   True   False  False
    True   False  False  True   True   False  True   True   True   False
    True   False  False  True   True   True   False  False  False  True
    True   False  False  True   True   True   False  False  True   False
    True   False  False  True   True   True   False  True   False  False
    True   False  False  True   True   True   False  True   True   False
    True   False  False  True   True   True   True   False  False  True
    True   False  False  True   True   True   True   False  True   False
    True   False  False  True   True   True   True   True   False  False
    True   False  False  True   True   True   True   True   True   False
    True   False  True   False  False  False  False  False  False  False
    True   False  True   False  False  False  False  False  True   False
    True   False  True   False  False  False  False  True   False  False
    True   False  True   False  False  False  False  True   True   False
    True   False  True   False  False  False  True   False  False  False
    True   False  True   False  False  False  True   False  True   False
    True   False  True   False  False  False  True   True   False  False
    True   False  True   False  False  False  True   True   True   False
    True   False  True   False  False  True   False  False  False  True
    True   False  True   False  False  True   False  False  True   False
    True   False  True   False  False  True   False  True   False  False
    True   False  True   False  False  True   False  True   True   False
    True   False  True   False  False  True   True   False  False  True
    True   False  True   False  False  True   True   False  True   False
    True   False  True   False  False  True   True   True   False  False
    True   False  True   False  False  True   True   True   True   False
    True   False  True   False  True   False  False  False  False  False
    True   False  True   False  True   False  False  False  True   False
    True   False  True   False  True   False  False  True   False  False
    True   False  True   False  True   False  False  True   True   False
    True   False  True   False  True   False  True   False  False  False
    True   False  True   False  True   False  True   False  True   False
    True   False  True   False  True   False  True   True   False  False
    True   False  True   False  True   False  True   True   True   False
    True   False  True   False  True   True   False  False  False  True
    True   False  True   False  True   True   False  False  True   False
    True   False  True   False  True   True   False  True   False  False
    True   False  True   False  True   True   False  True   True   False
    True   False  True   False  True   True   True   False  False  True
    True   False  True   False  True   True   True   False  True   False
    True   False  True   False  True   True   True   True   False  False
    True   False  True   False  True   True   True   True   True   False
    True   False  True   True   False  False  False  False  False  False
    True   False  True   True   False  False  False  False  True   False
    True   False  True   True   False  False  False  True   False  False
    True   False  True   True   False  False  False  True   True   False
    True   False  True   True   False  False  True   False  False  False
    True   False  True   True   False  False  True   False  True   False
    True   False  True   True   False  False  True   True   False  False
    True   False  True   True   False  False  True   True   True   False
    True   False  True   True   False  True   False  False  False  True
    True   False  True   True   False  True   False  False  True   False
    True   False  True   True   False  True   False  True   False  False
    True   False  True   True   False  True   False  True   True   False
    True   False  True   True   False  True   True   False  False  True
    True   False  True   True   False  True   True   False  True   False
    True   False  True   True   False  True   True   True   False  False
    True   False  True   True   False  True   True   True   True   False
    True   False  True   True   True   False  False  False  False  False
    True   False  True   True   True   False  False  False  True   False
    True   False  True   True   True   False  False  True   False  False
    True   False  True   True   True   False  False  True   True   False
    True   False  True   True   True   False  True   False  False  False
    True   False  True   True   True   False  True   False  True   False
    True   False  True   True   True   False  True   True   False  False
    True   False  True   True   True   False  True   True   True   False
    True   False  True   True   True   True   False  False  False  True
    True   False  True   True   True   True   False  False  True   False
    True   False  True   True   True   True   False  True   False  False
    True   False  True   True   True   True   False  True   True   False
    True   False  True   True   True   True   True   False  False  True
    True   False  True   True   True   True   True   False  True   False
    True   False  True   True   True   True   True   True   False  False
    True   False  True   True   True   True   True   True   True   False
    True   True   False  False  False  False  False  False  False  False
    True   True   False  False  False  False  False  False  True   False
    True   True   False  False  False  False  False  True   False  False
    True   True   False  False  False  False  False  True   True   False
    True   True   False  False  False  False  True   False  False  False
    True   True   False  False  False  False  True   False  True   False
    True   True   False  False  False  False  True   True   False  False
    True   True   False  False  False  False  True   True   True   False
    True   True   False  False  False  True   False  False  False  True
    True   True   False  False  False  True   False  False  True   False
    True   True   False  False  False  True   False  True   False  False
    True   True   False  False  False  True   False  True   True   False
    True   True   False  False  False  True   True   False  False  True
    True   True   False  False  False  True   True   False  True   False
    True   True   False  False  False  True   True   True   False  False
    True   True   False  False  False  True   True   True   True   False
    True   True   False  False  True   False  False  False  False  False
    True   True   False  False  True   False  False  False  True   False
    True   True   False  False  True   False  False  True   False  False
    True   True   False  False  True   False  False  True   True   False
    True   True   False  False  True   False  True   False  False  False
    True   True   False  False  True   False  True   False  True   False
    True   True   False  False  True   False  True   True   False  False
    True   True   False  False  True   False  True   True   True   False
    True   True   False  False  True   True   False  False  False  True
    True   True   False  False  True   True   False  False  True   False
    True   True   False  False  True   True   False  True   False  False
    True   True   False  False  True   True   False  True   True   False
    True   True   False  False  True   True   True   False  False  True
    True   True   False  False  True   True   True   False  True   False
    True   True   False  False  True   True   True   True   False  False
    True   True   False  False  True   True   True   True   True   False
    True   True   False  True   False  False  False  False  False  False
    True   True   False  True   False  False  False  False  True   False
    True   True   False  True   False  False  False  True   False  False
    True   True   False  True   False  False  False  True   True   False
    True   True   False  True   False  False  True   False  False  False
    True   True   False  True   False  False  True   False  True   False
    True   True   False  True   False  False  True   True   False  False
    True   True   False  True   False  False  True   True   True   False
    True   True   False  True   False  True   False  False  False  True
    True   True   False  True   False  True   False  False  True   False
    True   True   False  True   False  True   False  True   False  False
    True   True   False  True   False  True   False  True   True   False
    True   True   False  True   False  True   True   False  False  True
    True   True   False  True   False  True   True   False  True   False
    True   True   False  True   False  True   True   True   False  False
    True   True   False  True   False  True   True   True   True   False
    True   True   False  True   True   False  False  False  False  False
    True   True   False  True   True   False  False  False  True   False
    True   True   False  True   True   False  False  True   False  False
    True   True   False  True   True   False  False  True   True   False
    True   True   False  True   True   False  True   False  False  False
    True   True   False  True   True   False  True   False  True   False
    True   True   False  True   True   False  True   True   False  False
    True   True   False  True   True   False  True   True   True   False
    True   True   False  True   True   True   False  False  False  True
    True   True   False  True   True   True   False  False  True   False
    True   True   False  True   True   True   False  True   False  False
    True   True   False  True   True   True   False  True   True   False
    True   True   False  True   True   True   True   False  False  True
    True   True   False  True   True   True   True   False  True   False
    True   True   False  True   True   True   True   True   False  False
    True   True   False  True   True   True   True   True   True   False
    True   True   True   False  False  False  False  False  False  False
    True   True   True   False  False  False  False  False  True   False
    True   True   True   False  False  False  False  True   False  False
    True   True   True   False  False  False  False  True   True   False
    True   True   True   False  False  False  True   False  False  False
    True   True   True   False  False  False  True   False  True   False
    True   True   True   False  False  False  True   True   False  False
    True   True   True   False  False  False  True   True   True   False
    True   True   True   False  False  True   False  False  False  True
    True   True   True   False  False  True   False  False  True   False
    True   True   True   False  False  True   False  True   False  False
    True   True   True   False  False  True   False  True   True   False
    True   True   True   False  False  True   True   False  False  True
    True   True   True   False  False  True   True   False  True   False
    True   True   True   False  False  True   True   True   False  False
    True   True   True   False  False  True   True   True   True   False
    True   True   True   False  True   False  False  False  False  False
    True   True   True   False  True   False  False  False  True   False
    True   True   True   False  True   False  False  True   False  False
    True   True   True   False  True   False  False  True   True   False
    True   True   True   False  True   False  True   False  False  False
    True   True   True   False  True   False  True   False  True   False
    True   True   True   False  True   False  True   True   False  False
    True   True   True   False  True   False  True   True   True   False
    True   True   True   False  True   True   False  False  False  True
    True   True   True   False  True   True   False  False  True   False
    True   True   True   False  True   True   False  True   False  False
    True   True   True   False  True   True   False  True   True   False
    True   True   True   False  True   True   True   False  False  True
    True   True   True   False  True   True   True   False  True   False
    True   True   True   False  True   True   True   True   False  False
    True   True   True   False  True   True   True   True   True   False
    True   True   True   True   False  False  False  False  False  False
    True   True   True   True   False  False  False  False  True   False
    True   True   True   True   False  False  False  True   False  False
    True   True   True   True   False  False  False  True   True   False
    True   True   True   True   False  False  True   False  False  False
    True   True   True   True   False  False  True   False  True   False
    True   True   True   True   False  False  True   True   False  False
    True   True   True   True   False  False  True   True   True   False
    True   True   True   True   False  True   False  False  False  True
    True   True   True   True   False  True   False  False  True   False
    True   True   True   True   False  True   False  True   False  False
    True   True   True   True   False  True   False  True   True   False
    True   True   True   True   False  True   True   False  False  True
    True   True   True   True   False  True   True   False  True   False
    True   True   True   True   False  True   True   True   False  False
    True   True   True   True   False  True   True   True   True   False
    True   True   True   True   True   False  False  False  False  False
    True   True   True   True   True   False  False  False  True   False
    True   True   True   True   True   False  False  True   False  False
    True   True   True   True   True   False  False  True   True   False
    True   True   True   True   True   False  True   False  False  False
    True   True   True   True   True   False  True   False  True   False
    True   True   True   True   True   False  True   True   False  False
    True   True   True   True   True   False  True   True   True   False
    True   True   True   True   True   True   False  False  False  True
    True   True   True   True   True   True   False  False  True   False
    True   True   True   True   True   True   False  True   False  False
    True   True   True   True   True   True   False  True   True   False
    True   True   True   True   True   True   True   False  False  True
    True   True   True   True   True   True   True   False  True   False
    True   True   True   True   True   True   True   True   False  False
    True   True   True   True   True   True   True   True   True   False
    """)
