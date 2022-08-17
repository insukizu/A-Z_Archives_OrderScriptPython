import os
import shutil

print("!Warning this script delete all empty folders in the directory it was executed in [v0.9️]¡")
print("1 Start")
print("0 Close")
x = input("")
if x == "1":
    index_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                  "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

    while True:
        for x in index_list:
            if os.path.exists(f"{x}"):
                pass
            else:
                os.mkdir(f"{x}")
            print(f"{x}")
        break

    while True:
        for x in index_list:
            home_letter = x
            container = [_ for _ in os.listdir() if _.startswith(home_letter)]
            for i in container:
                shutil.move(i, x)
        break

    for item in os.listdir(os.getcwd()):
        if os.path.isdir(item):
            if not os.listdir(item):
                os.removedirs(os.path.join(os.getcwd(), item))
else:
    pass
