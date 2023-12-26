from controller_investimentos import controller_investimentos
from controller_mail import controller_mail
from consome_openAI import consome_openAI
from controller_cliente import controller_cliente
import asyncio

print(
    "Este sistema cria uma mensagem de marketing personalizada por Inteligencia Artificial e envia para o e-mail do cliente.")
conta_input = (input("Insira a conta do cliente: "))

# Cria uma instância da classe controller_cliente
cliente_instancia = controller_cliente()
# Chama o método cliente na instância
result = cliente_instancia.cliente(conta=conta_input)
novo_result = [{'id': dado['id'], 'nome': dado['nome'], 'email': dado['email'], 'perfil': dado['perfil']} for dado in
               result]
# print(novo_result)

# Cria uma instância da classe controller_cliente
controller_investimentos = controller_investimentos()
# Chama o método cliente na instância
resultado_invest = controller_investimentos.investimentos()
# print(resultado_invest)

for dicionario in novo_result:
    id = dicionario['id']
    nome = dicionario['nome']
    email = dicionario['email']
    perfil = dicionario['perfil']

# print(f'ID: {id}')
# print(f'Nome: {nome}')
# print(f'Email: {email}')
# print(f'Perfil: {perfil}')

# Crie uma instância da classe
instancia_consomidor = consome_openAI(nome=nome, perfil=perfil, resultado_invest=resultado_invest)
resposta = instancia_consomidor.openAI()
mensagem = resposta.content
print(mensagem)


#enviar a mensagem para o e-mail
controller_mail = controller_mail(mensagem=mensagem, email=email)
controller_mail.enviar_email()

# Exiba a mensagem 
print(f'Para o cliente {nome} da conta {conta_input} foi enviada a seguinte mensagem no e-mail {email}')
print(mensagem)

