battery_str = input("Batterijstand (%): ")

# input() geeft tekst terug, dus we zetten de string om naar een integer.
battery = int(battery_str)

if battery > 20:
    print("Batterij OK, stijgen!")
else:
    print("Batterij te laag")