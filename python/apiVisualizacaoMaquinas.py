import time

# Configuração do Banco de Dados
from mysql.connector import (connection)
mydb = connection.MySQLConnection(host='10.18.32.28', user='sentinelaSelect', password='Sentinela@123', database='sentinela')
# mydb = connection.MySQLConnection(host='localhost', user='root', password='Gg1502@#', database='sentinela')
mycursor = mydb.cursor()

# Listar as máquinas existentes e selecionar uma
def listarMaquinas():
  global idSelecionado
  sql = 'SELECT m.idMaquina, m.nomeModelo, m.fabricanteModelo, m.status  from maquina as m;'
  
  mycursor.execute(sql)
  arrayMaquinas = mycursor.fetchall()
  mydb.commit()
  
  i = 0

  #converter os valores recebidos
  #arrumar o loop qnd a maquina nao tem dados
  
  print("\nMáquinas cadastradas no banco de dados:\n")
  while i < len(arrayMaquinas):
    idMaquina = arrayMaquinas[i][0]
    modeloMaquina = arrayMaquinas[i][1]
    fabricanteMaquina = arrayMaquinas[i][2]
    statusMaquina = arrayMaquinas[i][3]
    
    print(f"({idMaquina}, {modeloMaquina} - {fabricanteMaquina}, {statusMaquina})", )
    i+=1
    
  # Validação para garantir que o usuário escreveu um número que seja o ID de alguma as maquinas mostradas a ele
  while True:
    idSelecionado = int(input("\nDigite número -2 caso queira sair\nDigite o número de identificação para escolher a maquina: "))
    
    if idSelecionado == -2:
      idSelecionado = -2
      break
    
    try: 
      arrayMaquinas[idSelecionado - 1]
    except:
      print('Número de Identificação não existente\n')
    else:
      if arrayMaquinas[idSelecionado - 1][0] == idSelecionado:
        print('Número de Identificação existente\n')
        break
          
def exibirDados(idMaquina):

  if idMaquina == -1:
    return print("MAQUINA NÃO SELECIONADA")
  elif idMaquina == -2:
    return False

