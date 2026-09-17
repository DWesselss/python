from djitellopy import Tello

tello = Tello()
tello.connect()

battery = tello.get_battery()
height = tello.get_height()
temperature = tello.get_temperature()

print(f"Type batterij: {type(battery)}")
print(f"Batterij: {battery}%")

print(f"Type hoogte: {type(height)}")
print(f"Hoogte: {height} cm")

print(f"Type temperatuur: {type(temperature)}")
print(f"Temperatuur: {temperature}°C")