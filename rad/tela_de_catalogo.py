import tkinter as tk
import os
from tkinter import ttk, messagebox
from funcoes_auxiliares import centralizar_janela
from tela_editar import Tela_edicao
from tela_cadastrar import Tela_cadastro
import Banco_de_dados as bd
##########classe tela de catálogo#########

class TelaDeCatalogo:
  
  def __init__(self):

  #atributos da janela
    self.janela = tk.Tk()
    self.janela.configure(bg="#F5F5F5")
    self.janela.title("Catalogo de filmes")
    self.janela.geometry(centralizar_janela(800, 600, self.janela))
    
    self.lb_titulo = tk.Label(
        self.janela,
        text=" Tela de Cátalogo ",
        font=("Arial", "10", "bold"),
        bg="#4192F0",
        fg="white",pady=20,
    ).grid(row=0, column=2, pady="10")
   


    ####frame treeview
    self.frame_treeview = tk.Frame(self.janela)
    self.frame_treeview.grid(row=3, column=2, pady=20, padx=40)
    ##configurações treeview
    self.tree = ttk.Treeview(self.frame_treeview, columns=('id', 'titulo', 'genero','descricao', 'data de lancamento'),show="headings")
    self.tree.column('id',minwidth=0,width=50)
    self.tree.column('titulo',minwidth=0,width=100)
    self.tree.column('genero',minwidth=0,width=100)
    self.tree.column('descricao',minwidth=0,width=200)
    self.tree.column('data de lancamento',minwidth=0,width=200)
    self.tree.heading(column='id',text='ID')
    self.tree.heading(column='titulo',text='Título')
    self.tree.heading(column='genero',text='Gênero')
    self.tree.heading(column='descricao',text='Descrição')
    self.tree.heading(column='data de lancamento',text='Data de Lançamento')
    self.tree.pack(side='left', fill='both', expand=True)
    #configuraçoes scrollbar
    self.scrollbar_vertical = ttk.Scrollbar(self.frame_treeview, orient="vertical", command=self.tree.yview)
    self.scrollbar_vertical.pack(side='right', fill='y')
    self.tree.configure(yscrollcommand=self.scrollbar_vertical.set)
    
    
    self.inserir_treeview()#inserir lista na tree view
    
    self.tree.bind("<<TreeviewSelect>>", self.selecionar_elementos)#criar evento para apartir da seleção capturar elementos



    self.frame_btn = tk.Frame(self.janela, bg="#F5F5F5", pady=20)
    self.frame_btn.grid(row=5, column=2, pady=10, padx=10)

    self.btn_cadastrar = tk.Button(self.frame_btn,
       text="cadastrar",
       font=("Arial", "10", "bold"),
       bg="blue",
       fg="white",
       command=self.mudar_para_tela_cadastrar).grid(row=1, column=1)

    self.btn_editar = tk.Button(master=self.frame_btn,
       text="Editar",
       font=("Arial", "10", "bold"),
       bg="#e6b800",
       fg="white",
       command=self.mudar_para_tela_editar).grid(row=1, column=2)

    self.btn_excluir = tk.Button(self.frame_btn,
       text="Excluir",
       font=("Arial", "10", "bold"),
       bg="red",
       fg="white",
       command=self.excluir).grid(row=1, column=3)

    self.btn_sair = tk.Button(self.frame_btn,
       text="Sair",
       font=("Arial", "10", "bold"),
       bg="green",
       fg="white",
       command=self.sair).grid(row=1, column=4)



 #######metodos da classe tela de catalogo

  def selecionar_elementos(self,event): #esse metodo captura os elentos atreavez da seleção
    filme_selecionado = self.tree.selection()
    item_tupla = ''
    for item in filme_selecionado:
      item_tupla = self.tree.item(item, 'values')
    
    return item_tupla
       
    
  
  def inserir_treeview(self): #esse método isere os elementos na treeview
    try:
      lista_filmes = bd.selecionarCatalogo()
      for linha in lista_filmes:
        self.tree.insert('', 'end', values=linha)
    except Exception as e:
      print(e)

  
  
  def mudar_para_tela_cadastrar(self): #mudar para tela de cadastro
    try:
      
      tela_cadastrar = Tela_cadastro(self.janela, self.tree)
      tela_cadastrar.janela.grab_set()
    except Exception as e:
     
      print(f"erro:{e}")


  
  def mudar_para_tela_editar(self): #mudar para tela de edição
    try:
      lista_filmes = self.selecionar_elementos(self)
      if not lista_filmes:
        lerta = messagebox.showinfo(title='alerta', message='selecione algum filme para editar!')
      else:
        tela_editar = Tela_edicao(self.janela, self.tree,lista_filmes[0],lista_filmes[1], lista_filmes[2], lista_filmes[3], lista_filmes[4])#inserindo elemento selecionado nos campos
        tela_editar.janela.grab_set()
        print(lista_filmes)
    except Exception as e:
      lerta = messagebox.showinfo(title='alerta', message='Erro ao tentar abrir janela de edição!!')
      print(f"erro:{e}")



  
  def excluir(self):
    try:
      lista_filmes = self.selecionar_elementos(self)
      if not lista_filmes:
        alerta = messagebox.showinfo(title='alerta', message='selecione algum filme para excluir!')
      else:
        mensagem = messagebox.askokcancel(title='Excluir', message='Deseja excluir o filme?')
      if mensagem:
        with open("log.txt" , "a") as log:
          log.write(f"excluiu o filme{lista_filmes[1]}")
          bd.excluirCatalogo(lista_filmes[0])
          self.tree.delete(*self.tree.get_children())
          lista_filmes = bd.selecionarCatalogo()
        for linha in lista_filmes:
            self.tree.insert('', 'end', values=linha)
          
    except Exception as e:
      print(e)


  def sair(self):
    try:
      with open("log.txt" , "a") as log:
        log.write("fez logof")
      with open("log.txt", "r") as log_file:
        log_str = log_file.read()
      bd.inserir_log(log_str)
      DIRETORIO_ABSOLUTO = os.path.abspath(os.path.dirname(__file__))
      diretorio_log = os.path.join(DIRETORIO_ABSOLUTO, "log.txt")
      os.remove(diretorio_log)
      print(bd.selecionarUsuario())
      self.janela.quit()
    except Exception as e:
      print(e)