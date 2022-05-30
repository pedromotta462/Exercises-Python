import time
from senha import senha
import smtplib
import email.message
import random

def enviaremail(temperatura): 
    horario = time.asctime()
    corpoemail = f""""
    <p>ALERTA DE TEMPERATURA</p>
    <p>ATENÇÃO!! A temperatura está em {temperatura}°C </p>
    <p>{horario}</p>
    """
    msg = email.message.Message()
    msg['Subject'] =  "ALERTA DE TEMPERATURA"
    msg['From'] = 'pedromotta1d2015@gmail.com' #email que está enviando
    msg['To'] = 'pedro.motta@ufpe.br' #email que irá receber
    password = senha #importei de um arquivo senha.py na mesma pasta que este, onde tem senha = "senha da conta"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpoemail) #Seta o conteudo principal do email
    
    s = smtplib.SMTP('smtp.gmail.com: 587') #conecção segura com o servidor
    s.starttls()
    # Loga no email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8')) #envia o email
    print('Email enviado')

temp = random.randrange(1,100)
print("A temperatura da máquina está em:",temp,"°C" )

if temp > 40:
    print("Enviando alerta...")
    enviaremail(temp)
else:
    print("Valores normais de temperatura...")