import ssl
import qrcode
import datetime

dt_now = datetime.datetime.now()
img = qrcode.make(dt_now) 
img.save('qrcode.png')