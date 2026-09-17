# Variant A
import djitellopy

tello_a = djitellopy.Tello()
tello_a.connect()
print(tello_a.get_battery())

# Variant B
from djitellopy import Tello

tello_b = Tello()
tello_b.connect()
print(tello_b.get_battery())

# Beide varianten werken en printen het batterijpercentage.
# Bij variant A geeft Tello() zonder djitellopy ervoor een NameError.
# Ik kies variant B omdat Tello() korter en duidelijker is.
# Variant A is handig als je meerdere onderdelen uit djitellopy gebruikt.