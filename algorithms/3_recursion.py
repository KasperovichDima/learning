def countdown(i):
    print(i)
    if not i:
        return
    countdown(i-1)

countdown(10)

def factorial(i: int):
    return i if i == 1 else i * factorial(i - 1)

print(factorial(3))