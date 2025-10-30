def sao_anagramas(string1, string2):
    # TODO: Implementar lógica
    pass

def cifra_de_cesar(texto, deslocamento):
    cifra = ""
    for char in texto:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            nova_posicao = (ord(char) - ascii_base + deslocamento) % 26
            cifra += chr(nova_posicao + ascii_base)
        else:
            cifra += char
    return cifra

def valida_cpf(cpf_string):
    # TODO: Implementar lógica
    pass