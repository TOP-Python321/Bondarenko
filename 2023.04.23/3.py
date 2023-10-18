num = int(input())
divisors_sum = 0

for i in range(1, int(num**0.5)+1):
    if num % i == 0:
        divisors_sum += i
        if i != num // i:
            divisors_sum += num // i

print(divisors_sum)

# 4
# 7

