import tkinter as tk
from tkinter import  messagebox
from funcoes_auxiliares import centralizar_janela
import Banco_de_dados as bd
#classe tela de edição
class Tela_edicao:

  def __init__(self, janela, tree, id, titulo, genero, descricao, data):
    self.id = id #variaves que recebem os valores dos campos
    self.titulo_var = tk.StringVar(value=titulo)
    self.genero_var = tk.StringVar(value=genero)
    self.descricao_var = descricao
    self.data_var = tk.StringVar(value=data)
    
    self.janela = tk.Toplevel(janela)
    self.janela.configure(bg="#F5F5F5") 
    self.janela.title("Catalogo de filmes")
    self.janela.geometry(centralizar_janela( 400, 300,self.janela))
    
    self.treeview = tree
   
    self.lb_titulo_janela = tk.Label(
        self.janela,
        text="Tela de edição",
        font=("Arial", "10", "bold"),
        bg="#4192F0",
        fg="white" 
    )
    self.lb_titulo_janela.grid(row=1, column=0, padx=10, pady=10)
    self.lb_titulo = tk.Label( self.janela,
                             text="Título: ",
                             font=("Arial", "10", "bold"),bg="#F5F5F5")
    self.lb_titulo.grid(row=4, column=0, pady=10)


    self.campo_titulo = tk.Entry(self.janela,textvariable=self.titulo_var, width=10,
       font=("Arial", "10"))
    self.campo_titulo.grid(row=4, column=2, pady=5)


    self.lb_genero = tk.Label( self.janela,
                             text="Gênero: ",
                             font=("Arial", "10", "bold"),bg="#F5F5F5")
    self.lb_genero.grid(row=10, column=0, pady=10)


    self.campo_genero = tk.Entry(self.janela, width=10,textvariable=self.genero_var,
       font=("Arial", "10"))
    self.campo_genero.grid(row=10, column=2, pady=5)

    self.lb_descricao = tk.Label( self.janela,
                             text="Descrição: ",
                             font=("Arial", "10", "bold"),bg="#F5F5F5")
    self.lb_descricao.grid(row=15, column=0, pady=10)


    self.campo_descricao = tk.Text(self.janela, width=10,height=5,
       font=("Arial", "10"))
    self.campo_descricao.grid(row=15, column=2, pady=5)
    self.campo_descricao.insert('1.0', self.descricao_var)

    self.lb_data = tk.Label( self.janela,
                             text="Data de lançamento: ",
                             font=("Arial", "10", "bold"),bg="#F5F5F5")
    self.lb_data.grid(row=20, column=0, pady=10, padx=5)


    self.campo_data = tk.Entry(self.janela, width=10, textvariable=self.data_var,
       font=("Arial", "10"))
    self.campo_data.grid(row=20, column=2, pady=5)

    self.btn_editar = tk.Button( self.janela,
                                    text="editar",
                                    font=("Arial", "10", "bold"), bg="blue",fg="white",command=self.editar_filme).grid(row=20, column=7,pady=5, padx=10)

    self.btn_cancelar = tk.Button( self.janela,
    text="cancelar",
    font=("Arial", "10", "bold"), bg="red",fg="white",command=self.janela.destroy).grid(row=21, column=7,pady=5, padx=10)


#####métodos da tela de edição
  def editar_filme(self): #editar filme
    try:
      bd.editarCatalogo(self.id, self.titulo_var.get(), self.genero_var.get(), self.campo_descricao.get('1.0', 'end-1c'), self.data_var.get())
      with open("log.txt" , "a") as log:
        log.write(f"editou o filme {self.titulo_var.get()} \n")
 
      print(bd.selecionarCatalogo())
      alerta = messagebox.showinfo(
          title="Alerta", message="Filme atualizado com sucesso!!")
      self.treeview.delete(*self.treeview.get_children())
      lista_filmes = bd.selecionarCatalogo()
      for linha in lista_filmes: #atualiza a tree
          self.treeview.insert('', 'end', values=linha)
      self.janela.destroy()
    except Exception as e:
      print(f"erro: {e}")
      alerta = messagebox.showerror(
            title="Alerta", message="Erro ao editar filme")
        
