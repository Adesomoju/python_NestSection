#This looks familiar doesn't it? If not, that's okay. The above is a popular theorem in
#Mathematics which basically means if you sum the square two sides of a special kind of
#triangle (right-angled triangle), you'll get the squre of the third side.
#You are to implement a simple Python function to calculate it

print('\tsimple quadractic maths function')
print(
    '''
    C = longest side
    a = length
    b = breadth
    
    ''')
a = int(input('enter the value for a: '))
b = int(input('enter the value for b: '))

C = ((a**2) + (b**2))**0.5
sqrt_c = C**2
sqrt_c = (a**2) + (b**2)

print('C = ',C,'cm')
print('C^2 = ',sqrt_c,'cm')

