# Sample Input

# 9 27
# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

N = int(input())
M = 3 * N

if 5 < N < 101 and 15 < M < 303:
    xenex = 1
    for num in range(1, N + 1):
        welcome = int(((N - 1)/2) +1)
        for xen in range(1):
            if num == welcome:
                print("WELCOME")

            else:
                if num > welcome:
                    print("-" * (M - xenex/2), ".|." * xenex, "-" * (M - xenex/2))
                    xenex -= 2
                else:
                    print( "-" * (M - xenex/2), ".|." * xenex, "-" * (M - xenex/2))
                    xenex += 2

    