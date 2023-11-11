import sqlite3 as connect


##########CRIAR TABELA USUÁRIO###########
def criarTabelaUsuario():
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario('id' INTEGER PRIMARY KEY, 'nome' TEXT , 'senha' TEXT , log TEXT)''')
    conexao.commit()
    print("Tabela criada com sucesso!")
  except connect.Error as e:
    print(f"Erro ao conectar ao banco de dados!\nerro:{e}")
  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")

def inserir_log(log):
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuario(log) VALUES (?)''', ( log,))
    conexao.commit()
    print("log adicionado com sucesso!")
  except connect.Error as e:
    print(e)
    print(f"Erro ao conectar ao banco de dados!")
  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")


 
def inserirUsuario(nome, senha):
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuario(nome, senha) VALUES(?, ?)''', (nome, senha))
    conexao.commit()
  
  except connect.Error as e:
    print(f"Erro ao inserir dados!\nErro:{e}")

  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")




  
def selecionarUsuario():
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuario''')
    conexao.commit()
    lista = cursor.fetchall()
    return lista
  except connect.Error as e:
    print(f"Erro ao ler dados!\nErro:{e}")

  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")
  
  


  def editarUsuario(nome,senha):
    try:
      conexao = connect.connect("bd_catalogo.sqlite")
      cursor = conexao.cursor()
      cursor.execute('''UPDATE usuario SET nome = ?, senha = ? WHERE id = ?''', (nome, senha, id))
      conexao.commit()
      
    except connect.Error as e:
      print(f"Erro ao editar dados!\nErro:{e}")
    
    finally:
      cursor.close()
      conexao.close()
      print("Banco de dados desconectado com sucesso!!")



def excluriUsuario(id):
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM usuario WHERE id = ?''', (id,))
    conexao.commit()
    
  except connect.Error as e:
    print(f"Erro ao excluir dados!\nErro:{e}")

  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")




########CRIAOCAO TABELA CATALOGO########
def criarTabelaCatalogo():
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS catalogo('id' INTEGER PRIMARY KEY, 'titulo' TEXT ,'genero' TEXT,  'descricao' TEXT,'data_de_lancamento' TEXT)''')
    conexao.commit()
    print("Tabela criada com sucesso!")
  except connect.Error as e:
    print(f"Erro ao conectar ao banco de dados!\nerro:{e}")

  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")


def inserirFilme(titulo, genero, descricao, data_de_lancamento):
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO catalogo(titulo, genero, descricao, data_de_lancamento) VALUES(?, ?, ?, ?)''', (titulo, genero, descricao, data_de_lancamento))
    conexao.commit()
  
  except connect.Error as e:
    print(f"Erro ao inserir dados!\nErro:{e}")

  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")




def selecionarCatalogo():
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM catalogo''')
    conexao.commit()
    lista = cursor.fetchall()
    return lista
  except connect.Error as e:
    print(f"Erro ao ler dados!\nErro:{e}")

  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")




def editarCatalogo(id, titulo, genero, descricao, data_de_lancamento):
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''UPDATE catalogo SET titulo = ?, genero = ?, descricao = ?, data_de_lancamento = ? WHERE id = ?''', (titulo, genero, descricao, data_de_lancamento, id))
    conexao.commit()

  except connect.Error as e:
    print(f"Erro ao editar dados!\nErro:{e}")

  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")



def excluirCatalogo(id):
  try:
    conexao = connect.connect("bd_catalogo.sqlite")
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM catalogo WHERE id = ?''', (id,))
    conexao.commit()
    
  except connect.Error as e:
    print(f"Erro ao excluir dados!\nErro:{e}")

  finally:
    cursor.close()
    conexao.close()
    print("Banco de dados desconectado com sucesso!!")




  