a = int(input("enter you age: "))

# if statement no: 1
if(a%2==0):
    print("your age is even")

#if statement no.2
if(a>=18):
    print("you are an adult now")

elif(a<0):
    print("you are entering wrong negative age")

elif(a==0):
    print("you are entering zero age")

else:
    print("you are not an adult")

print("end of the program")