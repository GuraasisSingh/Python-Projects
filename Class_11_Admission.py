#Build a Student Admission System, where a Class 10th pass student enrolls for a course in Arts,Science or Commerce Stream. The student should fill in the basic,
#academic and other details and enroll for the course.
print("Welcome to Class 11 !")
st=int(input("Enter 1 for Arts ,2 for Commerce, 3 for Science: \n"))
name=input("Enter your name: \n")
contact=int(input("Enter your contact: \n"))
per=int(input("Enter your 10th class percentage to proceed: \n"))
if per >=1 and per <100:
    t=True
else:
    t=False
if t==False:
    print("Sorry.Invalid percentage")
if st==1 and t==True:
    if per>=50 and per <=60:
        print("You are Eligible to take Arts")
        sch=0
        print("Your scholarship is",sch)
        fee=100000-sch    
        print("The fees to be paid is",fee)
    elif per>60 and per <=70:
        print("You are Eligible to take Arts")
        sch=1000
        print("Your scholarship is",sch)
        fee=100000-sch    
        print("The fees to be paid is",fee)
    elif per>70 and per <=80:
        print("You are Eligible to take Arts")
        sch=5000
        print("Your scholarship is",sch)
        fee=100000-sch    
        print("The fees to be paid is",fee)
    elif per>80 and per<=90:
        print("You are Eligible to take Arts")
        sch=7500
        print("Your scholarship is",sch)
        fee=100000-sch    
        print("The fees to be paid is",fee)
    elif per>90 and per<=100:
        print("You are Eligible to take Arts")
        sch=10000
        print("Your scholarship is",sch)
        fee=100000-sch    
        print("The fees to be paid is",fee)
    else:
        print("Sorry you are not Eligible for Arts")
   
elif st==2 :
     if per>=70 and per <=80:
         print("You are eligible to take Commerce")
         sch=0
         print("Your scholarship is",sch)
         fee=150000-sch    
         print("The fees to be paid is",fee)
     elif per>80 and per<=90:
         print("You are eligible to take Commerce")
         sch=10000
         print("Your scholarship is",sch)
         fee=150000-sch    
         print("The fees to be paid is",fee)
     elif per>90 and per<=100:
         print("You are eligible to take Commerce")
         sch=20000
         print("Your scholarship is",sch)
         fee=150000-sch
         print("The fees to be paid is",fee)
     else:
         print("Sorry you are not Eligible for Commerce")
elif st==3:
    if per>=75 and per <=80:
         print("You are eligible to take Science")
         sch=0
         print("Your scholarship is",sch)
         fee=180000-sch    
         print("The fees to be paid is",fee)
    elif per>80 and per<=90:
         print("You are eligible to take Science")
         sch=10000
         print("Your scholarship is",sch)
         fee=180000-sch    
         print("The fees to be paid is",fee)
    elif per>90 and per<=100:
         print("You are eligible to take Science")
         sch=20000
         print("Your scholarship is",sch)
         fee=180000-sch
         print("The fees to be paid is",fee)
    else:
         print("Sorry you are not Eligible for Science")
    
    
    

