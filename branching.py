import random
p = random.randint(1, 6)
print(p)
if p == 6:
    print("You win!!!")
elif p == 5:
    print("Try again!!!")
else:
    print("You lose!!!")

