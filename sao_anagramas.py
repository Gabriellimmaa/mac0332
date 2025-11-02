def sao_anagramas(string1, string2):


  string1 = string1.lower()
  string2 = string2.lower()


  if len(string1) == len(string2) and sorted(string1) == sorted(string2):
    return True
  else:
    return False



def main():
  primeira = input("Digite a primeira palavra: ")
  segunda = input("Digite a segunda palavra: ")
  print(sao_anagramas(primeira, segunda))

main()