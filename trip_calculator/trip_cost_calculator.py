'''
Trip Cost Calculator

Create a python script that asks a user questions in the command line. The script should follow the outlined specs.

Specs

Receive the following arguments from the user:

- kilometers to drive
- liters-per-kilometer usage of the car
- price per liter of fuel

Calculate the cost of the trip and display it to the user in the console.
'''
# Get inputs
km = float(input("How far will you drive (in km)? "))
usage = float(input("How many liters of fuel does your car use per kilometer? "))
price = float(input("What is the current price per liter of fuel? "))
# Print cost of trip
print("Your trip will cost", "%.2f" % (km * usage * price))
