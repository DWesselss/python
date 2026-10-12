# importeert tello van dji tellopy lib
from djitellopy import Tello

# maakt object aan om drone te commanderen
tello = Tello()

# verbind met drone
tello.connect()

# vraagt batterij%
battery = tello.get_battery()

# Toont het batterijpercentage in de terminal.
print(f"Batterij: {battery}%")

# kijkt of de batterij hoger is dan 20%
assert battery > 20, "Batterij te laag om op te stijgen!"

# sluit de verbinding met de drone
tello.end()