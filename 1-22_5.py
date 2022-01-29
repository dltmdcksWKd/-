a=0
while a < 100 :
    a +=1
    if((a%10)==3 or (a%10)==6 or (a%10)==9):
        if((a//10)==3 or (a//10)==6 or (a//10)==9):
            print("**")
        else:
            print("*")
    elif((a//10)==3 or (a//10)==6 or (a//10)==9):
        print('*')
    else:
        print(a)