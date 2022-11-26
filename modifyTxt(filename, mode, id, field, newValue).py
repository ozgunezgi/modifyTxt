def modifyTxt(filename, mode, id, field = "field", newValue = "newValue"):
    lst = []
    with open(filename, "r+") as f:
        for i in f.readlines():
            lst.append(i.split())
        for j in lst:
            if id == int(j[0]):
                if mode == "delete":
                    lst.pop(lst.index(j))
                elif mode == "update":
                    if field == "name":
                        lst[lst.index(j)][1] = str(newValue)
                    elif field == "surname":
                        lst[lst.index(j)][2] = str(newValue)
                    elif field == "job":
                        lst[lst.index(j)][3] = str(newValue)
                    elif field == "age":
                        lst[lst.index(j)][4] = str(newValue)
        finalstr = ""
        for k in lst:
            for m in k:
                finalstr = finalstr + m + " "
            finalstr = finalstr + "\n"
        f.seek(0)
        f.write(finalstr)
        f.truncate()