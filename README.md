# Pell-equation-solver
## Generates the fundamental solution to Pell's equation, for any n

Pell's equation are equations of the form

x<sup>2</sup> - n*y<sup>2</sup> = 1

The fundamental solution is the pair (x, y) that solves the equation with the minimum x.
The trivial solution always exist (x=1, y=0), but if you obtain a non-trivial solution, you can generate the rest of the inifinite solutions.

(There is only 1 possible solution, the trivial, if n is a perfect square)

This implementation uses the continued fractions method.

To solve Pell's equation for an arbitrary n, download pell.py and do:

```
python pell.py n
```

Where n is the integer to solve for
