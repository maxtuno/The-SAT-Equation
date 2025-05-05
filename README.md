# The SAT Equation: An Arithmetic Framework for Boolean Satisfiability

## Abstract
In this paper, we present an innovative arithmetic formulation that captures the essence of Boolean Satisfiability (SAT). By representing Conjunctive Normal Form (CNF) clauses through binary and arithmetic expressions, we establish a novel equivalence that bridges logical operations with numerical computations. This framework not only provides deeper insights into SAT problems but also offers potential computational advantages.

## Introduction
Boolean satisfiability is a fundamental problem in computer science, involving the determination of whether there exists an assignment to boolean variables such that a given Boolean formula evaluates to true. Typically expressed in CNF, these formulas consist of conjunctions of disjunctions (clauses) of literals. We introduce an arithmetic representation for these clauses, facilitating analysis through binary and power-of-two operations.

## Theorem
We propose the following theorem as a foundational result:

```math
\sum_{j=0}^{m-1} 2^{\sum_{i=0}^{n-1} x_{(n-1-i)j}^{2^i}} = (x_{0,0}^\pm \vee \ldots \vee x_{n-1,0}^\pm) \wedge \ldots \wedge (x_{0,m-1}^\pm \vee \ldots \vee x_{n-1,m-1}^\pm)
```

### Proof Outline
The proof begins by interpreting CNF clauses through binary arithmetic. A CNF clause is false if all its literals are false, which can be encoded as a binary number where true values map to 0 and false values to 1. For a set of variables $X = \{x_0, x_1, \ldots, x_{n-1}\}$, the possible assignments range from $0$ (all true) to $2^n - 1$ (all false).

```math
\begin{array}{}
0 & \underbrace{00 \ldots 00}_{|\mathcal{X}|} \\
1 & \underbrace{00 \ldots 01}_{|\mathcal{X}|} \\
\vdots & \vdots \\
2^{|\mathcal{X}|}-2 & \underbrace{11 \ldots 10}_{|\mathcal{X}|} \\
2^{|\mathcal{X}|}-1 & \underbrace{11 \ldots 11}_{|\mathcal{X}|} \\
\end{array}
```

Each CNF clause can be represented by summing over powers of two corresponding to the positions of true literals in its assignment. This transformation allows us to express the satisfaction condition of a CNF formula as an arithmetic summation:

```math
\sum_{j=0}^{m-1} 2^{\sum_{i=0}^{n-1} x_{(n-1-i)j}^{2^i}}
```

This sum captures all satisfying assignments for the entire CNF formula, where each term corresponds to a clause being true under a particular assignment.

## Balanced Condition
A balanced CNF formula is one in which every variable appears an equal number of times in both positive and negative forms. For instance:

```math
(A \vee \neg B) \wedge (\neg A \vee B)
```

In this example, each variable \(A\) and \(B\) appears once positively and once negatively, illustrating balance.

## Discussion
This arithmetic representation of SAT provides a novel perspective on the problem, potentially enabling new algorithmic approaches. By translating logical conditions into numerical operations, we can leverage existing mathematical tools to analyze and solve SAT instances more efficiently.

## Conclusion
The equivalence established between CNF clauses and their arithmetic counterparts offers a promising avenue for further research in satisfiability problems. This framework not only enriches our theoretical understanding but also opens up possibilities for practical advancements in solving complex Boolean formulas.

Future work will focus on exploring computational optimizations and extending this approach to other logical frameworks beyond CNF.

```python
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
```

# references:
https://www.academia.edu/129202540/A_Unique_Encoding_of_Satisfying_Assignments_for_Balanced_CNFs
https://www.academia.edu/27914083/NUMBER_THEORY_EQUATION_OF_SAT
https://www.academia.edu/28123997/PROOF_OF_ARITHMETIC_BOOLEAN_SATISFIABILITY_EQUATION
https://github.com/maxtuno/SAT_EQUATION
