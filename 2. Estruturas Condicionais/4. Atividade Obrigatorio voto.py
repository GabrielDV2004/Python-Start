import os
os.system("cls || clear") # Limpa o terminal

#Solicitando dados
idade = int(input("Digite sua idade> "))

#Exibindo dados
if idade <= 18 or idade >= 65:
 print("NÃO SÃO OBRIGADOS A VOTAR.")
else:
 print("OBRIGADOS A VOTAR.")