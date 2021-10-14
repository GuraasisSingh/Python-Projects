#Build a Bus/Air/Rail Booking System where the user can choose a source and destination from the list given and enter the information passenger wise,
#depending on the distance cost shall be computed.Rail and Air systems will have different fares for different classes.
#The student should be able to think of the system as how would he/she use it as a user.
s=int(input("Choose source, 1 for Gurdaspur,2 for Delhi,3 for Mohali"))
d=int(input("Choose destination, 1 for Chandigarh,2 for Amritsar,3 for Mumbai"))
m=int(input("Choose 1 for Bus Travel, 2 for Air Travel, 3 for Rail System"))
if s and d and m in [1,2,3]:
    t=True
else :
    t=False
    print("Sorry.Incorrect Place, Destination or Mode of Transportation")
if m==1 and t==True:
    print("Welcome to Bus Booking System")
    print("Cost of per km is Rs.10")
    if s==1 and d==1:
        name=input("Enter your Name")
        contact=int(input("Enter your contact"))
        dis=50
        cost=dis*10
        print("The amount of your bus trip is",cost)        
    elif s==1 and d==2:
        dis=100
        cost=dis*10
        print("The amount of your bus trip is",cost)
        name=input("Enter your Name")
        contact=int(input("Enter your contact"))
    elif s==1 and d==3:
        dis=20
        cost=dis*10
        print("The amount of your bus trip is",cost)
        name=input("Enter your Name")
        contact=int(input("Enter your contact"))
    elif s==2 and d==1:
        dis=60
        cost=dis*10
        print("The amount of your bus trip is",cost)
        name=input("Enter your Name")
        contact=int(input("Enter your contact"))
    elif s==2 and d==2:
        dis=10
        cost=dis*10
        print("The amount of your bus trip is",cost)
        name=input("Enter your Name")
        contact=int(input("Enter your contact"))
    elif s==2 and d==3:
        dis=65
        cost=dis*10
        print("The amount of your bus trip is",cost)
    elif s==3 and d==1:
        dis=10
        cost=dis*10
        print("The amount of your bus trip is",cost)
        name=input("Enter your Name")
        contact=int(input("Enter your contact"))
    elif s==3 and d==2:
        dis=0
        cost=dis*10
        print("The amount of your bus trip is",cost)
        name=input("Enter your Name")
        contact=int(input("Enter your contact"))
    elif s==3 and d==3:
        dis=80
        cost=dis*10
        print("The amount of your bus trip is",cost)
        name=input("Enter your Name")
        contact=int(input("Enter your contact"))
        
elif m==2 and t== True:
    print("Welcome to Air Plane Booking System")
    c=int(input("Enter 1 for Business Class Compartment, 2 for common compartment"))
    if c in [1,2]:
        b=True
    else:
        b=False
    if c==1:
        print("Cost of per km is Rs.200")
        if s==1 and d==1:
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
            dis=50
            cost=dis*200
            print("The amount of your air trip is",cost)        
        elif s==1 and d==2:
            dis=100
            cost=dis*200
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==1 and d==3:
            dis=20
            cost=dis*200
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==2 and d==1:
            dis=60
            cost=dis*200
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==2 and d==2:
            dis=10
            cost=dis*200
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==2 and d==3:
            dis=65
            cost=dis*200
            print("The amount of your air trip is",cost)
        elif s==3 and d==1:
            dis=10
            cost=dis*200
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==3 and d==2:
            dis=0
            cost=dis*200
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==3 and d==3:
            dis=80
            cost=dis*200
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
    elif c==2:
        print("Cost of per km is Rs.100")
        if s==1 and d==1:
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
            dis=50
            cost=dis*100
            print("The amount of your air trip is",cost)        
        elif s==1 and d==2:
            dis=100
            cost=dis*100
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==1 and d==3:
            dis=20
            cost=dis*100
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==2 and d==1:
            dis=60
            cost=dis*100
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==2 and d==2:
            dis=10
            cost=dis*100
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==2 and d==3:
            dis=65
            cost=dis*100
            print("The amount of your air trip is",cost)
        elif s==3 and d==1:
            dis=10
            cost=dis*100
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==3 and d==2:
            dis=0
            cost=dis*100
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==3 and d==3:
            dis=80
            cost=dis*100
            print("The amount of your air trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
            
elif m==3 and t== True:
    print("Welcome to Rail Booking System")
    n=int(input("Enter 2 for Business Class Compartment, 1 for common compartment"))
    if n in [1,2]:
        b=True
    else:
        b=False
   
    if n==1:
        print("Cost of per km is Rs.50")
        if s==1 and d==1:
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
            dis=50
            cost=dis*50
            print("The amount of your rail trip is",cost)        
        elif s==1 and d==2:
            dis=100
            cost=dis*50
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==1 and d==3:
            dis=20
            cost=dis*50
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==2 and d==1:
            dis=60
            cost=dis*50
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif d==2:
            dis=10
            cost=dis*50
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif d==3:
            dis=65
            cost=dis*50
            print("The amount of your rail trip is",cost)
        elif s==3 and d==1:
            dis=10
            cost=dis*50
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==3 and d==2:
            dis=0
            cost=dis*50
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==3 and d==3:
            dis=80
            cost=dis*50
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
    if n==2:
        print("Cost of per km is Rs.70")
        if s==1 and d==1:
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
            dis=70
            cost=dis*70
            print("The amount of your rail trip is",cost)        
        elif s==1 and d==2:
            dis=100
            cost=dis*70
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==1 and d==3:
            dis=20
            cost=dis*70
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==2 and d==1:
            dis=60
            cost=dis*70
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif d==2:
            dis=10
            cost=dis*70
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif d==3:
            dis=65
            cost=dis*70
            print("The amount of your rail trip is",cost)
        elif s==3 and d==1:
            dis=10
            cost=dis*70
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==3 and d==2:
            dis=0
            cost=dis*70
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
        elif s==3 and d==3:
            dis=80
            cost=dis*70
            print("The amount of your rail trip is",cost)
            name=input("Enter your Name")
            contact=int(input("Enter your contact"))
print("Thank you for using our booking system")

    
