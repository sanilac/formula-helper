# 🧮 TRON Calculator

> *"Because writing the same formulas over and over again is not the Tron Legacy we deserve."*

## 🚀 What is TRON Calculator?

TRON Calculator is your personal mathematical toolkit—a collection of battle-tested formulas wrapped in clean, reusable functions. Stop reinventing the wheel every time you need compound interest calculations or quadratic roots. Just import, call, and conquer.

Born from the frustration of copy-pasting math functions across projects, TRON Calculator is here to save your time, reduce bugs, and make your code cleaner than a freshly compiled Python module.

## ✨ Features

TRON Calculator comes loaded with **9 essential mathematical operations**:

### 📈 Financial Mathematics
- **Future Value Formula** - Calculate investment growth with compound interest
- **Compound Interest** - Determine the magic of exponential growth on your principal

### 🔢 Basic Operations
- **Calculate** - Four basic operations (+, -, *, /) with zero-division protection

### 📐 Algebra & Geometry
- **Quadratic Formula** - Find roots of any quadratic equation (real or complex detection included)
- **Pythagoras Theorem** - Calculate the hypotenuse or verify right triangles
- **Distance Formula** - Measure the distance between two points in 2D space
- **Section Formula** - Find the point dividing a line segment in a given ratio

### 🔢 Number Theory
- **Fibonacci Series** - Generate Fibonacci numbers recursively
- **Arithmetic Progression** - Calculate nth term or sum of AP series

## 🎯 Why Use TRON Calculator?

```python
# WITHOUT TRON Calculator 😫
def calculate_compound_interest(p, r, n, t):
    base = 1 + (r / n)
    exponent = n * t
    factor = math.pow(base, exponent)
    a = p * factor
    return a

result = calculate_compound_interest(10000, 0.05, 12, 10)
```

```python
# WITH TRON Calculator 😎
from tron_calculator import ci_formula

result = ci_formula(10000, 0.05, 12, 10)
```

**One import. Zero headaches.**

## 📦 Installation

Simply download `tron_calculator.py` and place it in your project directory or Python path.

```bash
# Clone or download the file
# Then in your project:
```

```python
from tron_calculator import *
# Or import specific functions
from tron_calculator import ci_formula, quadratic_formula, calculate
```

## 🎮 Usage Examples

### 💰 Calculate Investment Growth
```python
from tron_calculator import ci_formula

# Principal: $5000, Rate: 6% annually, Compounded monthly, Time: 5 years
future_value = ci_formula(5000, 0.06, 12, 5)
print(future_value)
# Output: "This is the amount: 6744.25"
```

### 🔍 Solve Quadratic Equations
```python
from tron_calculator import quadratic_formula

# Solve: 2x² + 5x - 3 = 0
roots = quadratic_formula(2, 5, -3)
print(roots)
# Output: ('The roots are real and distant', -3.0, 0.5)
```

### 📏 Calculate Distance Between Points
```python
from tron_calculator import distance_for

# Distance between (1, 2) and (4, 6)
dist = distance_for(1, 4, 2, 6)
print(dist)
# Output: 5.0
```

### 🌀 Generate Fibonacci Numbers
```python
from tron_calculator import fibo

# Get the 10th Fibonacci number
result = fibo(10)
print(result)
# Output: 55
```

### 📊 Arithmetic Progression Calculations
```python
from tron_calculator import ap

# Find 15th term: first term=3, common difference=4
nth_term = ap(3, 4, 15, "an")
print(nth_term)
# Output: 59.0

# Find sum of first 15 terms
sum_terms = ap(3, 4, 15, "sum")
print(sum_terms)
# Output: 465.0
```

## 🛠️ Function Reference

| Function | Parameters | Returns | Description |
|----------|-----------|---------|-------------|
| `compound_interest()` | p, r, n, t | tuple | Future value with label |
| `ci_formula()` | p, r, n, t | string | Formatted compound interest result |
| `calculate()` | a, b, operation | number/string | Basic arithmetic operations |
| `quadratic_formula()` | a, b, c | tuple | Roots of quadratic equation |
| `pythagoras()` | num1, num2, find | number | Hypotenuse calculation |
| `fibo()` | num | number | nth Fibonacci number |
| `ap()` | first_term, cd, n, sum_or_an | number/string | AP term or sum |
| `distance_for()` | x1, x2, y1, y2 | number | Distance between points |
| `section_for()` | x1, x2, y1, y2, m, n | tuple | Point dividing line segment |

## 🎓 Perfect For

- **Students** - Focus on problem-solving, not formula implementation
- **Data Scientists** - Quick mathematical operations without overhead
- **Developers** - Clean, tested functions ready to integrate
- **Educators** - Demonstrate concepts without boilerplate code

## 🤝 Contributing

Found a bug? Want to add more formulas? Contributions are welcome! This is a living toolkit that grows with the community's needs.

## 📝 License

Free to use, modify, and distribute. Because math belongs to everyone.

## 💡 Pro Tips

1. **Import selectively** to keep your namespace clean
2. **Check return types** - some functions return tuples, others return formatted strings
3. **Validate inputs** - the functions assume valid numerical inputs
4. **Round results** - most functions already round to 2 decimal places

---

**Built with 💙 by the developer who was tired of writing the same formulas again and again.**

*TRON Calculator - Because your time is too valuable to waste on repetitive code.*
