#Write a program that calculates and prints the value according to the given formula
#D is the variable whose values should be input to your program in a comma-separated
#sequence

print('pls, enter your values in a comma searated sequence')
C = 50
H = 30
result = input('enter your values: ')
D = result.split(',')

f = ((2*C*D)/H)**0.5
Q = int(round(f))

