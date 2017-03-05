
def fibonacci(n):
    current = 0
    after = 1
    for i in range(n):
        current, after = after, current + after
    return current

print(fibonacci(36))
