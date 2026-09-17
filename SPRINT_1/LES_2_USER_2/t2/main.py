battery_percentage = input("Battery percentage: ")
cost_per_minute = input("Battery cost per minute: ")

# flight_time = battery_percentage / cost_per_minute
# TypeError: unsupported operand type(s) for /: 'str' and 'str'

battery_percentage = int(battery_percentage)
cost_per_minute = float(cost_per_minute)

print(type(battery_percentage))
print(type(cost_per_minute))

flight_time = battery_percentage / cost_per_minute

print("Flight time:", flight_time, "minutes")