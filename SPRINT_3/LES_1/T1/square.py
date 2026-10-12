from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

for i in range(4):
    tello.move_forward(50)
    tello.rotate_clockwise(90)

tello.land()
tello.end()