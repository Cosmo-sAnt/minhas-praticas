
from datetime import datetime

# Variavel essa são as Blacklist e a list the conect
blacklist= ["126.255.255.255","191.255.255.255"]
conexoes_recebilda = ["192.168.1.101", "126.255.255.255", "1.178.32.0", "2.57.255.8", "3.2.35.64"]

#Configuração de Arquivo
arquivo = open("Relatorio_v2.txt","a")

#As Condições das variaveis acima
for ip1 in conexoes_recebilda:
    if ip1 in blacklist:
       agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
       mensagem = f"[{agora}]ALERTA!: IP {ip1} bloqueado"
       print(mensagem)
       arquivo.write(f"{mensagem}\n")
    else:
       print(f'IP {ip1} liberado')
arquivo.close()