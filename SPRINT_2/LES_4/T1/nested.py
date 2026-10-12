from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff()
tello.move_forward(100)

battery = tello.get_battery()
flight_time = tello.get_flight_time()
wifi = tello.query_wifi_signal_noise_ratio()
temperature = tello.get_temperature()

if battery > 40:
    if flight_time < 120:
        if wifi >= 60:
            if temperature < 70:
                tello.move_forward(100)
                tello.land()
            else:
                print(f"Temperatuur te hoog: {temperature}°C")
                tello.land()
        else:
            print(f"Wifi te zwak: {wifi}")
            tello.land()
    else:
        print(f"Vliegtijd te hoog: {flight_time} seconden")
        tello.land()
else:
    print(f"Batterij te laag: {battery}%")
    tello.land()

tello.end()