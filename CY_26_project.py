#Session 26 project
'''
Authentication System Project : 

The project can be done in the following ways:
Recommended: The user can be asked to register into the system,
and then using the credentials given while registering,
the user can be authenticated.
Hints :Modules, Lists/Dictionary,Functions. 
The user can be given predefined credentials,
and can be asked to login to access the system. Hints: if-else block
The user can be given predefined credentials and on first login,
the user can change the password.Hints: if-else block, lists/tuples.
Note:

1) The system after login has to do some action/function. 
2) In order to make the system foolproof just like an industry level system,
   a lot of validation techniques can be used like the number characters in the password, use of special characters etc.
'''
print("Welcome to Python Authentication System")

ask=int(input("Enter 1 to make new account and enter any other number to get predefined credentials for registration: \n"))
def login():
    print("A proper name should not contain a digit or character")
    name=input("Enter your name:\n")
    print("A proper ends with @yahoo.com or @gmail.com irrespective of the case of letters")
    email=input("Enter your email:\n").lower()
    print("An ideal contact must contain digits only with length of 10.")
    contact=int(input("Enter your contact:\n"))
    print("A strong password should atleast have 8 digits, must contain atleast 1 uppercase, 1 lowercase and a special digit")
    password=input("Create a new password:\n")
    return [name,email,contact,password]

def predefined():
    name="newuser"
    email="newuser.system@gmail.com"
    contact=1234567890
    password="new@123User"
    return [name,email,contact,password]

def show():
    print("Name:",details[0],"\nEmail:",details[1],"\nContact:",details[2],"\nPassword:",details[3])
    
def check(n,e,c,p):
    c1=True
    temp=0
    c2=False
    c3=False
    c4=False
    for i in n:
        for i in ['0','1','2','3','4','5','6','7','8','9','!','@','$','%','^','&','*','_','?']:
            temp+=1            
        if temp>0:
            c1=False
            print(n,"name is invalid")
        elif e.endswith("@gmail.com") or e.endswith("@yahoo.com"):
            c2=True
        else:
            print(e,"email is invalid")
    if len(str(c))==10:
        c3=True
    else:
        print(c,"the contact is invalid")
    x1=0
    x2=0
    x3=0
    x4=0
    for x in p:
        if x in ['0','1','2','3','4','5','6','7','8','9']:
            x1+=1
        elif x in ['@','#','\\','_','-','!','&']:
            x2+=1
        elif x in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z','q']:
            x3+=1
        elif x in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            x4+=1
    if x1>0 and x2>0 and x3>0 and x4>0 and len(p)>=8:
        c4=True
    else:
        print(p,"password is invalid")
    if c1 and c2 and c3 and c4:
        return True
    else:
        return False
        
if ask==1:
    details=login()
    
    t=check(details[0],details[1],details[2],details[3])
    if t:
        print("You have succesfully registered !")
    else:
        print("Registration Failed. Please try again")
    show()
else:
    details=predefined()
    show()
passChange=input("Do you want to change password?(yes/no)")
if passChange=="yes":
    login()

print("Thanks for using our platform to register")



    










    
