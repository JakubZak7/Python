###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = True
light_switch2 = True
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 1
print(f"How many light bulbs are lit: {bulbs_on}")