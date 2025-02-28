import psutil
import time
import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="10.18.32.10",
  user="sentinelaInsert",
  password="Sentinela@123",
  database="sentinela"
)

mycursor = mydb.cursor()

tempoSegundos = int(input("Insira quantos segundos deseja monitorar: "))

while tempoSegundos > 0:
    tempoSegundos-= 1
    now = datetime.datetime.now()

    processadorTempo = psutil.cpu_times_percent()
    tempoAtivo = round(processadorTempo.system + processadorTempo.user, 2)
    tempoInativo = round(processadorTempo.idle, 2)
    porcentagemUsoProcessador = psutil.cpu_percent()
    frequenciaProcessador = psutil.cpu_freq().current

    print("Processador:\n")
    print("Porcentagem de uso do processador: ", porcentagemUsoProcessador)
    print("Tempo que o processador passou realizando operações (em porcentagem): ", tempoAtivo)
    print("Tempo que o processador permaneceu inativo (em porcentagem): ", tempoInativo)
    print("Frequência do processador: ", frequenciaProcessador, "\n")
    
    sql = "INSERT INTO processador VALUES (default, %s, %s, %s, %s, %s, 1, 1)"
    val = (porcentagemUsoProcessador, tempoAtivo, tempoInativo, frequenciaProcessador, now)
    mycursor.execute(sql, val)

    mydb.commit()

    memoriaDisponivel = psutil.virtual_memory().available
    memoriaUtilizadaporcentagem = psutil.virtual_memory().percent
    memoriaNaousada = psutil.virtual_memory().free
    memoriaTotal = psutil.virtual_memory().total

    print("Memória Ram\n")
    print("Quantidade de memória disponível: ", memoriaDisponivel)
    print("Quantidade de memória utilizada em porcentagem: ", memoriaUtilizadaporcentagem)
    print("Quantidade de memória que permaneceu não utilizada: ", memoriaNaousada)
    print("Quantidade de memoria total: ", memoriaTotal, "\n")

    sql = "INSERT INTO memoria VALUES (default, %s, %s, %s, %s, %s, 1, 1)"
    val = (memoriaNaousada, memoriaDisponivel, memoriaTotal, memoriaUtilizadaporcentagem, now)
    mycursor.execute(sql, val)
    mydb.commit()

    bateriaPorcentagematual = psutil.sensors_battery().percent
    bateriaTemporestante = psutil.sensors_battery().secsleft

    print("Bateria\n")
    print("Porcentagem da carga atual da bateria: ", bateriaPorcentagematual)
    print("Tempo Restante em segundos da bateria: ", bateriaTemporestante, "\n")
    sql = "INSERT INTO bateria VALUES (default, %s, %s, %s, 1, 1)"
    val = (bateriaPorcentagematual, bateriaTemporestante, now)
    mycursor.execute(sql, val)
    mydb.commit()

    redeBytesenviados = psutil.net_io_counters().bytes_sent

    print("Rede\n")

    print("Quantidade de bytes enviados: ", redeBytesenviados, "\n")
    
    sql = "INSERT INTO redeChip VALUES (default, %s, %s, 1, 1)"
    val = (redeBytesenviados, now)
    mycursor.execute(sql, val)
    mydb.commit()

    armazenamentoDisponivel = psutil.disk_usage('C:').free
    armazenamentoTotal = psutil.disk_usage('C:').total

    print("Armazenamento\n")

    print("Quantidade de armazenamento disponivel: ", armazenamentoDisponivel)
    print("Quantidade total de armazenamento: ", armazenamentoTotal, "\n")

    sql = "INSERT INTO armazenamento VALUES (default, %s, %s, %s, 1, 1)"
    val = (armazenamentoTotal, armazenamentoDisponivel, now)
    mycursor.execute(sql, val)
    mydb.commit()

    time.sleep(1)