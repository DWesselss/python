def space_zone(free):
    if free < 10:
        return "kritiek"
    elif free < 20:
        return "laag"
    else:
        return "ok"

zone1 = space_zone(9)
zone2 = space_zone(19)
zone3 = space_zone(21)

print (f"Vrije ruimte 9% > zone: {zone1} (verwacht: kritiek)")
print (f"Vrije ruimte 15% > zone: {zone2} (verwacht: laag)")
print (f"Vrije ruimte 25% > zone: {zone3} (verwacht: ok)")