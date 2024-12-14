# This is program for area of circle
print('welcome to our area calculator')
print('enter which area you have to calculate')
shape = input()
print ('Have have selectcd '+ shape)
if shape == "circle":
    print('input radius of circle')
    radius = input()
    area = int(radius)*2*int(22/7)
    print('your area of circle is '+ str(area))
elif shape== "square":
    print ('enter length of square ')
    length=input()
    area = int(length)*int(length)
    print('your area of square is ' + str(area))
elif shape=="triangle":
    print('enter base and height of triangle')
    base = input()
    height= input()
    print("you have entered base ="+ str(base) ) 
    print("you have entered height =" + str(height) )
    area = float(1/2)*int(height)*int(base)
    print('your area of triangle is '+ str(area))
else :
    print('sorry I cannot calculate your shapes area')