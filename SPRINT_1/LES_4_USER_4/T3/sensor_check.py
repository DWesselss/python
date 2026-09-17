# Importeert de Tello-klasse uit djitellopy.
from djitellopy import Tello

# Maakt een object aan waarmee we de drone besturen.
tello = Tello()

# Verbindt het programma met de drone via wifi.
tello.connect()

# Vraagt het batterijpercentage van de drone op.
battery = tello.get_battery()

# Toont het batterijpercentage in de terminal.
print(f"Batterij: {battery}%")

# Controleert of de batterij hoger is dan 20%.
assert battery > 20, "Batterij te laag om op te stijgen!"

# Sluit de verbinding met de drone netjes af.
tello.end()