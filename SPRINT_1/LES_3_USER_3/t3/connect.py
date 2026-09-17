# Importeert de Tello-klasse.
from djitellopy import Tello

# Maakt een Tello-object aan.
tello = Tello()

# Verbindt met de drone via wifi.
tello.connect()

# Laat hem vliegen
tello.move_up(50)

# Leest en print het batterijpercentage.
print(tello.get_battery())