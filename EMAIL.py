import smtplib
conn=smtplib.SMTP('smtp.gmail.com',587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('babhulkarpurva@gmail.com','ppu')
conn.sendmail('babhulkarpurva@gmail.com','babhulkarpurva@gmail.com','Subject: AND THE EMAIL JUT GOT SEND REALLY\n\nDear Purva !!HOPE YOU ARE DOING WELL ALL THE VERY BEST!!')
