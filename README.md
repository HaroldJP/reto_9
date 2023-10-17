# reto_9

### Punto 1

De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

Para desarrollar este punto se me ocurrió hacer las 3 funciones consecutivamente en un único programa de python, de manera que en un mismo programa se puedan ejecutar las 3 funciones.
La primera de  ellas, sirve para calcular el promedio de 5 números; la segunda de ellas, sirve para calcular el área de un rectángulo; la tercera, sirve para calcular el volumen de una esfera.

```python
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
```

Si no es de su agrado, a continuación adjunto el programa individual para cada función.

Para calcular el promedio de los 5 números:

```python
print("La primera función que vamos ver es una que sirve para calcular el promedio de 5 números dados")
if __name__ == "__main__":
  a = float(input("Escriba el primer número real: "))
  b = float(input("Escriba el segundo número real: "))
  c = float(input("Escriba el tercer número real: "))
  d = float(input("Escriba el cuarto número real: "))
  e = float(input("Escriba el quinto número real: "))
  promedio = lambda a, b, c, d, e: (a + b + c + d + e) / 5
  prom = promedio(a, b, c, d, e)
  print("El promedio de los números " +str(a)+ ", " +str(b)+ ", " +str(c)+ ", " +str(d)+ " y " +str(e)+ " es " +str(prom))
```

La segunda función para calcular el área de un rectángulo:

```python
print("Ahora, la segunda función que vamos a ver sirve para calcular el área de un rectángulo.")
if __name__ == "__main__":
  f = float(input("Ingrese el primer lado del rectángulo: "))
  g = float(input("Ingrese el segundo lado del rectángulo: "))
  area = lambda f, g: f*g
  arear = area(f, g)
  print("El área del rectángulo ingresado es de " +str(arear))
```

Por último, la función que sirve para calcular el área de una esfera:

```python
print("La tercera función que vamos a ver sirve para calcular el volumen de una esfera.")
if __name__ == "__main__":
  import math
  r = float(input("Ingrese el radio de la esfera: "))
  volumen = lambda r: (4/3)*math.pi*(r**3)
  volumene = volumen(r)
  print("El volumen de una esfera con radio " +str(r)+ " es de " +str(volumene))
```

### Punto 2

De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

Para este punto haré la misma dinámica que con el punto anterior. A continuación, un único programa para ejecutar las 3 funciones a la vez, las cuales sirven para calcular el promedio multiplicativo de 5 números, calcular el perímetro de un círculo y también calcular el perímetro de un rectángulo.

```pyhton
print("Vamos a inciar con la primera de las 3 funciones, la cual sirve para calcular el promedio multiplicativo de 5 números dados.")
xd = input("Por favor ingrese cualquier tecla para continuar: ")
def prom_mul(*args) -> float:
    mul :  float = 1
    for num in args:
        mul *= num
    return mul**(1/5)
if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    print("El promedio multiplicativo de los números " +str(a)+ ", " +str(b)+ ", " +str(c)+ ", " +str(d)+ " y " +str(e)+ " es " +str(prom_mul(a, b, c, d, e)))
print("Ahora, vamos con la segunda función que sirve para calcular el perímetro de un círculo con su radio.")
xd2 = input("Por favor ingrese cualquier tecla para continuar: ")
r =float(input("Ingrese el radio del círculo: "))
def perimetro(*argus) -> float:
    import math
    return 2*math.pi*r
if __name__ == "__main__":
    print("El perímetro de un círculo con radio " +str(r)+ " es " +str(perimetro(r)))
print("Por último, nuestra tercera función sirve para calcular el perímetro de un rectángulo.")
xd3 = input("Por favor ingrese cualquier tecla para continuar: ")
f = float(input("Ingrese el primer lado del rectángulo: "))
g = float(input("Ingrese el segundo lado del rectángulo: "))
def perimetror(*argums) -> float:
    return (f*2) + (g*2)
if __name__ == "__main__":
    print("El perímetro de un rectángulo con lados " +str(f)+ " y " +str(g)+ " es " +str(perimetror(f, g)))
```

Ahora, cada prorama de forma individual, iniciando por el que sirve para calcular el promedio multiplicativo:

```python
print("Vamos a inciar con la primera de las 3 funciones, la cual sirve para calcular el promedio multiplicativo de 5 números dados.")
def prom_mul(*args) -> float:
    mul :  float = 1
    for num in args:
        mul *= num
    return mul**(1/5)
if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    print("El promedio multiplicativo de los números " +str(a)+ ", " +str(b)+ ", " +str(c)+ ", " +str(d)+ " y " +str(e)+ " es " +str(prom_mul(a, b, c, d, e)))
```

Ahora, la segunda función que sirve para calcular el perímetro de un círculo:

```python
print("Ahora, vamos con la segunda función que sirve para calcular el perímetro de un círculo con su radio.")
r =float(input("Ingrese el radio del círculo: "))
def perimetro(*argus) -> float:
    import math
    return 2*math.pi*r
if __name__ == "__main__":
    print("El perímetro de un círculo con radio " +str(r)+ " es " +str(perimetro(r)))
```

Por último, la tercera función que sirve para calcular el perímetro de un rectángulo:

```python
print("Por último, nuestra tercera función sirve para calcular el perímetro de un rectángulo.")
f = float(input("Ingrese el primer lado del rectángulo: "))
g = float(input("Ingrese el segundo lado del rectángulo: "))
def perimetror(*argums) -> float:
    return (f*2) + (g*2)
if __name__ == "__main__":
    print("El perímetro de un rectángulo con lados " +str(f)+ " y " +str(g)+ " es " +str(perimetror(f, g)))
```

### Punto 3

Escriba una función recursiva para calcular la operación de la potencia.

```python
def potencia(x, n):
  if n == 0:
    return 1
  else:
    return x * potencia(x, n - 1)
if __name__ == "__main__":
  x = float(input("Ingrese un número: "))
  n = int(input("Ingrese la potencia de ese número: "))
  potenci = potencia(x, n)
  print(str(x)+ "^" +str(n)+ " es igual a " + str(potenci))
```

### Punto 4

Utilice la siguiente plantilla de code para contar el tiempo:

Para empezar, vamos a utilizar la iteración de manera que, por ejemplo, al poner un valor de 10, el tiempo arrojado es de 0.002999, para valores más elevados como 100, el tiempo es de 0.071, lo cual ya es una diferencia de tiempo considerable comparando 10 con 100. Exactamente de 0.0681.

```python
def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    print(sumFibo)
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

if __name__ == "__main__":
  num = int(input("Ingrese numero: "))
  serieFibo = fibo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
```

### Punto 5

Crear cuenta en stackoverflow y adjuntar imagen en el repo

![](https://i.ibb.co/89ydvwH/overflow.png)

### Punto 6

Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

https://www.linkedin.com/in/harold-jim%C3%A9nez-1608a1296/