# VIEW CPU
  mycursor.execute("SELECT c.nome, cpu.porcentagemUso, cpu.tempoAtivoPorcentagem, cpu.tempoInativoPorcentagem, cpu.frequencia, cpu.tempoColeta from componente as c join processador as cpu on cpu.fkComponente = c.idComponente where fkMaquina = %s order by tempoColeta desc limit 1; ", [idMaquina])
  arrayCPU = mycursor.fetchall()
   
  # VIEW RAM
  mycursor.execute("SELECT c.nome, ram.capacidadeTotal, ram.capacidadeDisp, ram.porcentagemUso, ram.tempoColeta from componente as c join memoria as ram on ram.fkComponente = c.idComponente where fkMaquina = %s order by tempoColeta desc limit 1; ", [idMaquina])
  arrayRAM = mycursor.fetchall()  

  # VIEW BATERIA
  mycursor.execute("SELECT c.nome, bat.porcentagemAtual, bat.tempoColeta from componente as c join bateria as bat on bat.fkComponente = c.idComponente where fkMaquina = %s order by tempoColeta desc limit 1; ", [idMaquina])
  arrayBATERIA = mycursor.fetchall()

  mycursor.execute("SELECT c.nome, net.byteEnviado, net.tempoColeta from componente as c join redeChip as net on net.fkComponente = c.idComponente where fkMaquina = %s order by tempoColeta desc limit 1; ", [idMaquina])
  arrayREDE = mycursor.fetchall()

  mycursor.execute("SELECT c.nome, disco.capacidadeTotal, disco.capacidadeDisp, disco.tempoColeta     from componente as c join armazenamento as disco on disco.fkComponente = c.idComponente where fkMaquina = %s order by tempoColeta desc limit 1;", [idMaquina])
  arrayDISCO = mycursor.fetchall()
  
  mydb.commit()
  
  has_dataCPU = True
  has_dataRAM = True
  has_dataBATERIA = True
  has_dataREDE = True
  has_dataDISCO = True
  
  print(arrayDISCO)
  
  if len(arrayCPU) == 0:
    print('Sem dados de CPU para esta maquina')
    has_dataCPU = False

  if len(arrayRAM) == 0: 
    print('Sem dados de RAM para esta maquina')
    has_dataRAM = False

  if len(arrayBATERIA) == 0: 
    print('Sem dados de BATERIA para esta maquina')
    has_dataBATERIA = False

  if len(arrayREDE) == 0: 
    print('Sem dados de REDE para esta maquina')
    has_dataREDE = False

  if len(arrayDISCO) == 0:
    print('Sem dados de DISCO para esta maquina')
    has_dataDISCO = False
  
  # Mostrar dados CPU
  if has_dataCPU:
    cpu_nome = arrayCPU[0][0]
    cpu_porcentagemUso = arrayCPU[0][1]
    cpu_porcentagemAtivo = arrayCPU[0][2]
    cpu_porcentagemInativo = arrayCPU[0][3]
    cpu_frequencia = arrayCPU[0][4]
    cpu_tempoColeta = arrayCPU[0][5]
  
  # Mostrar dados RAM
  if has_dataRAM:
    ram_nome = arrayRAM[0][0]
    ram_capacidadeTotal = arrayRAM[0][1]
    ram_capacidadeDisp = arrayRAM[0][2]
    ram_porcentagemUso = arrayRAM[0][3]
    ram_tempoColeta = arrayRAM[0][4]
  
  # Mostrar dados BATERIA + REDE + DISCO
  if has_dataBATERIA:  
    bat_nome = arrayBATERIA[0][0]
    bat_porcentagemAtual = arrayBATERIA[0][1]
    bat_tempoColeta = arrayBATERIA[0][2]

  if has_dataREDE:
    rede_nome = arrayREDE[0][0]
    rede_byteEnviado = arrayREDE[0][1]
    rede_tempoColeta = arrayREDE[0][2]

  if has_dataDISCO:
    disco_nome = arrayDISCO[0][0]
    disco_capacidadeTotal = arrayDISCO[0][1]
    disco_capacidadeDisponivel = arrayDISCO[0][2]
    disco_tempoColeta = arrayDISCO[0][3]
  
  if has_dataCPU:
    print(f"""  
    {cpu_nome}
    <:---------------------------------------------------------:>
    | % USO - {cpu_porcentagemUso}              
    |                                  
    | % ATIVA - {cpu_porcentagemAtivo}           
    |                                  
    | % INATIVA - {cpu_porcentagemInativo}         
    |                                  
    | FREQUÊNCIA - {cpu_frequencia}                 
    |                                  
    | HORÁRIO DO REGISTRO - {cpu_tempoColeta}             
    <:---------------------------------------------------------:>""")
  
  if has_dataRAM:
    print(f"""
    {ram_nome}
    <:---------------------------------------------------------:>
    | % USO - {ram_porcentagemUso}             
    |                                  
    | CAPACIDADE TOTAL - {ram_capacidadeTotal}           
    |                                  
    | CAPACIDADE DISPONIVEL - {ram_capacidadeDisp}         
    |                                  
    | HORÁRIO DO REGISTRO - {ram_tempoColeta}             
    <:---------------------------------------------------------:>""")
  
  if has_dataBATERIA:
    print(f"""
    {bat_nome}
    <:---------------------------------------------------------:>
    | % ATUAL - {bat_porcentagemAtual}             
    |                                  
    | HORÁRIO DO REGISTRO - {bat_tempoColeta}           
    <:---------------------------------------------------------:>""")
  
  if has_dataREDE:
    print(f"""                                 
    {rede_nome}
    <:---------------------------------------------------------:>
    | CAPACIDADE DISPONIVEL - {rede_byteEnviado}         
    |                                  
    | HORÁRIO DO REGISTRO - {rede_tempoColeta}             
    <:---------------------------------------------------------:>""")
  
  if has_dataDISCO:
    print(f"""
    {disco_nome}
    <:---------------------------------------------------------:>
    | CAPACIDADE TOTAL - {disco_capacidadeTotal}           
    |                                  
    | CAPACIDADE DISPONIVEL - {disco_capacidadeDisponivel}         
    |                                  
    | HORÁRIO DO REGISTRO - {disco_tempoColeta}          
    <:---------------------------------------------------------:>\n\n""")
    
    return True

  

while True:
  listarMaquinas()
  retornoFuncao = exibirDados(idSelecionado)
  
  if not retornoFuncao:
    break
  
  time.sleep(2)
  


# Após a escolha deve mostrar os dados continuamente da maquina selecionada e ao apertar x deve re-aparecer as opcoes novamente