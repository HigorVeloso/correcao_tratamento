# Criando a função que recebe a lista de listas com as notas
def corretor(testes: list):
  pontuacoes = [] # criando a lista que receberá od dados caso a exceção não seja lançada
  try:
    for teste in testes:
      nota = 0 # variável que acumula os dados unicos da lista
      for i in range(len(teste)):
        if teste[i] not in ['A', 'B', 'C', 'D']: # Verificamos se temos uma alternativa valida
          raise ValueError(f'A alternativa {teste[i]} não é uma opção de alternativa válida')
        elif teste[i] == gabarito[i]: # Verificamos se as respostas são iguais e adicionamos ao dado
          nota += 1
      pontuacoes.append(nota)
  except Exception as e:
    print(e)
  else:
    return pontuacoes


# criando a função que recebe as duas listas e a operação a ser realizada
def divide_colunas(lista_1: list, lista_2: list) -> list:
  # try-except que verifica se é possível calcular a divisão e lança exceção se as listas tem tamanhos diferentes
  # ou se temos alguma divisão por zero em um dos cálculos entre os números das listas
  try:
    if len(lista_1) != len(lista_2): # Verificando se as listas tem o mesmo tamanho, se não lança uma exceção
      raise ValueError("As listas precisam ter o mesmo tamanho")

    # A função zip pareia os elementos das listas e uma lista é gerada por meio da razão entre os pares
    resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)] 
  except ValueError as e:
    print(e)
  except ZeroDivisionError as e:
    print(f"{e}: A 2ª lista não pode possuir um valor igual a 0")
  else:
    return resultado

