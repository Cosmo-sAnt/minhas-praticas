#1.vamos fazer uma vareavel chamada arqui1:essa variavel vai abri o relatorio v2 pra ver quantos ip bloqueados
aquir1 = open("Relatorio_v2.txt", "r")

#2.criar o contador
total_bloqueados = 0

print('---INICIANDO A AUDITORIA DE SEGURANÇA---')

#3. As condições pra percorrer o for por cada linha
for linha in aquir1:
    if "ALERTA" in linha:
        total_bloqueados = total_bloqueados + 1
        print(f'Detectamos no log: {linha.strip()}')
#3,5.aqui nao tem o else pois ele so ia roda por mais tempo no terminal ia ser inutiu
#4.Fechamento de arqui1
aquir1.close()

print('--------------------------------------------')
print(f"RESUMO: Foram detectado {total_bloqueados} IPs boqueados no relatorio.")