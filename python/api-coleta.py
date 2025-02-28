import psutil
import time
import mysql.connector
import datetime

from mysql.connector import (connection)
# mydb = connection.MySQLConnection(host='10.18.32.48', user='sentinelaInsert', password='Sentinela@123', database='sentinela')
mydb = connection.MySQLConnection(host='localhost', user='root', password='Gg1502@#', database='sentinela')

mycursor = mydb.cursor()
tempoSegundos = int(input("Insira quantos segundos deseja monitorar: "))

isLinux = psutil.LINUX

#Configuração da máquina
fkMaquina = 1
fkComponenteCPU = 1
fkComponenteRAM = 2
fkComponenteREDE = 4
fkComponenteBATERIA = 3
fkComponenteDISCO = 5

while tempoSegundos > 0:
    tempoSegundos-= 1
    now = datetime.datetime.now()

    processadorTempo = psutil.cpu_times_percent()
    tempoAtivo = round(processadorTempo.system + processadorTempo.user, 2)
    tempoInativo = round(processadorTempo.idle, 2)
    porcentagemUsoProcessador = psutil.cpu_percent()
    frequenciaProcessador = psutil.cpu_freq().current

    sql = "INSERT INTO processador VALUES (default, %s, %s, %s, %s, %s, 1, %s)"
    val = (porcentagemUsoProcessador, tempoAtivo, tempoInativo, frequenciaProcessador, now, fkComponenteCPU)
    mycursor.execute(sql, val)

    mydb.commit()

    memoriaDisponivel = psutil.virtual_memory().available
    memoriaUtilizadaporcentagem = psutil.virtual_memory().percent
    memoriaNaousada = psutil.virtual_memory().free
    memoriaTotal = psutil.virtual_memory().total

    sql = "INSERT INTO memoria VALUES (default, %s, %s, %s, %s, %s, 1, %s)"
    val = (memoriaNaousada, memoriaDisponivel, memoriaTotal, memoriaUtilizadaporcentagem, now, fkComponenteRAM)
    mycursor.execute(sql, val)
    mydb.commit()

    bateriaPorcentagematual = psutil.sensors_battery().percent
    # bateriaTemporestante = psutil.sensors_battery().secsleft

    sql = "INSERT INTO bateria VALUES (default, %s, 0, %s, 1, %s)"
    val = (bateriaPorcentagematual, now, fkComponenteBATERIA)
    mycursor.execute(sql, val)
    mydb.commit()

    redeBytesenviados = psutil.net_io_counters().bytes_sent

    sql = "INSERT INTO redeChip VALUES (default, %s, %s, 1, %s)"
    val = (redeBytesenviados, now, fkComponenteREDE)
    mycursor.execute(sql, val)
    mydb.commit()

    if isLinux:
        armazenamentoDisponivel = psutil.disk_usage('/').free
        armazenamentoTotal = psutil.disk_usage('/').total        
    else:
        armazenamentoDisponivel = psutil.disk_usage('C:').free
        armazenamentoTotal = psutil.disk_usage('C:').total

    sql = "INSERT INTO armazenamento VALUES (default, %s, %s, %s, 1, %s)"
    val = (armazenamentoTotal, armazenamentoDisponivel, now, fkComponenteDISCO)
    mycursor.execute(sql, val)
    mydb.commit()
    
    print("Processador:\n")
    print("Porcentagem de uso do processador: ", porcentagemUsoProcessador)
    print("Tempo que o processador passou realizando operações (em porcentagem): ", tempoAtivo)
    print("Tempo que o processador permaneceu inativo (em porcentagem): ", tempoInativo)
    print("Frequência do processador: ", frequenciaProcessador, "\n")

    print("Memória Ram\n")
    print("Quantidade de memória disponível: ", memoriaDisponivel)
    print("Quantidade de memória utilizada em porcentagem: ", memoriaUtilizadaporcentagem)
    print("Quantidade de memória que permaneceu não utilizada: ", memoriaNaousada)
    print("Quantidade de memoria total: ", memoriaTotal, "\n")

    print("Bateria\n")
    print("Porcentagem da carga atual da bateria: ", bateriaPorcentagematual)

    print("Rede\n")
    print("Quantidade de bytes enviados: ", redeBytesenviados, "\n")

    print("Armazenamento\n")
    print("Quantidade de armazenamento disponivel: ", armazenamentoDisponivel)
    print("Quantidade total de armazenamento: ", armazenamentoTotal, "\n")

    time.sleep(15)