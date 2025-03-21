import time
import mysql.connector

mydb = mysql.connector.connect(
    host="34.207.88.160",
    user="sentinelaTestes",
    password="Sentinela@123",
    database="sentinela"
)
mycursor = mydb.cursor()

idSelecionado = None

def listarMaquinas():
    global idSelecionado
    
    sql = 'SELECT m.idMaquina, m.status, m.setor, m.serial, f.nomeModelo FROM maquina AS m JOIN modelo AS f ON m.fkModelo = f.idModelo;'

    try:
        mycursor.execute(sql)
        arrayMaquinas = mycursor.fetchall()
        mydb.commit()
        
        if len(arrayMaquinas) == 0:
            print("Nenhuma máquina cadastrada no banco de dados.")
            return
        
        i = 0
        print("\nMáquinas cadastradas no banco de dados:\n")
        while i < len(arrayMaquinas):
            idMaquina = arrayMaquinas[i][0]
            statusMaquina = arrayMaquinas[i][1]
            setorMaquina = arrayMaquinas[i][2]
            serialMaquina = arrayMaquinas[i][3]
            modeloMaquina = arrayMaquinas[i][4]
            
            print(f"({idMaquina}) {modeloMaquina} - {statusMaquina} - Setor: {setorMaquina} - Serial: {serialMaquina}")
            i += 1
        
        while True:
            try:
                idSelecionado = int(input("\nDigite número -2 caso queira sair\nDigite o número de identificação para escolher a máquina: "))
                
                if idSelecionado == -2:
                    idSelecionado = -2
                    break
                
                if idSelecionado < 1 or idSelecionado > len(arrayMaquinas):
                    print("Número de Identificação não existente. Tente novamente.\n")
                else:
                    print(f'Máquina {idSelecionado} selecionada.')
                    break
            except ValueError:
                print("Por favor, insira um número válido.")
    except mysql.connector.Error as err:
        print(f"Erro na execução da consulta SQL: {err}")
        mydb.rollback()

def exibirDados(idMaquina):
    if idMaquina == -1:
        print("MAQUINA NÃO SELECIONADA")
        return  
    elif idMaquina == -2:
        return -2

    # Tempo Ativo da CPU
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 1 AND t.idTipo = 1
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    tempoAtivoCPU = mycursor.fetchall()

    # Tempo Inativo da CPU
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 1 AND t.idTipo = 2
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    tempoInativoCPU = mycursor.fetchall()

    # Uso da CPU
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 1 AND t.idTipo = 3
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    usoCPU = mycursor.fetchall()

    # Frequência da CPU
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 1 AND t.idTipo = 4
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    frequenciaCPU = mycursor.fetchall()

    # Memória Disponivel
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 2 AND t.idTipo = 5
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    MemDispRAM = mycursor.fetchall()

    #Memória Utilizada em porcentagem
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 2 AND t.idTipo = 6
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    MemUtilRAM = mycursor.fetchall()

    #Memória Não utilizada
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 2 AND t.idTipo = 7
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    MemNaoUtilRAM = mycursor.fetchall()

    #Memória Total
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 2 AND t.idTipo = 8
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    MemTotalRAM = mycursor.fetchall()

    # Bateria
    #mycursor.execute("""
    #    SELECT c.nome, d.valor, d.tempoColeta 
    #    FROM dados AS d
    #    JOIN tipo AS t ON t.idTipo = d.fkTipo
    #    JOIN componente AS c ON c.idComponente = t.fkComponente
    #    WHERE c.fkMaquina = %s AND t.fkComponente = 3 AND t.idTipo = 9
    #    ORDER BY d.tempoColeta DESC;
    #""", (idMaquina,))
    #BateriaBAT = mycursor.fetchall()

    # Rede
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 4 AND t.idTipo = 10
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    BytesEnviadosBYTES = mycursor.fetchall()

    #Armazenamento
    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 5 AND t.idTipo = 11
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    DiscoDispDISCO = mycursor.fetchall()


    mycursor.execute("""
        SELECT c.nome, d.valor, d.tempoColeta 
        FROM dados AS d
        JOIN tipo AS t ON t.idTipo = d.fkTipo
        JOIN componente AS c ON c.idComponente = t.fkComponente
        WHERE c.fkMaquina = %s AND t.fkComponente = 5 AND t.idTipo = 12
        ORDER BY d.tempoColeta DESC;
    """, (idMaquina,))
    DiscoTotalDISCO = mycursor.fetchall()

    # Pegando os valores mais recentes para cada tipo de dado (da posição 0, que é o mais recente)
    tempoAtivo = tempoAtivoCPU[0][1] 
    tempoInativo = tempoInativoCPU[0][1]  
    uso = usoCPU[0][1]  
    frequencia = frequenciaCPU[0][1] 
    MemDisp = MemDispRAM[0][1]
    MemUtil = MemUtilRAM[0][1]
    MemNaoUtil = MemNaoUtilRAM[0][1]
    MemTotal = MemTotalRAM[0][1]
#    Bateria = BateriaBAT[0][1]
    BytesEnviados = BytesEnviadosBYTES[0][1]
    DiscoDisp = DiscoDispDISCO[0][1]
    DiscoTotal = DiscoTotalDISCO[0][1]
    horarioRegistro = usoCPU[0][2]  

    print(f"""
    {usoCPU[0][0]}  #(CPU)
    <:---------------------------------------------------------:>
    | Tempo Ativo: {tempoAtivo}                 
    | Tempo Inativo: {tempoInativo}               
    | % de Uso: {uso}               
    | Frequência: {frequencia}                 
    | Horário do Registro: {horarioRegistro}              
    <:---------------------------------------------------------:>
    <:---------------------------------------------------------:>
    | Memória Disponivel: {MemDisp / 1024**3:.2f} GB            
    | Memória Utilizada: {MemUtil} %               
    | Memória Não Utilizada: {MemNaoUtil / 1024**3:.2f} GB               
    | Memória Total: {MemTotal / 1024**3:.2f} GB                 
    | Horário do Registro: {horarioRegistro}              
    <:---------------------------------------------------------:>
    <:---------------------------------------------------------:>
    | Bytes em porcentagem: {BytesEnviados:.0f}                
    | Horário do Registro: {horarioRegistro}              
    <:---------------------------------------------------------:>
    <:---------------------------------------------------------:>
    | Armazenamento Disponivel em Bytes: {DiscoDisp} TB
    | Armazenamento Total: {DiscoTotal} TB               
    | Horário do Registro: {horarioRegistro}              
    <:---------------------------------------------------------:>
    
    """)

    return True

while True:
    listarMaquinas()
    if idSelecionado == -2:
        break
    
    retornoFuncao = exibirDados(idSelecionado)
    
    if retornoFuncao == -2:
        break
    
    time.sleep(5)
