from djitellopy import Tello

# Constanten
DISTANCE = 100
MIN_BATTERY = 35
MAX_FLIGHT_TIME = 90
MIN_HEIGHT = 30
MAX_HEIGHT = 200

# Eerste etappe
tello = Tello()
tello.connect()

start_battery = tello.get_battery()

tello.takeoff()
tello.move_forward(DISTANCE)

# Metingen
battery = tello.get_battery()
flight_time = tello.get_flight_time()
height = tello.get_height()

# Guards
if battery < MIN_BATTERY:
    print(f"Batterij: {battery}%, minimaal {MIN_BATTERY}% nodig")
    tello.land()
    tello.end()
    exit()

if flight_time > MAX_FLIGHT_TIME:
    print(f"Vliegtijd: {flight_time} sec, maximaal {MAX_FLIGHT_TIME} sec")
    tello.land()
    tello.end()
    exit()

if not MIN_HEIGHT <= height <= MAX_HEIGHT:
    print(f"Hoogte: {height} cm, moet tussen {MIN_HEIGHT} en {MAX_HEIGHT} cm zijn")
    tello.land()
    tello.end()
    exit()

# Happy path
tello.move_back(DISTANCE)
tello.land()

end_battery = tello.get_battery()
tello.end()

used = start_battery - end_battery
percentage = (used / start_battery) * 100

print("Vlucht voltooid!")
print(f"Startbatterij: {start_battery}%")
print(f"Eindbatterij: {end_battery}%")
print(f"Verbruik: {used} procentpunten")
print(f"Verbruik t.o.v. start: {percentage:.1f}%")