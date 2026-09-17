from djitellopy import Tello

tello = Tello()
tello.connect()

battery = tello.get_battery()

print(type(battery))        # <class 'int'>
print(type(type(battery)))  # <class 'type'>

t = type(battery)

print(t is int)  # True
print(t == int)  # True

# 'is' controleert of twee verwijzingen exact hetzelfde object aanwijzen.
# '==' controleert of twee waarden gelijk zijn.
# Hier geven beide True, omdat 't' naar het type-object 'int' verwijst.