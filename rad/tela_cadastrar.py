import tkinter as tk
from tkinter import  messagebox
from funcoes_auxiliares import centralizar_janela
import Banco_de_dados as bd
#classe tela de cadastro
class Tela_cadastro:

  def __init__(self, janela, tree):
  
    
    self.janela = tk.Toplevel(janela)
    self.janela.configure(bg="#F5F5F5")   
    self.janela.geometry(centralizar_janela( 400, 300,self.janela))

    self.janela.title("Catalogo de filmes")
    
    self.treeview = tree # variavel que recebe o treeview
    
    self.lb_titulo_janela = tk.Label(
        self.janela,
        text="Tela de cadastro",
        font=("Arial", "10", "bold"),
        bg="#4192F0",
        fg="white" 
    )
    self.lb_titulo_janela.grid(row=1, column=0, padx=10, pady=10)
    self.lb_titulo = tk.Label( self.janela,
                             text="Título: ",
                             font=("Arial", "10", "bold"),bg="#F5F5F5")
    self.lb_titulo.grid(row=4, column=0, pady=10)

  
    self.campo_titulo = tk.Entry(self.janela, width=10,
       font=("Arial", "10"))
    self.campo_titulo.grid(row=4, column=2, pady=5)
    

    self.lb_genero = tk.Label( self.janela,
                             text="Gênero: ",
                             font=("Arial", "10", "bold"),bg="#F5F5F5")
    self.lb_genero.grid(row=10, column=0, pady=10)


    self.campo_genero = tk.Entry(self.janela, width=10,
       font=("Arial", "10"))
    self.campo_genero.grid(row=10, column=2, pady=5)

    self.lb_descricao = tk.Label( self.janela,
                             text="Descrição: ",
                             font=("Arial", "10", "bold"),bg="#F5F5F5")
    self.lb_descricao.grid(row=15, column=0, pady=10)


    self.campo_descricao = tk.Text(self.janela, width=10,height=5,
       font=("Arial", "10"))
    self.campo_descricao.grid(row=15, column=2, pady=5)

    self.lb_data = tk.Label( self.janela,
                             text="Data de lançamento: ",
                             font=("Arial", "10", "bold"),bg="#F5F5F5")
    self.lb_data.grid(row=20, column=0, pady=10, padx=5)


    self.campo_data = tk.Entry(self.janela, width=10,
       font=("Arial", "10"))
    self.campo_data.grid(row=20, column=2, pady=5)
    
    self.btn_cadastrar = tk.Button( self.janela,
                                    text="cadastrar",
                                    font=("Arial", "10", "bold"), bg="blue",fg="white",command=self.cadastrar_filme).grid(row=20, column=7,pady=5, padx=10)
    
    self.btn_cancelar = tk.Button( self.janela,
    text="cancelar",
    font=("Arial", "10", "bold"), bg="red",fg="white",command=self.janela.destroy).grid(row=21, column=7,pady=5, padx=10)

#metodos da classe tela de cadastro
  
  def cadastrar_filme(self): #cadastrar filme
    try:
      titulo = self.campo_titulo.get()
      genero = self.campo_genero.get()
      descricao = self.campo_descricao.get("1.0", "end")
      data = self.campo_data.get()
      bd.criarTabelaCatalogo()
      if titulo == "" or genero == "" or descricao == "" or data == "":
        alerta = messagebox.showinfo(
          title="Alerta", message="Preencha todos os campos")
      else:
       
        lista_filmes = bd.selecionarCatalogo()
        lista = []
        for linha in lista_filmes:
            lista.append(linha[1])
            print(lista)
        if titulo in lista:
         
          self.campo_titulo.delete(0, "end")
          self.campo_genero.delete(0, "end")
          self.campo_descricao.delete(1.0, "end")
          self.campo_data.delete(0, "end")
          alerta = messagebox.showinfo(title="Alerta", message="filme já cadastrado!")
          
        else:
          bd.inserirFilme(titulo, genero, descricao, data)     
          alerta = messagebox.showinfo(title="Alerta", message="filme cadastrado com sucesso!")
          print(lista)
          self.treeview.delete(*self.treeview.get_children())
          lista_filmes = bd.selecionarCatalogo()
          
          for linha in lista_filmes: #atualiza a treeview
              self.treeview.insert('', 'end', values=linha)
          self.janela.destroy()

          with open("log.txt" , "a") as log:
            log.write(f"cadastrou o filme {titulo} \n")

        
    except Exception as e:
        print(f"erro: {e}")
                            
                                                                                           
   