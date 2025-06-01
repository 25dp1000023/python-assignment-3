n=int(input('Enter a number: '))

def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)

result="Factorial of 5 is:",factorial(n)
print(result)