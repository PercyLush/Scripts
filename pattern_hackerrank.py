# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------

try:
    N, M = int(input()).split()
    print(f"{N}, {M}")
    welcome_number = int((N - 1)/2 + 1)

    counter1 = 1
    dash = 3
    dash1 = 1
    test1 = M
    test2 = M

    if 5 < N < 101 and 15 < M < 303:
        for length in range(1, N + 1):
            
            if length == welcome_number:
                num = int((M - 7)/2)
                print(f"{'-'*num}{'WELCOME'}{'-'*num}")

            else:
                if length < welcome_number:
                    dash_num = int((test1 - dash)/2)
                    print(f"{'-'*dash_num}{'.|.'*counter1}{'-'*dash_num}")
                    counter1 += 2
                    dash += 3
                    test1 -= 3
                elif length > welcome_number:
                    counter1 -= 2
                    dash_num = test2 - int(test2 - 3*dash1)
                    print(f"{'-'*dash_num}{'.|.'*counter1}{'-'*dash_num}")
                    dash1 += 1
except:
    print("Error...")