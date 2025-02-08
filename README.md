# The-SAT-Equation
The SAT Equation: Encoding Satisfying Assignments into an Integer.

Appendix:
A balanced CNF formula is a logical formula in Conjunctive Normal Form (CNF) that is balanced in such a way that each variable appears in the same number of positive and negative clauses. Let's break it down:

CNF (Conjunctive Normal Form): It is a way of structuring a logical formula where you have a conjunction (AND) of clauses, and each clause is a disjunction (OR) of literals. A literal is a variable or its negation. For example:

(
𝐴
∨
¬
𝐵
∨
𝐶
)
∧
(
𝐵
∨
𝐷
)
∧
(
¬
𝐴
∨
¬
𝐶
)
This formula is in CNF because it is a conjunction of clauses, and each clause is a disjunction of literals.

Balanced: A CNF formula is balanced if each variable appears the same number of times in positive form (like 
𝐴
) as in negative form (like 
¬
𝐴
). This means that if a variable appears 'n' times in one way, it must also appear 'n' times in the other way to be considered balanced.

For example, consider the formula:

(
𝐴
∨
¬
𝐵
)
∧
(
¬
𝐴
∨
𝐵
)
The variable 
𝐴
 appears once as 
𝐴
 and once as 
¬
𝐴
, which is balanced.

The variable 
𝐵
 appears once as 
𝐵
 and once as 
¬
𝐵
, which is also balanced.

In this formula, each variable appears the same number of times in positive and negative forms, so it can be considered a balanced CNF formula.
