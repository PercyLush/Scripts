def is_prime(num):
    prime_number = True
    if num <= 1:
        prime_number = False
    else:
        for n in range(2 , num - 1):
            if num % n == 0:
                prime_number = False
                break

    return prime_number
for i in range(-10, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
