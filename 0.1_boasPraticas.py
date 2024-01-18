############# Fazer uso de PSEUDOCÓDICO
### - Calcular a Àrea de um Paralelograma
"""
Um paralelograma é um quadrilátero com lados opostos paralelos (e portanto ângulos opostos iguais). 
Um quadrilátero com lados iguais é chamado de losango e um paralelogramo cujos ângulos são todos ângulos retos é chamado de retângulo.
  1 - Exiba "Bem-vindo ao calculador de área de paralelogramo"
  2 - Peça para usuário inserir o comprimento da base
  3 - Armazene o comprimento da base em uma variável
  4 - Peça para o usuário inserir a palavra
  5 - Armazene a altura em uma variável
  6 - Calcule a área do paralelogramo: base * altura
  7 - Armazene o resultado em uma variável
  8 - Exiba o resultado
""" 
print("Exiba Bem-vindo ao calculador de área de paralelogramo")
base = float(input("Insira o comprimento da base: "))
altura = float(input("Insira a altura: "))
area = base * altura
print("A area do Paralelograma é: ", area)
