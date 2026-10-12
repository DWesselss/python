disk_free     = 45   # %
cpu_load      = 30   # %
temperature   = 48   # °C

disk_ok = disk_free >= 20
cpu_ok  = cpu_load <= 80
temp_ok = temperature <= 70

# Check of alles OK is
if disk_ok and cpu_ok and temp_ok:
    print("Backup toegestaan")

# Check of er iets mis is
if not disk_ok or not cpu_ok or not temp_ok:
    print("Backup geweigerd")

# Aparte schijfwaarschuwing
if not disk_ok:
    print(f"Waarschuwing: nog {disk_free}% vrij")