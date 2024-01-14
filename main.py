import random

def password_generator():
    characters  = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,p,w,x,y,z0123456789"

    # save it to a string
    length = int(input("Password length: "))
    # ask the user to input the length of desired password

    #use random module to generate gibberish password of
    #given length
    password =""
    for i in range (length):
        password += random.choice(characters)
    #print out the password
    print(f"Your password is : {password}")
password_generator() 
