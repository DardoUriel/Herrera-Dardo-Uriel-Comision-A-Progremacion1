'''
4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo

'''
from ..functions import multiple
number = int(input("ingrese un numero: "))
number2 = int(input("ingrese un numero: "))
print(multiple(number,number2))#devuelve si los numeros son multiplos
