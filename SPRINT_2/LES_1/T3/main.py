battery = None  # Test afzonderlijk met: None, 0, 15 en 80

# Guard 1: controleren of er een meting is.
if battery is None:
    print("Geen meting beschikbaar")
    exit()

# Guard 2: controleren of de batterij volledig leeg is.
if battery == 0:
    print("Batterij volledig leeg")
    exit()

# Guard 3: controleren of de batterij te laag is.
if battery <= 20:
    print(f"Batterij te laag: {battery}%")
    exit()

print(f"Batterij OK: {battery}%")
print("Takeoff wordt toegestaan")  # Simulatie zonder echte drone