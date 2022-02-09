'''
Build a Hotel booking system (like OYO) on the basis of the location chosen by the user. Rates and other details should be displayed along with star ratings out of 5. Each location may have 3-5 Hotels of each category 3-star,4-star and 5-star. The charges could comprise all taxes and all additional 
On Completing the Project:
The student should be able to:
Explain the project
Run the system with sample inputs
Run the system with mentor suggested inputs
Explain what extra features would the student want to add
Marks Distribution:	
Area
Marks
Code
30
Coding Etiquettes
10
Logic and Approach
30
Execution
15
Explanation
15
Total
100
'''
print("Welcome to our hotel booking system")
loc=(input("Enter location as Chandigarh, Delhi, Mumbai and Goa"))
if loc in ["Chandigarh", "Delhi", "Mumbai","Goa"]:
    print("The various hotels here at",loc," are:")
    print("Three Stars:")
    print("Crown Palace, 2499 a night\nHilton Garden, 2800 a night\n Comfort Inn, 2000 a night")
    print("Four Stars:")
    print("Holiday Inn, 3499 a night\nMandarian Garden, 6000 a night\n Peninsular Hotels, 8000 a night")
    print("Five Stars:")
    print("Hyatt, 2999 a night\nThe Breakers, 4000 a night\n Mariott International, 9000 a night")
    print("You will get Complimentary breakfast with all the hotels")
    h=int(input("Enter 1 for Crown Palace, 2 for Hilton Garden, 3 for  Comfort Inn,4 for Holiday Inn,5 for Mandarian Garden 6 for Peninsular Hotels, 7 for Hyatt, 8 for The Breakers, 9 for  Mariott International"))
    if h==1:
        p=2499
    elif h==2:
        p=2800
    elif h==3:
        p=2000
    elif h==4:
        p=3499
    elif h==5:
        p=6000
    elif h==6:
        p=8000
    elif h==7:
        p=2999
    elif h==8:
        p=4000
    elif h==9:
        p=9000
    else:
        print("Invalid Choice")
    print("Thanks for using our platform to book, the total is",p)      

else:
    print("Invalid location, Please enter a valid one.")
