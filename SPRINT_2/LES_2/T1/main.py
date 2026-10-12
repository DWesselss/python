disk_free     = 45   # %
cpu_load      = 30   # %
temperature   = 48   # °C

disk_ok = disk_free >= 20
cpu_ok  = cpu_load <= 80
temp_ok = temperature <= 70

# TODO: check of alles OK is → print "Backup toegestaan"
if disk_ok and cpu_ok and temp_ok:
    print("Backup toegestaan")

# TODO: check of er iets mis is → print "Backup geweigerd"
if not disk_ok or not cpu_ok or not temp_ok:
    print("Backup geweigerd")

# TODO: aparte schijfwaarschuwing met not
if not disk_ok:
    print(f"Waarschuwing: nog {disk_free}% vrij")