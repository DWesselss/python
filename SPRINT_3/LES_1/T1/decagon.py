from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

for i in range(10):
    tello.move_forward(20)
    tello.rotate_clockwise(36)

tello.land()
tello.end()