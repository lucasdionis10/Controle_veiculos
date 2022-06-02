import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pass',
    database = 'controle_veículos',
)

cursor = conexao.cursor()





#Motoristas
#Create

#Nome = "José Carlos"
#Telefone = 14912345678
#CNH = 123456748
#Cria_motorista = f'INSERT INTO cadastro_motoristas(Nome, Telefone, CNH) VALUES ("{Nome}", {Telefone}, {CNH})'
#cursor.execute(Cria_motorista)
#conexao.commit()


#Read

#Leitura_motoristas = f'SELECT * FROM cadastro_motoristas;'
#cursor.execute(Leitura_veiculos)
#resultado_leitura_motoristas = cursor.fetchall()
#print(resultado_leitura_motoristas)


#Update

#Nome_alterar="José"
#Novo_nome = "Carlos Alberto"
#Telefone_alterar = 14912345678
#Novo_telefone = 14987654321
#CNH_alterar = 1234567891
#Novo_CNH = 1234585684

#Altera_motorista = f'UPDATE cadastro_motoristas SET Nome = "{Novo_nome}" WHERE Nome = "{Nome_alterar}"';
#Altera_telefone = f'UPDATE cadastro_motoristas SET Telefone = {Novo_telefone} WHERE Telefone = {Telefone_alterar}';
#Altera_CNH = f'UPDATE cadastro_motoristas SET CNH = {Novo_CNH} WHERE CNH = {CNH_alterar}';

#cursor.execute(Altera_motorista)
#cursor.execute(Altera_telefone)
#cursor.execute(Altera_CNH)
#conexao.commit()


#Delete

#Nome_deletar="Carlos Alberto"
#Delete_motorista = f'DELETE FROM cadastro_motoristas WHERE Nome = "{Nome_deletar}"';

#cursor.execute(Delete_motorista)
#conexao.commit()

#_______________________Veículos________________________________

#Veículos
#Create

#Placa = "luc45"
#Marca = "Mazda"
#Veiculo = "RX7"
#Km_troca_oleo = 18
#Cria_veiculo = f'INSERT INTO cadastro_veiculos(Placa, Marca, Veiculo, Km_troca_oleo) VALUES ("{Placa}", "{Marca}", "{Veiculo}", {Km_troca_oleo})'
#cursor.execute(Cria_veiculo)
#conexao.commit()


#Read

#Leitura_veiculos = f'SELECT * FROM cadastro_veiculos;'
#cursor.execute(Leitura_veiculos)
#resultado_leitura_veiculos = cursor.fetchall()
#print(resultado_leitura_veiculos)


#Update

#Placa_alterar= "luc45"
#Nova_placa = "FERA55"
#Marca_alterar = "Mazda"
#Nova_marca = "Ford"
#Veiculo_alterar = "RX7"
#Novo_veiculo = "Mustang"
#Km_oleo_alterar = 18
#Novo_km_oleo = 20

#Altera_placa = f'UPDATE cadastro_veiculos SET Placa = "{Nova_placa}" WHERE Placa = "{Placa_alterar}"';
#Altera_marca = f'UPDATE cadastro_veiculos SET Marca = "{Nova_marca}" WHERE Marca = "{Marca_alterar}"';
#Altera_veiculo = f'UPDATE cadastro_veiculos SET Veiculo = "{Novo_veiculo}" WHERE Veiculo = "{Veiculo_alterar}"';
#Altera_km_oleo = f'UPDATE cadastro_veiculos SET Km_troca_oleo = {Novo_km_oleo} WHERE Km_troca_oleo = {Km_oleo_alterar}';

#cursor.execute(Altera_placa)
#cursor.execute(Altera_marca)
#cursosr.execute(Altera_veiculo)
#cursor.execute(Altera_km_oleo)
#conexao.commit()


#Delete

#Placa_Deletar="FERA55"
#Delete_veiculo = f'DELETE FROM cadastro_veiculos WHERE Placa = "{Placa_Deletar}"';

#cursor.execute(Delete_veiculo)
#conexao.commit()

#_______________________Controle________________________________

#Controle
#Create

