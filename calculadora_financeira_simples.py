#Receives user input on present and future values, months and financial tax 
print("Quer descobrir quanto terá de pagar?")
presentValue = int(input("Qual é o valor atual? R$"))
taxaJuros = float(input("Qual é a taxa de juros? "))
tempo = int(input("Em quanto tempo (meses ou anos) vai pagar? "))
juros = taxaJuros / 100 
vF = presentValue * ((1 + juros)**tempo)

#Prints future value output 
print(f"O valor final a ser pago será de: R${vF:.2f}")

#Discover the present value with the final value and time variation

finalValue = int(input("Qual é o valor atual? R$"))
taxaJuros = int(input("Qual é a taxa de juros? "))
tempo = int(input("Em quanto tempo (meses ou anos) vai pagar? "))
juros = taxaJuros / 100
pV = finalValue / ((1 + juros)**tempo)

print(f"O valor inicial a ser pago será de: R${pV:.2f}")