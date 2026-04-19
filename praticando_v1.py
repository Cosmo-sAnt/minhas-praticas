# Variavel essa são as Blacklist e a list the conect
blacklist= ["126.255.255.255","191.255.255.255"]
conexoes_recebilda = ["192.168.1.101", "126.255.255.255", "1.178.32.0", "2.57.255.8", "3.2.35.64"]

#Configuração de Arquivo
arquivo = open("Relatorio.txt","a")

#As Condições das variaveis acima
for ip in conexoes_recebilda:
    if ip in blacklist:
        mensagen = f"ALERTA : IP {ip} bloqueado!\n"
        print(mensagen)
        arquivo.write(mensagen)
    else:
        print(f'IP {ip} liberado')

arquivo.close()