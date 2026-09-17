def battery_ok(battery):
    return 20 < battery <= 100


# Normale waarde: 87% moet worden toegestaan.
assert battery_ok(87) is True, "87% moet mogen"

# Grenswaarde: precies 20% moet worden geweigerd.
assert battery_ok(20) is False, "20% moet worden geweigerd"

# Onmogelijke waarde: 120% moet worden geweigerd.
assert battery_ok(120) is False, "120% is een onmogelijk batterijpercentage"

print("Alle checks geslaagd — klaar om te vliegen.")

# Verwijder het hekje hieronder om bewust een AssertionError te tonen:
# assert battery_ok(20) is True, "Test geslaagd: 20% is te laag om te vliegen"