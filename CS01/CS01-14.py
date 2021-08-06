thislist = [5,10,15,20,25,50,20]
for i in range(len(thislist)):
    if (thislist[i] == 25):
        thislist[i] = 20
    elif (thislist[i] == 20):
        thislist[i] = 200
print(thislist)