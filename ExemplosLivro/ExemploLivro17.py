#-------------TIPOS DE ARGUMENTOS EM UMA FUNÇÃO EM PYTHON------------


#TIPO 1:Parâmetro posicional, obrigatório, sem valor default (padrão).
def somar(a, b):
    return a + b

resultado = somar(2, 3) #passar os dois argumentos obrigatórios
print(resultado)



#TIPO 2:Parâmetro posicional, obrigatório, com valor default (padrão).
def calcular_desconto(valor, desconto=0): # O parâmetro desconto possui zero valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) # Não aplicar nenhum desconto
valor2 = calcular_desconto(100, 0.25) # Aplicar desconto de 25%

print(f"\nPrimerio valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")

def cadastrar_pessoa(nome, idade, cidade):
    print("\nDados a serem cadastrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

cadastrar_pessoa("joão", 23, "São Paulo")
cadastrar_pessoa("São Paulo", "joão", 23)





#TIPO 3:Parâmetro nominal, obrigatório, sem valor default (padrão).
def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()
texto = converter_maiuscula(flag_maiuscula=True, texto="João")  # Passagem nominal de parâmetros
print(texto)





#TIPO 4:Parâmetro nominal, obrigatório, com valor default (padrão).
def converter_maiuscula(texto, flag_maiuscula=True): # O parâmetro flag_minuscula possui True como valor default
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()
    
texto1 = converter_maiuscula(flag_maiuscula=True, texto="LINGUAGEM de Programação")  # Passagem nominal de parâmetros
texto2 = converter_maiuscula(texto="LINGUAGEM de Programação")

print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")




#TIPO 5:Parâmetro posicional e não obrigatório (args).
def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for i,valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

print("\nChamada1")
imprimir_parametros("São Paulo", 10, 23.78, "João")

print("\nChamada2")
imprimir_parametros("São Paulo", 10)




#TIPO 6:Parâmetro nominal e não obrigatório (kwargs).
def imprimir_parametros(**kwargs):
    print(f"Tipo de obejeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros(cidade="São Paulo", idade=33, nome="Joâo")

print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)
        


