def sao_anagramas(string1: str, string2: str) -> bool:
    """
    Verifica se duas strings são anagramas.

    Duas palavras são consideradas anagramas se possuem as mesmas letras,
    com a mesma quantidade, mas em ordem diferente.

    Args:
        string1 (str): Primeira string a ser comparada.
        string2 (str): Segunda string a ser comparada.

    Returns:
        bool: Retorna True se as strings forem anagramas, caso contrário False.
    """
    string1 = string1.lower()
    string2 = string2.lower()

    resultado = len(string1) == len(string2) and sorted(string1) == sorted(string2)
    return resultado


def cifra_de_cesar(texto: str, deslocamento: int) -> str:
    """
    Codifica ou decodifica um texto usando a Cifra de César.

    Args:
        texto (str): O texto a ser processado.
        deslocamento (int): O número de posições para deslocar os caracteres.
            Use valores positivos para codificar e negativos para decodificar.

    Returns:
        str: O texto resultante após a codificação/decodificação.

    Examples:
        >>> cifra_de_cesar("AbC", 1)
        'BcD'
        
        >>> cifra_de_cesar("BCd", -1)
        'ABc'
    """
    cifra = ""
    for char in texto:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            nova_posicao = (ord(char) - ascii_base + deslocamento) % 26
            cifra += chr(nova_posicao + ascii_base)
        else:
            cifra += char
    return cifra

def encontrar_maior_palavra(frase: str) -> str:

  """
  Verifica qual a maior palavra de uma frase


  Args:
    frase: (str): String em que será encontrada a maior palavra

  Returns:
    Str: retorna a maior palavra encontrada na frase
  """

  maior_palavra = ""
  maior_tamanho = 0

  lista_de_palavras = frase.split()

  for palavra in lista_de_palavras:
      if len(palavra) > maior_tamanho:
        maior_tamanho = len(palavra)
        maior_palavra = palavra

  return maior_palavra

def valida_cpf(cpf_string):
    # TODO: Implementar lógica
    pass
