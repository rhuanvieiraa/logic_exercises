import datetime
import random

nome_completo = input("Nome e sobrenome: ")
num_quarto = int(input("Número do quarto: "))
data_checkin = input("Data (dd/mm/aaaa): ")

data_obj = datetime.datetime.strptime(data_checkin, "%d/%m/%Y")
ano_reserva = data_obj.year
numero_aleatorio = random.randint(1000, 9999)

posicao_espaco = nome_completo.find(" ")
if posicao_espaco != -1:
    primeiro_nome = nome_completo[:posicao_espaco]
else:
    primeiro_nome = nome_completo

codigo_reserva = f"{primeiro_nome}{num_quarto}{ano_reserva}{numero_aleatorio}"

if num_quarto <= 100:
    tipo_acomodacao = "Econômico"
elif num_quarto <= 300:
    tipo_acomodacao = "Standard"
else:
    tipo_acomodacao = "Luxo"

print("\n--- RELATÓRIO ---")
print("Nome:", nome_completo)
print("Data:", data_checkin)
print("Quarto:", num_quarto)
print("Código:", codigo_reserva)
print("Tipo:", tipo_acomodacao)
