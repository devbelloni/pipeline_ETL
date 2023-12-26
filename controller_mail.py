import smtplib
import email.message

class controller_mail():
    def __init__(self, mensagem, email):
        self.mensagem=mensagem
        self.email=email
    def enviar_email(self):
        corpo_email = f"""
        <p>{self.mensagem}</p>
        <br>
        <p>Atenciosamente,</p>
        <p>Seu gerente virtual.</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "Gerente Virtual - Banco A"
        msg['From'] = 'prof.belloni@gmail.com'
        msg['To'] = self.email
        password = 'secreto'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {self.email}')

