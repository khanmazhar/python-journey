import math

initial_speed = float(input('Enter initial velocity: '))
acceleration = float(input('Enter acceleration: '))
distance = float(input('Enter distance: '))

# calculations
final_velocity = round(
    math.sqrt(pow(initial_speed, 2) + 2*acceleration*distance), 2)

print('The final velocity is', final_velocity)
