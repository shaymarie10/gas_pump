import gas_pump_core

code = int(input('what is the code?'))
if code == 1212:
    input('Would you like to know the revenue of Shuffles Stop?')
    log = gas_pump_core.list_of_log()
    revenue = gas_pump_core.revenue_in_log(log)
    print(revenue)
else:
    print('access denied')

