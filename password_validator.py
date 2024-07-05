user_password = "PercyBheki@1"

password = str(input("Enter your Password: "))
Try = 3

while password != user_password:
    Try -= 1

    if Try == 0:
        print("Account Locked")
        break
    else:
        password = str(input(f"Try again ({Try} Incorrect password): "))

if password == user_password:
    print("Welcome.....")