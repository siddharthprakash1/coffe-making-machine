#PRINT REPORT
#CHECK RESOURCES SUFFICIENT
#PROCESS COINS
#CHECK TRANSACTION SUCCESSFUL
#MAKE COFFEE
from menu import *
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu = Menu()

is_on=True

while is_on:
    a=menu.get_items()
    n=input("enter the coffee you like "+a+ " :")
    if n=="off":
        is_on=False
    elif n=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(n)
        if coffee_maker.is_resource_sufficient(drink):
            if print(money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)
