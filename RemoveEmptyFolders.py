import os

print("!Warning this script delete all empty folders in the directory it was executed in [v0.9️]¡")
print("1 Start")
print("0 Close")
x = input("")

if x == "1":
    while True:
        for item in os.listdir(os.getcwd()):
            if os.path.isdir(item):
                if not os.listdir(item):
                    os.removedirs(os.path.join(os.getcwd(), item))

        break
else:
    pass
