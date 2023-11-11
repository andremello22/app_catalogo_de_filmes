import tkinter as tk
from tkinter import messagebox
import Banco_de_dados as bd
from funcoes_auxiliares import centralizar_janela
#classe tela de cadastro de usuários
class TelaDeCriacaoDeUsuario:

  def __init__(self, janela):
    self.janela = tk.Toplevel(janela)
    self.janela.configure(bg="#F5F5F5")
    self.janela.title("Catalogo de filmes")
    self.janela.geometry(centralizar_janela(400, 300, self.janela))

    self.lb_titulo = tk.Label(
        self.janela,
        text=" Tela de criação de usuário ",
        font=("Arial", "10", "bold"),
        bg="#4192F0",
        fg="white",
    ).grid(row=0, column=2, pady="10")

   

    self.lb_nome = tk.Label(self.janela,
                            text="Nome: ",
                            font=("Arial", "10"),
                            bg="#F5F5F5").grid(row=2, column=0, padx=5, pady=5)

    self.campo_nome_cadastro = tk.Entry(self.janela, width=20,
                               font=("Arial", "15"))
    self.campo_nome_cadastro.grid(row=2, column=2)

    self.lb_senha = tk.Label(self.janela, text="Senha: ",
                             bg="#F5F5F5").grid(row=6, column=0, padx=10)

    self.campo_senha_cadastro = tk.Entry(self.janela, width=20,
                               font=("Arial", "15"))
    self.campo_senha_cadastro.grid(row=6,column=2,pady=5)


    self.btn_cradastrar = tk.Button(self.janela,
                               text="Cadastrar usuário",
                               font=("Arial", "10", "bold"),
                               bg="#005F3C",
                               fg="white",
                               command=self.criar_usuario).grid(row=10, column=2, pady=5)


    self.btn_voltar = tk.Button(self.janela,
       text="voltar",
       font=("Arial", "10", "bold"),
       bg="#e6b800",
       fg="white",
       command=self.voltar).grid(row=12, column=2, pady=5)



    self.lb_mensagem = tk.Label(self.janela,
                                text="",
                                font=("Arial", "10"),
                                bg="#F5F5F5")
    self.lb_mensagem.grid(row=14, column=2, pady=5)






  ##################métodos tela de criação de usuário########

  def criar_usuario(self): #criar usuário
    try:
      
      nome = self.campo_nome_cadastro.get()
      senha = self.campo_senha_cadastro.get()
      bd.criarTabelaUsuario()
      lista_de_usuario = bd.selecionarUsuario()

      lista=[]
      for linha in lista_de_usuario:
        print(linha[1])
        lista.append(linha[1] ) 
      if nome == "" or senha == "":
        alerta = messagebox.showinfo(
        title="Alerta", message="Preencha todos os campos")
      elif nome in lista:
        self.campo_nome_cadastro.delete(0, "end")
        self.campo_senha_cadastro.delete(0, "end")
        alerta = messagebox.showinfo(title="Alerta", message="Usuário já cadastrado!")

      else:
       
        bd.inserirUsuario(nome,senha)
        self.lb_mensagem.config(text="Usuário cadastrado com sucesso")

        alerta = messagebox.showinfo(
          title="Alerta", message="usuario cadastrado com sucesso!!")
        print(lista_de_usuario)
        self.janela.destroy()
       
    except Exception as e:
      alerta = messagebox.showinfo(title="Alerta", message="Erro ao cadastra usuario, tente novamente mais tarde")
      print(f"erro:{e}")


  def voltar(self): #voltar para tela de login
    try:
      
      self.janela.destroy()
      
    except Exception as e:
      print(f"erro:{e}")



