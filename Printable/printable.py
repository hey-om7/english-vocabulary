file1 = open("../Vocabulary.txt", "r")
l1 = file1.read()
l2 = [str(index+1)+".) "+i.strip().replace("\n", "")
      for index, i in enumerate(l1.split("--"))]


def format_print(x):
    try:
        _temp = x.split(":")[0]+":  "+x.split(":")[1]
        _temp2 = _temp.split(">")[0]+"\neg: "+_temp.split(">")[1]
        _temp2 += "\n--------------------\n"
        return _temp2
    except:
        print("Error at", x)


l3 = list(map(lambda x: format_print(x), l2))


# print(*l3)
f = open("PrintReadyFile.txt", "w")
f.write("".join(l3))
f.close()
print("Ended successfully with last statement\n\n", l3[-1])
