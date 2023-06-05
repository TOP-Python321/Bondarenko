n = int(input())

fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print(*fib[:n])

# 23
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657

