from email.mime.multipart import MIMEMultipart  # MIME stands for multipurpose internet mail extensions
from email.mime.text import MIMEText
import smtplib
from pathlib import Path
from email.mime.image import MIMEImage

message = MIMEMultipart()
message['from'] = 'meimportaunbledo123@hotmail.com'
message['to'] = 'keltoum@labgeni.us'
message['subject'] = 'This is a test'
message.attach(MIMEText('''Hola Kellycita! 
Aprendi a enviar e-mails usando Python!

''', 'html'))
message.attach(MIMEImage(Path('Joelito.jpg').read_bytes()))

with smtplib.SMTP(host="smtp.live.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('meimportaunbledo123@hotmail.com', 'megustalasalsa123')
    smtp.send_message(message)
    print('sent')
