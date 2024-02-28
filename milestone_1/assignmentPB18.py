import math

#eq = '4x^2 + 4x +    (-8) =  0'
eq = input("Please give equation: ")

eq = eq.replace(' ', '')
eq = eq.split('+')
eq = ', '.join(eq)
eq = eq.replace(',', '')
eq = eq.replace('(', '')
eq = eq.replace(')', '')
print(eq)



a = int(eq.replace("x^2", "").split()[0])
b = int(eq.replace("x", "").split()[1])
c = int(eq.replace("=0", "").split()[2])


print(a,b,c) # 4 4 -8

d = math.sqrt(b*b-4*a*c)

x1 = int(((-b)+d)/(2*a))
x2 = int(((-b)-d)/(2*a))

print(x1, x2) # -2 1