from djitellopy import Tello

CLIMB = 100
MAX_HEIGHT = 200
MIN_BATTERY = 30
MAX_TEMP = 70
MAX_FLIGHT_TIME = 180
MIN_WIFI = 50

tello = Tello()
tello.connect()
tello.takeoff()

height = tello.get_height()
battery = tello.get_battery()
temperature = tello.get_temperature()
flight_time = tello.get_flight_time()
wifi = tello.query_wifi_signal_noise_ratio()

if height + CLIMB > MAX_HEIGHT:
    print(f"Hoogte: {height} cm, maximum na stijgen: {MAX_HEIGHT} cm")
    tello.land()
    tello.end()
    exit()

if battery < MIN_BATTERY:
    print(f"Batterij: {battery}%, minimaal {MIN_BATTERY}% nodig")
    tello.land()
    tello.end()
    exit()

if temperature >= MAX_TEMP:
    print(f"Temperatuur: {temperature}°C, moet onder {MAX_TEMP}°C zijn")
    tello.land()
    tello.end()
    exit()

if flight_time > MAX_FLIGHT_TIME:
    print(f"Vliegtijd: {flight_time} sec, maximum {MAX_FLIGHT_TIME} sec")
    tello.land()
    tello.end()
    exit()

if wifi < MIN_WIFI:
    print(f"Wifi: {wifi}, minimaal {MIN_WIFI} nodig")
    tello.land()
    tello.end()
    exit()

tello.move_up(CLIMB)
tello.move_down(CLIMB)
tello.land()
tello.end()