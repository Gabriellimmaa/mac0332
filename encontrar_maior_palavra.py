def encontrar_maior_palavra(frase):

  maior_paravra =""
  maior_tamanho = 0

  lista_de_palavras = frase.split()

  for palavra in lista_de_palavras:
      if len(palavra) > maior_tamanho:
        maior_tamanho = len(palavra)
        maior_palavra = palavra

  return maior_palavra

def main():
  frase = input("Digite uma frase: ")
  print(encontrar_maior_palavra(frase))

main()