def battery_ok(battery):
    return 20 < battery <= 100


# normale %
assert battery_ok(87) is True, "87% moet mogen"

# 20% moet afgeween
assert battery_ok(20) is False, "20% moet worden geweigerd"

# onmogelijk
assert battery_ok(120) is False, "120% is een onmogelijk batterijpercentage"

print("Alle checks geslaagd — klaar om te vliegen.")

# voor error hieronder # weghalen
# assert battery_ok(20) is True, "Test geslaagd: 20% is te laag om te vliegen"