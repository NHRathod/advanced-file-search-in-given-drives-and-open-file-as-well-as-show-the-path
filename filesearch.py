import os
import webbrowser

startdir=["D:\\","C:\\"]
ret=""
searchlist=[]
while True:
    userinput = input("Enter search keys:")
    if userinput.lower() == "stop":
        break
    searchlist.append(userinput)
def match(left, right):
    bol = 0
    for item in left:
        if item.lower() not in right.lower():
            break
        else:
            bol=bol+1
    if bol == len(left):
        return True
    else:
        return False


def searchstart(startdir):
    for file in os.listdir(startdir):
        try:
            if os.path.isdir(os.path.join(startdir,file)):
                searchstart(os.path.join(startdir,file))
            else:
                matching = match(searchlist,file)
                if matching == True:
                    global ret
                    ret=os.path.join(startdir,file)
                    break
        except Exception:
            pass
        if ret != "":
            break

print("Searching")
for dir in startdir:
    searchstart(dir)
if ret == "":
    print("File not found")
else:
    print("File path is:")
    print(ret)
    webbrowser.open(ret)
