MIN_BATTERY = 20

battery = 25

if battery < MIN_BATTERY:
    print(f"Batterij is lager dan de grens van {MIN_BATTERY}%")

if battery == MIN_BATTERY:
    print(f"Batterij is precies gelijk aan de grens van {MIN_BATTERY}%")

if battery > MIN_BATTERY:
    print(f"Batterij is hoger dan de grens van {MIN_BATTERY}%")