import random
weapons = ["bat", "gun", "pipe", "pan"]
rand_weap = random.choice(weapons)
invent = []

name = input("Whats your name? ")
print("Hello there " + name + " how are you today?")

print(rand_weap)
if rand_weap == "pan":
    print("Good luck fighting a zombie horde with a", rand_weap)
    invent.append(rand_weap)
    print(invent)
elif 