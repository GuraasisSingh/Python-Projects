'''
Restaurant
Build a python application to see restaurants near me. Given a location by the user, the application shall show restaurants rating wise from highest to lowest.
Couple of reviews about the restaurant, the best mode of travel and timings shall also be displayed. Contact details of the restaurants like phone number,
email ID should also be mentioned
'''
loc=input('Enter your location:(Chandigarh,Mumbai,Delhi,Amritsar)\n')
def dishes():
    print(" The best dishes in this restaurent are:\n Hakka Noodles\n Double Chees Pizza\n Veg Wraps \n Exotic Salad")
    d=int(input(" Enter 1 for Hakka Noodles\n Enter 2 for Double Cheese Pizza\n Enter 3 for Veg Wraps \n Enter 4 for Exotic Salad\n"))
    if d==1:
        print("Your bill is Rs.299")
    elif d==2:
        print("Your bill is Rs.599")
    elif d==3:
        print("Your bill is Rs.199")
    elif d==4:
        print("Your bill is Rs.325")
    else:
        print("This dish is currently unavailable")
def restaurant(loc):
    print("The restaurants near you in",loc,"are Aman Kitchen ,Punjabi Taste ,Burger King and  Subway")
    ch=int(input("Enter 1 for Aman Kitchen ,2 for Pizza Hut,3 for Burger King,4 for Subway Restaurants\n"))
    if ch==1:
        print("The reviews of this restaurant are awesome. Brilliant Choice!")
        print("You can easily travel there by walking")
        print("The timings are available from 10 am to 7 pm ")
        print("The contact of restaurant is 9724746290")
        print("The email of resturant is support@113@gmail.com")
        dishes()
    elif ch==2:
        print("The reviews of this restaurant are are good. People love the food but its a little expensive. Nice Choice!")
        print("You can easily travel there by a bus")
        print("The timings are available from 10 am to 7 pm")
        print("The contact of restaurant is 9724746290")
        print("The email of resturant is support@113@gmail.com")
        dishes()
    elif ch==3:
        print("The reviews of this restaurant are are moderate. People like the food but its expensive. Good Choice!")
        print("You can easily travel there by a two wheeler")
        print("The timings are available from 10 am to 7 pm")
        print("The contact of restaurant is 9724746290")
        print("The email of resturant is support@113@gmail.com")
        dishes()
    elif ch==4:
        print("The reviews of this restaurant are are fine. People complain about the variety of items in the menu and its a little expensive. Fine Choice!")
        print("You can easily travel there by a cab in 30 minutes")
        print("The timings are available from 10 am to 7 pm")
        print("The contact of restaurant is 9724746290")
        print("The email of resturant is support@113@gmail.com")
        dishes()
    else:
        print("Invalid choice")
        

if loc=='Delhi':
    restaurant(loc)
elif loc=='Chandigarh':
    restaurant(loc)
elif loc=='Mumbai':
    restaurant(loc)
elif loc=='Amritsar':
    restaurant(loc)
else:
    print("Invalid location")
print("Thank you for using our platform for ordering.")
