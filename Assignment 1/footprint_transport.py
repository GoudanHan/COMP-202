# COMP 202 A1: Part 3
# Footprint of local transportation and travel
# Author: Tianyu Han

import doctest
from unit_conversion import *

INCOMPLETE = -1


################################################


# calculoate foot print from driving
def fp_from_driving(annual_km_driven):
    '''
    (num) -> flt
    Approximate CO2E footprint for one year of driving, based on total km driven.
    Result in metric tonnes.
    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
    "D.) Multiply total yearly mileage by .79 (for pounds)"

    >>> fp_from_driving(0)
    0.0
    >>> round(fp_from_driving(100), 4)
    0.0223
    >>> round(fp_from_driving(1234), 4)
    0.2748
    '''
    driving = kg_to_tonnes(pound_to_kg(km_to_miles(annual_km_driven)*0.79))
    return driving


# calculoate foot print from uber rides
def fp_from_taxi_uber(weekly_uber_rides):
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the annual footprint from a given
    number of weekly uber/taxi/etc rides.

    Source: https://www.mapc.org/resource-library/the-growing-carbon-footprint-of-ride-hailing-in-massachusetts/
        81 million trips -> 100,000 metric tonnes

    >>> fp_from_taxi_uber(0)
    0.0
    >>> round(fp_from_taxi_uber(10), 4)
    0.6442
    >>> round(fp_from_taxi_uber(25), 4)
    1.6104
    '''
    uber = weekly_to_annual(weekly_uber_rides)/(81000000/100000)
    return uber


# calculoate foot print from weekly bus and rail trips
def fp_from_transit(weekly_bus_trips, weekly_rail_trips):
    '''
    (num, num) -> flt
    Annual CO2E tonnes from public transit based on number of weekly bus
    rides and weekly rail (metro/commuter train) rides.

    Source: https://en.wikipedia.org/wiki/Transportation_in_Montreal
    The average amount of time people spend commuting with public transit in Montreal, for example to and from work, on a weekday is 87 min. 29.% of public transit riders, ride for more than 2 hours every day. The average amount of time people wait at a stop or station for public transit is 14 min, while 17% of riders wait for over 20 minutes on average every day. The average distance people usually ride in a single trip with public transit is 7.7 km, while 17% travel for over 12 km in a single direction.[28]
    Source: https://en.wikipedia.org/wiki/Société_de_transport_de_Montréal
    As of 2011, the average daily ridership is 2,524,500 passengers: 1,403,700 by bus, 1,111,700 by rapid transit and 9,200 by paratransit service.

    Source: How Bad Are Bananas
        A mile by bus: 150g CO2E
        A mile by subway train: 160g CO2E for London Underground

    >>> fp_from_transit(0, 0)
    0.0
    >>> round(fp_from_transit(1, 0), 4)
    0.0374
    >>> round(fp_from_transit(0, 1), 4)
    0.0399
    >>> round(fp_from_transit(10, 2), 4)
    0.4544
    '''
    transit = kg_to_tonnes(km_to_miles((weekly_to_annual(weekly_bus_trips*7.7)))*150/1000) \
              + kg_to_tonnes(km_to_miles((weekly_to_annual(weekly_rail_trips*7.7)))*160/1000)
    return transit


# calculoate the total foot print from transportation
def fp_of_transportation(weekly_bus_rides, weekly_rail_rides, weekly_uber_rides, weekly_km_driven):
    '''(num, num, num, num) -> flt
    Estimate in tonnes of CO2E the footprint of weekly transportation given
    specified annual footprint in tonnes of CO2E from diet.

    >>> fp_of_transportation(0, 0, 0, 0)
    0.0
    >>> round(fp_of_transportation(2, 2, 1, 10), 4)
    0.3354
    >>> round(fp_of_transportation(1, 2, 3, 4), 4)
    0.3571
    >>> round(fp_of_transportation(0, 0, 0, 100), 4)
    1.1618
    '''
    transportation = fp_from_transit(weekly_bus_rides, weekly_rail_rides) + fp_from_taxi_uber(weekly_uber_rides) \
                     + fp_from_driving(weekly_to_annual(weekly_km_driven))
    return transportation


#################################################

# You might want to put helper functions here :)

# calculoate foot print from annual long and short flights
def fp_from_flights(annual_long_flights, annual_short_flights):
    """(num, num) -> float
    This functions returns the annual metric tonnes of CO2E produced by flights.
    >>> round(fp_from_flights(1, 0), 4)
    1.9958
    >>> round(fp_from_flights(1, 1), 4)
    2.4948
    """
    flights = kg_to_tonnes(pound_to_kg(annual_long_flights * 4400)) + \
              kg_to_tonnes(pound_to_kg(annual_short_flights * 1100))
    return flights


# calculoate foot print from annual train and coach bus rides
def fp_from_train_and_coach(annual_train, annual_coach):
    """(num, num) -> float
    This functions returns the annual metric tonnes of CO2E produced by train and coach bus rides.
    >>> round(fp_from_train_and_coach(1, 0), 4)
    0.0345
    >>> round(fp_from_train_and_coach(0, 1), 4)
    0.033
    """
    train_and_coach = kg_to_tonnes(annual_train * 34.45 + annual_coach * 33)
    return train_and_coach


# calculoate foot print from hotels
def fp_from_hotel(annual_hotels):
    """(num) -> float
    This functions returns the annual metric tonnes of CO2E produced by hotels.
    >>> round(fp_from_hotel(100), 4)
    0.027
    >>> fp_from_hotel(0)
    0.0
    """
    hotel = kg_to_tonnes(annual_hotels * 270 / 1000)
    return hotel

#################################################


# calculoate the total foot print from travel
def fp_of_travel(annual_long_flights, annual_short_flights, annual_train, annual_coach, annual_hotels):
    '''(num, num, num, num, num) -> float
    Approximate CO2E footprint in metric tonnes for annual travel, based on number of long flights (>4 h), short flights (<4), intercity train rides, intercity coach bus rides, and spending at hotels.

    Source for flights: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852 --- in lbs
    "E.) Multiply the number of flights--4 hours or less--by 1,100 lbs
    F.) Multiply the number of flights--4 hours or more--by 4,400 libs"

    Source for trains: https://media.viarail.ca/sites/default/files/publications/SustainableMobilityReport2016_EN_FINAL.pdf
    137,007 tCO2E from all of Via Rail, 3974000 riders
        -> 34.45 kg CO2E

    Source for buses: How Bad Are Bananas
        66kg CO2E for ROUND TRIP coach bus ride from NYC to Niagara Falls
        I'm going to just assume that's an average length trip, because better data not readily avialible.

    Source for hotels: How Bad Are Bananas
        270 g CO2E for every dollar spent

    >>> fp_of_travel(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_travel(0, 1, 0, 0, 0), 4) # short flight
    0.499
    >>> round(fp_of_travel(1, 0, 0, 0, 0), 4) # long flight
    1.9958
    >>> round(fp_of_travel(2, 2, 0, 0, 0), 4) # some flights
    4.9895
    >>> round(fp_of_travel(0, 0, 1, 0, 0), 4) # train
    0.0345
    >>> round(fp_of_travel(0, 0, 0, 1, 0), 4) # bus
    0.033
    >>> round(fp_of_travel(0, 0, 0, 0, 100), 4) # hotel
    0.027
    >>> round(fp_of_travel(6, 4, 24, 2, 2000), 4) # together
    15.4034
    >>> round(fp_of_travel(1, 2, 3, 4, 5), 4) # together
    3.2304
    '''
    travel = fp_from_flights(annual_long_flights, annual_short_flights) \
             + fp_from_train_and_coach(annual_train, annual_coach) + fp_from_hotel(annual_hotels)
    return travel

#################################################

if __name__ == '__main__':
    doctest.testmod()
