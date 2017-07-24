def open_tank():
    """ None -> [[str, str, float, float]] item[0]=str(item[0])
    """
    with open('tank.txt', 'r') as file:
        file.readline()
        string_inventory = file.readlines()
    inventory = []
    for item in string_inventory:
        sub_list = item.split(', ')
        gallons = float(sub_list[2].strip())
        if gallons > 0:
            # [str, str, str, str] -> [str, str, float, float]
            inventory.append([sub_list[0], sub_list[1], float(sub_list[2].strip()), float(sub_list[3].strip())])
    # return inventory (list)
    return inventory

def make_message(inventory):
    """ [[str, str, float, float]] -> str """
    msg = 'Welcome to Shuffles Stop! What type of gas would you like?\n'
    for item in inventory:
        msg += '\t{}. {} ${:.2f}\n'.format(item[1], item[0], item[3])
    return msg

def get_codes(inventory):
    """ [[str, str, float, float]] -> [str] """
    codes = []
    for item in inventory:
        codes.append(item[1])
    return codes

def gas_price(inventory, gas, amount):
    ''' (List[Item], string, float) -> float
    >>> gas_price([['regular', 100, 2.0], ['mid', 150, 2.15]], 'regular', 5)
    10.0
        
    '''
    for item in inventory:
        if item[1] == gas:
            return float(item[3]) * amount

def update_log(inventory, gas, gallons, price):
    """ [[str, str, float, float]], str, float, float -> None"""
    for item in inventory:
        if item[1] == gas:
            gas_name = item[0]
    
    message = '\n{}, {}, {}'.format(gas_name, gallons, price)
    with open('log.txt', 'a') as file:
        file.write(message)
    return None

def update_tank(inventory, gas_name, amount_purchased):
    """([[str, float, float]], str, float) -> None
    taking in the gas type, gallons purchased and updating
    the tank txt file with new amount in tank"""
    # make list into a string
    # ['regular, mid-grade, premium']
    # overwrite tank text file with string 



def list_of_log():
    left = []
    with open('log.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2].strip().replace('$', ''))])
    return left

def revenue_in_log(log):
   left = list_of_log()
   price = 0
   for item in left:
       item[2] = float(item[2]) + float(item[2])
       price += item[2]
   return price 

def in_the_tank():
    left = []
    with open('tank.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[2]), float(split_string[3])])
    return left

def take_away(inventory, gas_type, amount):
    str_l = ['type, gas_code, amount_in_tank, price']
    for item in inventory:
        if item[0] == gas_type:
            if float(amount) > item[1]:
                print('Sorry, we have sold out of this type of gas.')
                return False
            else:
                item[2] = float(item[2]) - float(amount)
        item[1] = str(item[1])
        item[2] = str(item[2])
        item[3] = str(item[3])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)

    with open('tank.txt', 'w') as file:
        file.write(message)
    return True 

def refill():
    str_l = ['type, amount_in_tank, price']
    left = in_the_tank()
    for item in left:
        if item[1] < 5000.0:
            item[1] = 5000.0
        item[1]=str(item[1])
        item[2]=str(item[2])
        str_l.append(', '.join(item))
        message = '\n'.join(str_l)

    with open('tank.txt', 'w') as file:
        file.write(message) 

