# ============================================================================
#   Star 1
# ============================================================================


modules_file = open('2019day1modules.txt', 'r')
module_masses = modules_file.readlines()

required_fuel = 0

for mass in module_masses:
    required_fuel += int(mass)//3 - 2

print("total:", required_fuel)


# ============================================================================
#   Star 2
# ============================================================================


modules_file = open('2019day1modules.txt', 'r')
module_masses = list(map(int, modules_file.readlines()))

total_fuel = 0


def required_fuel(mass):
    fuel = mass//3 - 2

    if fuel < 0:
        return 0
    return fuel + required_fuel(fuel)


for mass in module_masses:
    total_fuel += required_fuel(mass)

print("total:", total_fuel)
