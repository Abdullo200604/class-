import json

from moduls import User

u = User("Abdulloh", "lwcardinal12@gmail.com", 1111)
u2 = User("azizxon", "lwcardinal12@gmail.com",1234)



path = "data.json"





menu = ("1. Kirish\n"
        "2. Ro'yhatdan O'tish\n")

while True:
    print(menu)
    choice = input()
    if choice == "1":
        with open("example.json", "w") as file:
            json.dump(u.to_dict(),u2.to_dict(), file, indent=4)
    else:
        print("Login yoki parol")
