import pyautogui
import time
#Zoom: 100%

#entrar no chrome
pyautogui.press('win')
pyautogui.write('Google Chrome')
pyautogui.press('enter')
time.sleep(1)

#entrar no site
pyautogui.write('https://siap.educacao.go.gov.br/')
pyautogui.press('enter')
time.sleep(5)

#logar
pyautogui.write('Login') #inserir o loguin quando for executar
pyautogui.press('tab')
pyautogui.write('Senha') #inserir a senha quando for executar
pyautogui.click(x=1234, y=594)
pyautogui.click(x=1234, y=594)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(x=1132, y=684)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(10)

#entrar em Planejamento do Professor
pyautogui.click(x=518, y=139) #menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268) #acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)

#entrar em 1 mês antes
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=1154, y=668)
time.sleep(3)
pyautogui.press('end')
time.sleep(4)

#Entrar na primeira aula de matemática e replicá-los
pyautogui.click(x=615, y=757)
time.sleep(10)
for c in range (20):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

#voltar para as aulas e ir em 1 mês antes
pyautogui.click(x=518, y=139) #menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268) #acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=1154, y=668)
time.sleep(3)
pyautogui.press('end') #somente p matemática e português
time.sleep(3)

#Entrar na primeira aula de português e replicá-los
pyautogui.click(x=617, y=655)
time.sleep(10)
for c in range (20):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

#voltar para as aulas e ir em 1 mês antes
pyautogui.click(x=518, y=139) #menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268) #acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up') #seleciona o mês de cima (anterior)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=1154, y=668)
time.sleep(3)
pyautogui.press('end') #somente p matemática e português
time.sleep(3)

#Entrar na primeira aula de inglês e replicá-los
pyautogui.click(x=613, y=565)
time.sleep(10)
for c in range (5):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

#voltar para as aulas e ir em 1 mês antes
pyautogui.click(x=518, y=139) #menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268) #acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up') #seleciona o mês de cima (anterior)
pyautogui.press('enter')
time.sleep(5)

#Entrar na primeira aula de História e replicá-los
pyautogui.click(x=612, y=867)
time.sleep(10)
for c in range (12):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

#voltar para as aulas e ir em 1 mês antes
pyautogui.click(x=518, y=139) #menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268) #acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up') #seleciona o mês de cima (anterior)
pyautogui.press('enter')
time.sleep(5)

#Entrar na primeira aula de Geografia e replicá-los
pyautogui.click(x=614, y=772)
time.sleep(10)
for c in range (12):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

#voltar para as aulas e ir em 1 mês antes
pyautogui.click(x=518, y=139) #menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268) #acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up') #seleciona o mês de cima (anterior)
pyautogui.press('enter')
time.sleep(5)

#Entrar na primeira aula de Ensino Religioso e replicá-los
pyautogui.click(x=613, y=676)
time.sleep(6)
for c in range (12):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

# voltar para as aulas e ir em 1 mês antes
pyautogui.click(x=518, y=139)  # menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268)  # acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up')  # seleciona o mês de cima (anterior)
pyautogui.press('enter')
time.sleep(5)

#Entrar na primeira aula de Educação Física e replicá-los
pyautogui.click(x=618, y=584)
time.sleep(6)
for c in range (12):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

# voltar para as aulas e ir em 1 mês antes
pyautogui.click(x=518, y=139)  # menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268)  # acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up')  # seleciona o mês de cima (anterior)
pyautogui.press('enter')
time.sleep(5)

#Entrar na primeira aula de Ciências e replicá-los
pyautogui.click(x=619, y=489)
time.sleep(6)
for c in range (15):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

# voltar para as aulas e ir em 1 mês antes
pyautogui.click(x=518, y=139)  # menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268)  # acompanhamento planejamento do professor
pyautogui.click(x=907, y=268)
time.sleep(5)
pyautogui.click(x=580, y=305)
time.sleep(3)
pyautogui.press('up')  # seleciona o mês de cima (anterior)
pyautogui.press('enter')
time.sleep(5)

# Entrar na primeira aula de Arte e replicá-los
pyautogui.click(x=616, y=392)
time.sleep(6)
for c in range(6):
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    time.sleep(4)
    pyautogui.click(x=696, y=892)  # Replicar
    time.sleep(1)
    pyautogui.click(x=880, y=627)  # Confirmar
    time.sleep(5)
    pyautogui.press('end')
    time.sleep(2)
    pyautogui.press('end')
    pyautogui.click(x=962, y=887)  # Salvar e próximo
    pyautogui.click(x=962, y=887)
    time.sleep(8)

# Encerramento do programa
pyautogui.click(x=518, y=139)  # menu de sistema
time.sleep(3)
pyautogui.click(x=907, y=268)  # acompanhamento planejamento do professor
