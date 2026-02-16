import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar
# pyautogui.write -> escrever
# pyautogui.press -> pressionar
# pyautogui.hotkey -> combinação de teclas

# passo 1 entrar no sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# passo 2 fazer login
pyautogui.click(x=649, y=477) # clicar no campo usuario
pyautogui.write("SEUEMAIL@email.com")
pyautogui.press("tab") # clicar no campo senha
pyautogui.write("SUASENHA")
pyautogui.write("tab")
pyautogui.press("enter")
time.sleep(3)

# passo 3 importar a base de dados
#pandas
tabela = pandas.read_csv("produtos.csv")
print (tabela)


# passo 4 cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=613, y=328) # clicar no botao novo produto

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o proximo campo

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab") # passar para o proximo campo

    tipo =  tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab") # passar para o proximo campo

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab") # passar para o proximo campo

    preco_unitario =  str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab") # passar para o proximo campo

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab") # passar para o proximo campo

    obs = str(tabela.loc[linha, "obs"])
    
    
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # passar para o proximo campo
    pyautogui.press("enter")

    pyautogui.scroll(19999) # rolar a tela para cima


# passo 5 repetir para todos os produtos

# pyautogui foi feito para fazer automações de tarefas repetitivas no python 
# controla o mouse e o teclado