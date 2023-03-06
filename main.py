from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#menu list items object
list= Menu()

#Profit as of starting
profit = 0

#my coffee machine and my money processor object
my_maker = CoffeeMaker()
my_profit = MoneyMachine()

#While the coffee machine is on we perform.
is_on = True
while is_on:
  
  #Ask user input
  choice = input("what coffee would you like espresso/latte/cappucino? ")
  
  #Now if the user choice is off, then we need to turn off the machine
  if choice == "off":
    is_on = False
    print("the coffee machine is off come back later!")
    # if the user wants the report, then we have to get it.
    
  elif choice =="report":
    #Let's generate the report from the class coffeeMaker and object report
    report = my_maker.report()
    report = my_profit.report()
    print(report)

    #IF NOT the report then we look for the coffee type

  elif choice != "report" and choice !="off":
    #fetching the menu item
    #we also tell how much it is going to cost
    drink = list.find_drink(choice)
    coffe_name= drink.name
    coffee_ingredients = drink.ingredients
    coffee_cost = drink.cost 
    print(f" Your {coffe_name} is going to be ${coffee_cost}")
    
    #collect money and calculate the change for the user  
    cost_of_drink= my_profit.make_payment(coffee_cost)

    #Deducting the ingredients from the coffee made in the machine
    my_maker.make_coffee(drink)

