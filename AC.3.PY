#Exercício 1

def determina_tipo_triangulo(a, b, c):
  

  # Validação se os lados formam um triângulo
  if a + b <= c or a + c <= b or b + c <= a:
    return "Não é um triângulo"

  # Verificação se o triângulo é equilátero
  if a == b and b == c:
    return "Equilátero"

  # Verificação se o triângulo é isósceles
  if a == b or a == c or b == c:
    return "Isósceles"

  # Triângulo escaleno
  return "Escaleno"

# Teste da função
def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

# Execução do teste
testa_triangulo()





#Exercício 2

def dia_semana(numero):
 

  dias_semana = {
      1: "Domingo",
      2: "Segunda-feira",
      3: "Terça-feira",
      4: "Quarta-feira",
      5: "Quinta-feira",
      6: "Sexta-feira",
      7: "Sábado",
  }

  if not isinstance(numero, int):
    return ""

  return dias_semana.get(numero, "")

# Teste da função
def testa_dia_semana():
    print(dia_semana(2)) # Segunda-feira
    print(dia_semana(6)) # Sexta-feira
    print(dia_semana(7)) # Sábado
    print(dia_semana(9)) # 

# Execução do teste
testa_dia_semana()






#Exercício 3

def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  return a * b

def divisao(a, b):
  if b == 0:
    return "Divisão por zero!"
  else:
    return a / b

def calculadora():
  while True:
    # Leitura dos dois números
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")

    # Validação dos números
    try:
      numero_1 = float(numero_1)
      numero_2 = float(numero_2)
    except ValueError:
      print("Erro: Os valores digitados não são números válidos.")
      continue

    # Leitura da operação
    operacao = input("Digite a operação (+, -, *, /): ")

    # Execução da operação
    resultado = None
    if operacao == "+":
      resultado = soma(numero_1, numero_2)
    elif operacao == "-":
      resultado = subtracao(numero_1, numero_2)
    elif operacao == "*":
      resultado = multiplicacao(numero_1, numero_2)
    elif operacao == "/":
      resultado = divisao(numero_1, numero_2)
    else:
      print("Erro: Operação inválida.")
      continue

    # Exibição do resultado
    print(f"Resultado: {resultado}")

    # Pergunta para continuar
    continuar = input("Deseja continuar (s/n)? ")
    if continuar.lower() == "n":
      break

# Execução da calculadora
calculadora()


