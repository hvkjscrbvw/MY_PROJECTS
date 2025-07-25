import random
import time

wrong_responses = [
    "Please try again.",
    "Password is incorrect",
    "That is the wrong password",
    "I see you",
]
password = "AerVanTex@60"
i = 0
wait = 0
while True:
    attempt = input("Password: ")
    if password == attempt:
        print("Welcome")
        break
    else:
        print(random.choice(wrong_responses))
        i += 1
        if i == 5:
            wait += 10
            wait_time = str(wait)
            print("Too many tries. Try again in " + wait_time + " seconds.")
            time.sleep(wait)
            i = 0
