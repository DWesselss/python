from djitellopy import Tello

tello = Tello()
tello.connect()

battery = tello.get_battery()
height  = tello.get_height()
temp    = tello.get_highest_temperature()
flight_time = tello.get_flight_time()   # seconden op deze accu

if battery >= 20:
    print(f"Batterij: {battery}% is voldoende. Opstijgen goedgekeurd")  
    tello.takeoff()

if height == 0:
    print("Drone staat niet op de grond.")
    tello.end()
    exit()

if temp < 80:
    print(f"Drone temperatuur: {temp}°C is voldoende. Opstijgen goedgekeurd")
    tello.takeoff()
else:
        print("Drone te warm.")
        tello.end()
        exit()
        
if battery < 20:
    print("Batterij te laag.")
    tello.end()
    exit()
    
if flight_time > 300:
    print(f"Drone heeft al {flight_time} seconden gevlogen. Accu moet eruit, en vlucht geweigerd.")
    tello.end()
    exit()