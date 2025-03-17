import psutil
import time
import mysql.connector
import datetime

from mysql.connector import (connection)
mydb = connection.MySQLConnection(host='54.209.134.75', user='sentinelaAdmin', password='Sentinela@123', database='sentinela')
# mydb = connection.MySQLConnection(host='localhost', user='root', password='Gg1502@#', database='sentinela')

mycursor = mydb.cursor()
tempoSegundos = int(input("Insira quantos ciclos deseja monitorar: "))

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


    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 1);"
    val = (tempoAtivo,)
    mycursor.execute(sql, val)

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 2);"
    val = (tempoInativo,)
    mycursor.execute(sql, val)

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 3);"
    val = (porcentagemUsoProcessador,)
    mycursor.execute(sql, val)

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 4);"
    val = (frequenciaProcessador,)
    mycursor.execute(sql, val)


    memoriaDisponivel = psutil.virtual_memory().available
    memoriaUtilizadaporcentagem = psutil.virtual_memory().percent
    memoriaNaousada = psutil.virtual_memory().free
    memoriaTotal = psutil.virtual_memory().total

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 5);"
    val = (memoriaDisponivel,)
    mycursor.execute(sql, val)
    
    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 6);"
    val = (memoriaUtilizadaporcentagem,)
    mycursor.execute(sql, val)

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 7);"
    val = (memoriaNaousada,)
    mycursor.execute(sql, val)

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 8);"
    val = (memoriaTotal,)
    mycursor.execute(sql, val)

    bateriaPorcentagematual = psutil.sensors_battery().percent
    # bateriaTemporestante = psutil.sensors_battery().secsleft

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 9);"
    val = (bateriaPorcentagematual,)
    mycursor.execute(sql, val)

    redeBytesenviados = psutil.net_io_counters().bytes_sent

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 10);"
    val = (redeBytesenviados,)
    mycursor.execute(sql, val)

    if isLinux:
        armazenamentoDisponivel = psutil.disk_usage('/').free
        armazenamentoTotal = psutil.disk_usage('/').total        
    else:
        armazenamentoDisponivel = psutil.disk_usage('C:').free
        armazenamentoTotal = psutil.disk_usage('C:').total

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 11);"
    val = (armazenamentoDisponivel,)
    mycursor.execute(sql, val)

    sql = "INSERT INTO dados VALUES(default, %s, now(), 1, 12);"
    val = (armazenamentoTotal,)
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
