import numpy as np 
Mt1 = []
Mt2 = []
loop = 1
Mtcolumns = int(input("EnterYourColumns : "))
Mtrows = int(input("EnterYourRows : "))
while( loop <= 2):
    print("EnterYourMatrix",loop)
    for i in range(Mtrows) :
        for j in range(Mtcolumns) :
            print("MatrixColumns [",i,",",j,"] :" ,end="")
            if(loop == 1):
                Mt1input = int(input(""))
                Mt1.append(Mt1input)
            else:
                Mt2input = int(input(""))
                Mt2.append(Mt2input)
    loop += 1
Mt1py = np.asarray(Mt1)
Mt2py = np.asarray(Mt2)
Newmt1 = Mt1py.reshape(Mtrows,Mtcolumns)
Newmt2 = Mt2py.reshape(Mtrows,Mtcolumns)
print(Newmt1,"\n======================")
print(Newmt2,"\n======================")
sum = np.add(Newmt1, Newmt2)
print(sum)