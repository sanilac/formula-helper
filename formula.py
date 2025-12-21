import math
def compound_interest(p, r, n, t):
    """
    Calculates the final amount A using the compound interest formula.
    A = P * (1 + r/n)^(n*t)
    """
    # Calculate the term inside the parentheses: (1 + r/n)
    base = 1 + (r / n)

    # Calculate the exponent: (n*t)
    exponent = n * t

    # Use the math.pow function for the exponentiation: base ^ exponent
    factor = math.pow(base, exponent)

    # Final calculation: P * factor
    a = p * factor

    # Return the final amount
    return "The Future Value of an Annuity Formula is:", a
def calculate(a,b,operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return "Division by zero error" if b == 0 else a / b
    else:
        return "Not valid"
def quadratic_formula(a,b,c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0 :
        return "the zeroes are not real"
    else:
        root1 = (-b -math.sqrt(discriminant))/(2*a)
        root2 = (-b +math.sqrt(discriminant))/(2*a)
        if root1 == root2:
            return "The roots are real and equal",root1
        else:
            return"The roots are real and distant",root1,root2
def pythagoras(num1,num2,find):
    if find == "side":
        result = round(math.sqrt((num1**2)+(num2**2)),2)
        return result
    else:
        result1 = round(math.sqrt((num1**2)+(num2**2)),2)
        return result1
def ci_formula(p,r,n,t):
    base = 1+(r/n)
    factor = base **(n*t)
    result = p*factor
    return "This is the amount:",round(result,2)
def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1)+fibo(num-2)
def ap(first_term, cd ,n,sum_or_an):
    if n <=0:
        return "n must be a positive integer"
    if sum_or_an =="an":
        return round(first_term + (n - 1) * cd,2)
    elif sum_or_an =="sum":
        return round(n/2*(2*first_term+(n-1)*cd),2)
    else:
        return "Invalid option.Use sum or an"
def distance_for(x1,x2,y1,y2,):
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2)**2),2)
def section_for(x1,x2,y1,y2,m,n):
    x = (x1 * n + x2 * m) / (m + n)
    y = (y1 * n + y2 * m) / (m + n)
    return round(x, 2), round(y, 2)
if __name__ =="__main__":
    print("Welcome to the tron calculator")
    list1 = ["future value formula", "calculate", "quadratic formula", "pythagoras", "compound interest",
             "fibonacci series", "Arithmetic Progression", "distance formula", "section formula"]
    for l in list1:
        print(l)
