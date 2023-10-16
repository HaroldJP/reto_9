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
    