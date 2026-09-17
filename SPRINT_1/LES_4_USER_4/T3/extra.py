from djitellopy import Tello

tello = Tello()
tello.connect()

try:
    battery = tello.get_battery()

    # Tijdelijke testwaarde om de assert bewust te laten falen.
    battery = 5

    assert battery > 20, "Batterij te laag!"
    print(f"Batterij: {battery}%")
finally:
    print("Verbinding wordt afgesloten.")
    tello.end()