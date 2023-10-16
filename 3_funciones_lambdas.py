print("La primera función que vamos ver es una que sirve para calcular el promedio de 5 números dados")
xd = input("Por favor digite cualquier tecla para continuar: ")
if __name__ == "__main__":
  a = float(input("Escriba el primer número real: "))
  b = float(input("Escriba el segundo número real: "))
  c = float(input("Escriba el tercer número real: "))
  d = float(input("Escriba el cuarto número real: "))
  e = float(input("Escriba el quinto número real: "))
  promedio = lambda a, b, c, d, e: (a + b + c + d + e) / 5
  prom = promedio(a, b, c, d, e)
  print("El promedio de los números " +str(a)+ ", " +str(b)+ ", " +str(c)+ ", " +str(d)+ " y " +str(e)+ " es " +str(prom))
print("Ahora, la segunda función que vamos a ver sirve para calcular el área de un rectángulo.")
xd1 = input("Por favor digite cualquier tecla para continuar: ")
if __name__ == "__main__":
  f = float(input("Ingrese el primer lado del rectángulo: "))
  g = float(input("Ingrese el segundo lado del rectángulo: "))
  area = lambda f, g: f*g
  arear = area(f, g)
  print("El área del rectángulo ingresado es de " +str(arear))
print("Por último, la tercera función que vamos a ver sirve para calcular el volumen de una esfera.")
xd2 = input("Por favor ingrese cualquier tecla para continuar: ")
if __name__ == "__main__":
  import math
  r = float(input("Ingrese el radio de la esfera: "))
  volumen = lambda r: (4/3)*math.pi*(r**3)
  volumene = volumen(r)
  print("El volumen de una esfera con radio " +str(r)+ " es de " +str(volumene))