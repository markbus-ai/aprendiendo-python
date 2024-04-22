
import qrcode
qr_link = input("ingresa el link del qr que quieras generar")

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(qr_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('qr.png')
