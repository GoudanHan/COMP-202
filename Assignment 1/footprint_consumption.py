# COMP 202 A1: Part 4
# Footprint of computing and diet
# Author: Tianyu Han

import doctest
from unit_conversion import *


INCOMPLETE = -1

######################################

# calculoate foot print from daily online use
def fp_from_online(daily_online_use):
    """(num) -> float
    This function returns annual metric tonnes of CO2E generated from online time.
    >>> round(fp_from_online(0), 4)
    0.0
    >>> round(fp_from_online(2), 4)
    0.0402
    """
    online = kg_to_tonnes(daily_to_annual(daily_online_use)*55/1000)
    return online


# calculoate foot print from daily phone use
def fp_from_phone(daily_phone_use):
    """(num) -> float
    This function returns annual metric tonnes of CO2E generated from phone use.
    >>> round(fp_from_phone(1), 4)
    1.25
    >>> round(fp_from_phone(2), 4)
    2.5
    """
    phone = kg_to_tonnes(daily_phone_use*1250)
    return phone


# calculoate foot print from annual new devices
def fp_from_device(new_light_devices, new_medium_devices, new_heavy_devices):
    """(num,num,num) -> float
    This function returns annual metric tonnes of CO2E generated from new devices.
    >>> round(fp_from_device(1,2,3), 4)
    2.875
    >>> round(fp_from_device(0,0,0), 4)
    0.0
    """
    device = kg_to_tonnes((new_light_devices) * 75 + \
             (new_medium_devices) * 200 + (new_heavy_devices) * 800)
    return device


# calculoate the total foot print from computing
def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> round(fp_of_computing(0, 0, 1, 0, 0), 4)
    0.075
    >>> round(fp_of_computing(0, 0, 0, 1, 0), 4)
    0.2
    >>> round(fp_of_computing(0, 0, 0, 0, 1), 4)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    computing = fp_from_online(daily_online_use) + fp_from_phone(daily_phone_use) \
                + fp_from_device(new_light_devices, new_medium_devices, new_heavy_devices)
    return computing


######################################


# calculoate foot print from daily meat
def fp_from_meat(daily_g_meat):
    """(num) -> float
    This function returns annual metric tonnes of CO2E generated from meats.
    >>> round(fp_from_meat(0), 4)
    0.0
    >>> round(fp_from_meat(1000), 4)
    9.7885
    """
    meat = kg_to_tonnes(daily_to_annual(daily_g_meat*26.8)/1000)
    return meat


# calculoate foot print from daily cheese
def fp_from_cheese(daily_g_cheese):
    """(num) -> float
    This function returns annual metric tonnes of CO2E generated from cheese.
    >>> round(fp_from_cheese(0), 4)
    0.0
    >>> round(fp_from_cheese(100), 4)
    0.4383
    """
    cheese = kg_to_tonnes(daily_to_annual(daily_g_cheese*12)/1000)
    return cheese


# calculoate foot print from daily milk
def fp_from_milk(daily_L_milk):
    """(num) -> float
    This function returns annual metric tonnes of CO2E generated from milk.
    >>> round(fp_from_milk(0), 4)
    0.0
    >>> round(fp_from_milk(1), 4)
    0.0978
    """
    milk = kg_to_tonnes(daily_to_annual(daily_L_milk*267.7777)/1000)
    return milk


# calculoate foot print from daily eggs
def fp_from_eggs(daily_num_eggs):
    """float -> float
    This function returns annual metric tonnes of CO2E generated from eggs.
    >>> round(fp_from_eggs(0), 4)
    0.0
    >>> round(fp_from_eggs(1), 4)
    0.1096
    """
    eggs = kg_to_tonnes(daily_to_annual(daily_num_eggs*300)/1000)
    return eggs


# calculoate the total foot print from diet
def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''
    diet = 1.0556 + fp_from_meat(daily_g_meat) + fp_from_cheese(daily_g_cheese) \
           + fp_from_milk(daily_L_milk) + fp_from_eggs(daily_num_eggs)
    return diet
    


#################################################

if __name__ == '__main__':
    doctest.testmod()

