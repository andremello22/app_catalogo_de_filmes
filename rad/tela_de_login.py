import tkinter as tk
from tkinter import messagebox 
import Banco_de_dados as bd
from funcoes_auxiliares import centralizar_janela
############classe tela de login################
class TelaDeLogin():

  def __init__(self):

    self.janela = tk.Tk()
    self.janela.configure(bg="#F5F5F5")
    self.janela.title("Catalogo de filmes")
    self.janela.geometry(centralizar_janela(400, 300, self.janela))

    self.lb_titulo = tk.Label(
        self.janela,
        text=" Tela de Login ",
        font=("Arial", "20", "bold"),
        bg="#4192F0",
        fg="white",
    ).grid(row=0, column=2, pady="10")

     

    self.lb_nome = tk.Label(self.janela,
                            text="Usuário: ",
                            font=("Arial", "10"),
                            bg="#F5F5F5").grid(row=2, column=0, padx=5, pady=5)

    self.campo_nome = tk.Entry(self.janela, width=20,
                               font=("Arial", "15"))
    self.campo_nome.grid(row=2, column=2)
    
    self.lb_senha = tk.Label(self.janela, text="Senha: ",
                             bg="#F5F5F5").grid(row=6, column=0, padx=10)

    self.campo_senha = tk.Entry(self.janela, width=20,
                               font=("Arial", "15"), show="*")
    self.campo_senha.grid(row=6,
                                                          column=2,
                                                          pady=5)

    self.btn_login = tk.Button(self.janela,
                               text="Login",
                               font=("Arial", "10", "bold"),
                               bg="#00BAD6",
                               fg="white",
                               command=self.fazer_login).grid(row=10, column=2, pady=5)

    self.btn_criarConta = tk.Button(
        self.janela,
        text="Criar Conta",
        font=("Arial", "7", "bold"),
        bg="#F9F871",
        fg="#261ED6",
        command=self.mudar_tela_login_criacao_de_usuario).grid(row=11,
                                                               column=2,
                                                               pady=5)
    self.janela.mainloop()
   
  ###################metodos tela de login###################
  def mudar_tela_login_criacao_de_usuario(self):
    try:
      from tela_criacao_de_usuario import TelaDeCriacaoDeUsuario
      tela_de_criacao_usuario = TelaDeCriacaoDeUsuario(self.janela)
      tela_de_criacao_usuario.janela.grab_set()
      
    except Exception as e:
      alerta = messagebox.showinfo(
      title="Alerta", message="Erro ao criar conta, tente novamente")
      print(f"erro:{e}")

  

#fazer login
  def fazer_login(self):
    try:
      from tela_de_catalogo import TelaDeCatalogo
      nome = self.campo_nome.get()
      senha = self.campo_senha.get()
      lista_usuarios = bd.selecionarUsuario()
      estado_login = False
      if nome == "" or senha == "":
        alerta = messagebox.showinfo(
        title="Alerta", message="Preencha todos os campos")
      else:
         for linha in lista_usuarios:
            if not (linha[1] == nome and linha[2] == senha):
              estado_login = False
              continue
               
            else:
              estado_login = True
              break
              
              
         if estado_login:
            self.janela.destroy()
            tela_criacao_u = TelaDeCatalogo()
    
            #criando txt com o nome do usuário
            with open("log.txt" , "w") as log:
              log.write(f"{nome} logado \n")
            
      
         else: 
            self.campo_nome.delete(0, "end")
            self.campo_senha.delete(0, "end")
            alerta = messagebox.showerror(
              title="Alerta", message="Usuário ou senha inválidos")
            print("login erro")
    except Exception as e:
      print(f"erro: {e}")









 