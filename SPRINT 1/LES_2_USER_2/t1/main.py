drone_name = "Tello"
battery_percentage = 80
height = 1.5
is_flying = False

# None omdat er geen fout is. 0 zou een echte foutcode zijn.
last_error = None

print(drone_name.upper(), type(drone_name))
print(battery_percentage, type(battery_percentage))
print(height, type(height))
print(is_flying, type(is_flying))
print(last_error, type(last_error))