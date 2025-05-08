def sqrt_newton(x, tolerance=1e-10):
    guess = x / 2.0
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2.0
    return guess

print(sqrt_newton(2))