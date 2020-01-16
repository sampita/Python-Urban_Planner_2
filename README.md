# Python-Urban_Planner_2

## Setup

In the previous Urban Planner exercise, you practices defining custom types to represent buildings. Now you need to create a type to represent your city. Here are the requirements for the class. You define the properties and methods.

1. Name of the city.
2. The mayor of the city.
3. Year the city was established.
4. A collection of all of the buildings in the city.
5. A method to add a building to the city.

Remember, each class should be in its own file. Define the **`City`** class in the `city.py` file.

## Importing into Main
Open the `main.py` file and import the **`Building`** class from `building.py`. Once you have defined your **`City`** class, also import that into main.py. For this exercise, all the logic of constructing buildings and building your city will be in `main.py`, so take all of your logic from `building.py` and move it over to main.
- **`main.py`**
```
from building import Building
from city import City
```

## Birth of a City
Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.
- **`main.py`**
```
megalopolis = City()

# Awesome code here

for building in megalopolis.buildings:
print(building)