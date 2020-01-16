from building import Building
from city import City

Samtopia = City("Samtopia", "Sam Pita", 2020)

Town_Hall = Building("1 Main St", 5)
Market = Building("24 Market Sq", 1)
Bank = Building("37 Washington Ln", 2)

Samtopia.add_building(Town_Hall)
Samtopia.add_building(Market)
Samtopia.add_building(Bank)

for building in Samtopia.buildings:
    print(f'This building is designed by {building.designer} at {building.address} and it is {building.stories} stories.')

