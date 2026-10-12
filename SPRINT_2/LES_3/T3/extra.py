from djitellopy import Tello

tello = Tello()
tello.connect()

battery = tello.get_battery()               # percentage
temp    = tello.get_highest_temperature()   # graden Celsius
height  = tello.get_height()                # centimeters

MIN_BATTERY = 20
MAX_TEMP = 80
MAX_HEIGHT = 0

if battery < MIN_BATTERY:
    print(f"Batterij te laag: {battery}% (minimum: {MIN_BATTERY}%)")
    tello.end()
    exit()

if temp >= MAX_TEMP:
    print(f"Drone te warm: {temp}°C (maximum: {MAX_TEMP}°C)")
    tello.end()
    exit()

if height != MAX_HEIGHT:
    print(f"Drone staat niet op de grond: {height} cm (moet: {MAX_HEIGHT} cm zijn)")
    tello.end()
    exit()

print(
    f"Status: Batterij: {battery:.1f}% | "
    f"Temp: {temp:.1f}°C | "
    f"Hoogte: {height:.1f} cm"
)

tello.takeoff()