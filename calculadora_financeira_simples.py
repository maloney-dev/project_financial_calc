#Receives user input on present and future values, months and financial tax 
print("Quer descobrir quanto terá de pagar?")
presentValue = int(input("Qual é o valor atual? R$"))
taxaJuros = int(input("Qual é a taxa de juros? "))
tempo = int(input("Em quantos meses vai pagar? "))
juros = taxaJuros / 100 
vF = presentValue * ((1 + juros)**tempo)
