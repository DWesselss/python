from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

for i in range(6):
    tello.move_forward(30)
    tello.rotate_clockwise(60)

tello.land()
tello.end()