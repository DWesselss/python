def can_fly(battery):
    return battery > 20


assert can_fly(100) is True, "100% moet mogen"
assert can_fly(21) is True, "21% moet nog mogen"
assert can_fly(20) is False, "20% is de grens — weigeren"
assert can_fly(0) is False, "0% moet weigeren"
assert can_fly(-1) is False, "-1% moet weigeren"

print("can_fly() volledig bewezen!")