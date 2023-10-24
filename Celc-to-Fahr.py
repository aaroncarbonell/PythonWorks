#Aaron Carbonell
#INF103
#Celcius to Fahrenheit Temperature Converter (pg. 160 ex. 9)
#Write a program that converts Celsius temperatures to Fahrenheit temperatures.
#The formula is as follows:

#F=95C+32
#The program should ask the user to enter a temperature in Celsius, then display the temperature
#converted to Fahrenheit.

Cel = float(input('enter degrees celcius: '))

DF = 9/5 * Cel + 32

print('Degrees Fahrenhiet: ' + str(DF))
