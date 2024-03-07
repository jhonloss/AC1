
# Exercício 1

def bhaskara(a, b, c):
  
  
  delta = b**2 - 4*a*c
  if delta == 0:
    x1 = -b / (2*a)
    return x1, x1
  elif delta > 0:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    return x1, x2
  else:
    return None

# Leitura dos coeficientes
a = float(input("Digite o coeficiente de x²: "))
b = float(input("Digite o coeficiente de x: "))
c = float(input("Digite o termo independente: "))

# Cálculo das raízes
raizes = bhaskara(a, b, c)

# Apresentação dos resultados
if raizes is None:
  print("A equação não possui raízes reais.")
elif isinstance(raizes, float):
  print(f"A equação possui uma única raiz real: {raizes}")
else:
  x1, x2 = raizes
  print(f"A equação possui duas raízes reais: {x1} e {x2}")









# Exercício 2

  # Leitura do ano
ano = int(input("Digite o ano: "))

# Cálculo da expressão lógica
bissexto = (ano % 4 == 0) and (not (ano % 100 == 0) or ano % 400 == 0)

# Exibição do resultado
print(f"O ano {ano} é bissexto? {bissexto}")