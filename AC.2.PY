

# Exercício 1


def eq_seg_grau(a, b, c):
  """
  Função para calcular as raízes de uma equação de segundo grau.

  Parâmetros:
    a: Coeficiente de x².
    b: Coeficiente de x.
    c: Termo independente.

  Retorno:
    Uma tupla com as duas raízes da equação.
  """
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

# Exemplo de uso
a = 1
b = 2
c = 1

raizes = eq_seg_grau(a, b, c)

if raizes is None:
  print("A equação não possui raízes reais.")
elif isinstance(raizes, float):
  print(f"A equação possui uma única raiz real: {raizes}")
else:
  x1, x2 = raizes
  print(f"A equação possui duas raízes reais: {x1} e {x2}")






def bissexto(ano):
  """
  Função para verificar se um ano é bissexto.

  Parâmetro:
    ano: Um valor inteiro que representa o ano.

  Retorno:
    True se o ano for bissexto, False caso contrário.
  """
  if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
      return False
    else:
      return True
  else:
    return False

# Exemplo de uso
ano = 2025

if bissexto(ano):
  print(f"O ano {ano} é bissexto.")
else:
  print(f"O ano {ano} não é bissexto.")







#Exercício 2
  

def calcula_salario(valor_hora, num_horas, irpf=0.275):


  if not isinstance(valor_hora, (int, float)) or not isinstance(num_horas, (int, float)):
    raise TypeError("Os parâmetros valor_hora e num_horas devem ser números.")

  if irpf < 0 or irpf > 1:
    raise ValueError("O parâmetro irpf deve estar entre 0 e 1.")

  salario_bruto = valor_hora * num_horas
  imposto_renda = salario_bruto * irpf
  salario_liquido = salario_bruto - imposto_renda

  return salario_liquido

# Exemplo de uso
valor_hora = 25.0
num_horas = 180

salario_liquido = calcula_salario(valor_hora, num_horas)

print(f"Salário líquido: R${salario_liquido:.2f}")