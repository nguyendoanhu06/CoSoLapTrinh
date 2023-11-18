import random

total= 0
simulation = 10

for _ in range(simulation):
    consecutive= 0
    f_needed = 0

    while consecutive < 3:
        result = random.choice(['H', 'T'])
        print(result, end=' ')
        f_needed += 1

        if result == 'H':
            consecutive= (consecutive + 1) if consecutive >= 0 else 1
        else:
            consecutive = (consecutive - 1) if consecutive <= 0 else -1

    print(f"({f_needed} flip)")
    total += f_needed

average = total / simulation
print(f'On average, {average:.1f} flip were needed.')