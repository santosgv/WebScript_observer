from email.message import EmailMessage
import smtplib

def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to

    user='aurora.alerta@outlook.com.br' # urora.alerta@outlook.com.br //Patrus2020!
    password='jsyygpavmvwnrywf'# gmail'llcqbkxainwmrzvt'
    msg['from'] = user

    server=smtplib.SMTP('smtp.office365.com',587) ## Para enviar do Outlok precisa liberar o acesso da conta (smtp.gmail.com',587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()
