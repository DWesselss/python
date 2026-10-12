battery = tello.get_battery()
wifi    = tello.get_wifi()

# Guard 1: batterij
if battery < 20:
    print(f"Batterij te laag: {battery}%")
    tello.end()
    exit()

# TODO: Guard 2 — wifi
if wifi < 0:
    print(f"Geen Wifi")
    tello.end()
    exit()

tello.takeoff()