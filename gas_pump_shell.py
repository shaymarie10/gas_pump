import gas_pump_core

def purchase_gas(amount, gas, inventory):
    amount = float(amount)
    left = gas_pump_core.take_away(inventory, gas, amount)
    price = gas_pump_core.gas_price(inventory, gas, amount)
    print("Your total will be ${:.2f}".format(price))
    gas_pump_core.update_log(inventory, gas, amount, price)

def main():
    inventory = gas_pump_core.open_tank()
    msg = gas_pump_core.make_message(inventory)
    codes = gas_pump_core.get_codes(inventory)
    log = gas_pump_core.list_of_log()
    revenue = gas_pump_core.revenue_in_log(log)
    tank = gas_pump_core.in_the_tank()

    while True:
        gas = input(msg)
        if gas in codes:
            amount = input('How many gallons would you like to buy?\n').strip()
            if amount.isnumeric():
                purchase_gas(amount, gas, inventory)
            else:
                 print('this is not a valid response. Please use positive integers')
            break
        else:
            print('Sorry invalid response!')
        
    print('Thank you and have a good day!')  

if __name__ == '__main__':
    main()
