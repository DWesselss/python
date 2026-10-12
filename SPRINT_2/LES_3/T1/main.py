from djitellopy import Tello

tello = Tello()
tello.connect()
battery = tello.get_battery()

# TODO: voeg guard clause toe
if battery < 20:
    print("Batterij is te laag om te vliegen")
    tello.end()
    exit()

tello.takeoff()
tello.move_forward(100)
tello.land()
tello.end()