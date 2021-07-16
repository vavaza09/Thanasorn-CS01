A = int(input("keep score:"))
B = int(input('score midexam:'))
C = int(input('score finalexam:'))
D = A + B + C
if(80<=D<=100):
    print('Grad A')
elif(75<=D<=79):
    print('Grad B+')
elif(70<=D<=74):
    print('Grad B')
elif(65<=D<=69):
    print('Grad C+')
elif(60<=D<=64):
    print('Grad C')
elif(55<=D<=59):
    print('Grad D+')
elif(50<=D<=54):
    print('Grad D')
elif(0<=D<=49):
    print('Grad F')






