
def centralizar_janela(width, height, janela):
 
  screen_width = janela.winfo_screenwidth()
  screen_height = janela.winfo_screenheight()
  x=int((screen_width/2)-(width/2))
  y=int((screen_height/2)-(height/2))
  #janela = "%dx%d+%d+%d" % (width, height, x, y
  return f"{width}x{height}+{x}+{y}"
  