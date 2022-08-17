import os
import shutil

print("!Warning this script delete all empty folders in the directory it was executed in [v0.9️]¡")
print("1 Start")
print("0 Close")
x = input("")

if x == "1":
    index_list = {"documents", "photos", "videos", "music", "compressed", "software", "programming", "others"}

    documents = [".afpub", ".pdf", ".doc", ".docx", ".txt", ".odt", ".odp", ".odg", ".ods", ".xlsx", ".ppt", ".pptx"]

    photos = [".jpg", ".png", ".gif", ".webp", ".pdf", ".afdesign", ".afphoto", ".sai2", ".sai", ".bmp", ".tiff"]

    videos = [".mp4", ".mkv", ".avi", ".mov", ".flv", ".divx", ".webm", ".swf"]

    music = [".mp3", ".aac", ".wav", ".aiff", ".wma", ".opus", ".ogg"]

    compressed = [".rar", ".7z", ".zip", ".msi", ".bz2", ".gz", ".tar", ".wim", ".xz"]

    software = [".deb", ".exe"]

    programming = [".go", ".py", ".html", ".css", ".php", ".js", ".rs", ".md", ".json", ".gitattributes"]

    others = [".tmp", ".dat", ".dmg"]

    while True:
        for x in index_list:
            if os.path.exists(f"{x}"):
                pass
            else:
                os.mkdir(f"{x}")
        break

    while True:
        for x in documents:
            extension_name = x
            container = [_ for _ in os.listdir() if _.endswith(extension_name)]
            for i in container:
                shutil.move(i, "documents")
        break

    while True:
        for x in photos:
            extension_name = x
            container = [_ for _ in os.listdir() if _.endswith(extension_name)]
            for i in container:
                shutil.move(i, "photos")
        break

    while True:
        for x in videos:
            extension_name = x
            container = [_ for _ in os.listdir() if _.endswith(extension_name)]
            for i in container:
                shutil.move(i, "videos")
        break

    while True:
        for x in music:
            extension_name = x
            container = [_ for _ in os.listdir() if _.endswith(extension_name)]
            for i in container:
                shutil.move(i, "music")
        break

    while True:
        for x in compressed:
            extension_name = x
            container = [_ for _ in os.listdir() if _.endswith(extension_name)]
            for i in container:
                shutil.move(i, "compressed")
        break

    while True:
        for x in software:
            extension_name = x
            container = [_ for _ in os.listdir() if _.endswith(extension_name)]
            for i in container:
                shutil.move(i, "software")
        break

    while True:
        for x in programming:
            extension_name = x
            container = [_ for _ in os.listdir() if _.endswith(extension_name)]
            for i in container:
                shutil.move(i, "programming")
        break

    while True:
        for x in others:
            extension_name = x
            container = [_ for _ in os.listdir() if _.endswith(extension_name)]
            for i in container:
                shutil.move(i, "others")
        break

    while True:

        for item in os.listdir(os.getcwd()):
            if os.path.isdir(item):
                if not os.listdir(item):
                    os.removedirs(os.path.join(os.getcwd(), item))

        break

    for item in os.listdir(os.getcwd()):
        if os.path.isdir(item):
            if not os.listdir(item):
                os.removedirs(os.path.join(os.getcwd(), item))

else:
    pass
