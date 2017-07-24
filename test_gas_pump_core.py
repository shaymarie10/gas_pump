import gas_pump_core

def test_make_message():
    inventory = [['Regular', '1', 5000, 2.10]]
    expected = '''Welcome to Shuffles Stop! What type of gas would you like?
\t1. Regular $2.07
\t2. Mid-Grade $2.10
\t3. Premium $2.20
\t4. Diesel $3.10
'''
    assert gas_pump_core.make_message(inventory) == expected