#Veiculo = "Ferrari"
#Motorista = "José Carlos"
#Data_saida = "2021-12-30"
#Hora_saida = 134500
#Km_saida = 12
#Destino = "Manaus/AM"
#Data_retorno = "2021-12-31"
#Hora_retorno = 134500
#km_retorno = 40
#Km_percorrido = km_retorno - Km_saida


#Cria_controle = f'INSERT INTO controle(Veiculo, Motorista, Data_saida, Hora_saida, Km_saida, Destino, Data_retorno, Hora_retorno, km_retorno, Km_percorrido) VALUES ("{Veiculo}", "{Motorista}", "{Data_saida}", {Hora_saida}, {Km_saida}, "{Destino}", "{Data_retorno}", {Hora_retorno}, {km_retorno}, {Km_percorrido})'
#cursor.execute(Cria_controle)
#conexao.commit()


#Read

#Leitura_controle = f'SELECT * FROM controle;'
#cursor.execute(Leitura_controle)
#resultado_leitura_veiculos = cursor.fetchall()
#print(resultado_leitura_veiculos)


#Update

#Veiculo_alterar = "Ferrari"
#Novo_veiculo = "Mustang"
#Motorista_alterar = "José Carlos"
#Novo_motorista = "Alberto"
#Data_saida_alterar = "2021-12-30"
#Nova_data_saida = "2021-12-29"
#Hora_saida_alterar = 134500
#Nova_hora_saida = 145500
#Km_saida_alterar = 12
#Novo_km_saida = 14
#Destino_alterar = "Manaus/AM"
#Novo_destino = "Goiânia/GO"
#Data_retorno_alterar = "2021-12-31"
#Nova_data_retorno = "2022-01-14"
#Hora_retorno_alterar = 134500
#Nova_hora_retorno = 184800
#Km_retorno_alterar = 40
#Novo_km_retorno = 200
#Km_percorrido_alterar = Km_retorno_alterar - Km_saida_alterar
#Novo_Km_percorrido = Novo_km_retorno - Novo_km_saida



#Altera_veiculo = f'UPDATE controle SET Veiculo = "{Novo_veiculo}" WHERE Veiculo = "{Veiculo_alterar}"';
#Altera_motorista = f'UPDATE controle SET Motorista = "{Novo_motorista}" WHERE Motorista = "{Motorista_alterar}"';
#Altera_data_saida = f'UPDATE controle SET Data_saida = "{Nova_data_saida}" WHERE Data_saida = "{Data_saida_alterar}"';
#Altera_hora_saida = f'UPDATE controle SET Hora_saida = {Nova_hora_saida} WHERE Hora_saida = {Hora_saida_alterar}';
#Altera_km_saida = f'UPDATE controle SET Km_saida = {Novo_km_saida} WHERE Km_saida = "{Km_saida_alterar}"';
#Altera_destino = f'UPDATE controle SET Destino = "{Novo_destino}" WHERE Destino = "{Destino_alterar}"';
#Altera_data_retorno = f'UPDATE controle SET Data_retorno = "{Nova_data_retorno}" WHERE Data_retorno = "{Data_retorno_alterar}"';
#Altera_hora_retorno = f'UPDATE controle SET Hora_retorno = {Nova_hora_retorno} WHERE Hora_retorno = {Hora_retorno_alterar}';
#Altera_km_retorno = f'UPDATE controle SET Km_retorno = {Novo_km_retorno} WHERE Km_retorno = {Km_retorno_alterar}';
#Altera_km_percorrido = f'UPDATE controle SET Km_percorrido = {Novo_Km_percorrido} WHERE Km_percorrido = {Km_percorrido_alterar}';


#cursor.execute(Altera_veiculo)
#cursor.execute(Altera_motorista)
#cursor.execute(Altera_data_saida)
#cursor.execute(Altera_hora_saida)
#cursor.execute(Altera_km_saida)
#cursor.execute(Altera_destino)
#cursor.execute(Altera_data_retorno)
#cursor.execute(Altera_hora_retorno)
#cursor.execute(Altera_km_retorno)
#cursor.execute(Altera_km_percorrido)

#conexao.commit()



#Delete

#Id_deletar= 0
#Delete_id = f'DELETE FROM controle WHERE Id_log = "{Id_deletar}"';

#cursor.execute(Delete_id)
#conexao.commit()

#cursor.close()
#conexao.close()