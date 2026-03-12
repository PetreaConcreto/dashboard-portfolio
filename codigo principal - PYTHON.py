import pyautogui
import time

pyautogui.PAUSE = 1

# abrir o navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# entrar no site da hashtag

pyautogui.write("hashtagtreinamentos.com/curso-python")
pyautogui.press("enter")

time.sleep(5)

# preencher formulário

pyautogui.click(x=1132, y=801)
pyautogui.write("Guilherme Jeronimo")
pyautogui.click(x=1117, y=882)
pyautogui.write("guilhermej.jeronimo@gmail.com")
pyautogui.click(x=1156, y=953)
pyautogui.write("14 991097985")

# enviar formulário

pyautogui.press("tab")
pyautogui.press("enter")

#pos = pyautogui.locateCenterOnScreen("botao1.png")
#if pos is None:
#    raise Exception("Não encontrei o botão na tela. Verifique se ele está visível e igual ao PNG.")
#pyautogui.click(pos)