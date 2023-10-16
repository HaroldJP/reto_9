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
    
