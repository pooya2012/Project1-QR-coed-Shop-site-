#import Library
import qrcode
import random

#random name QR
QR_TOKEN = random.randint(1,50000)

QR_CODE = qrcode.make(
    f'{QR_TOKEN}'
)

#save QR
QR_CODE.save(f'{QR_TOKEN}.png')

#print token
print(QR_TOKEN)

#the end of code
QR_CODE.show()
