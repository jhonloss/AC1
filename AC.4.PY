def ler_nome():
  nome = input("Digite seu nome: ")
  if not nome:
    print("Nome inválido.")
    exit()
  return nome

def ler_notas():
  ap1 = float(input("Digite a nota da AP1: "))
  ap2 = float(input("Digite a nota da AP2: "))
  as_ = float(input("Digite a nota da AS: "))
  ac = float(input("Digite a nota da AC: "))

  if not all(0 <= nota <= 10 for nota in [ap1, ap2, as_, ac]):
    print("Erro: Notas inválidas.")
    exit()

  return ap1, ap2, as_, ac

def calcular_media(ap1, ap2, as_, ac):
  menor_ap = min(ap1, ap2)
  media = (ap1 + ap2 - menor_ap + as_) * 0.4 + ac * 0.2
  return media

def exibir_resultado(nome, media):
  aprovado = "Aprovado" if media >= 7.0 else "Reprovado"
  print(f"{nome}, sua média final é {media:.2f}. Você está {aprovado}.")

# Leitura do nome
nome = ler_nome()

# Leitura das notas
ap1, ap2, as_, ac = ler_notas()

# Cálculo da média
media = calcular_media(ap1, ap2, as_, ac)

# Exibição do resultado
exibir_resultado(nome, media)
