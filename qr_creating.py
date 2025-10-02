import qrcode

website_url = "https://www.codedex.io/projects"

qr = qrcode.QRCode( version=1, box_size=5, border=5)
qr.add_data(website_url)
qr.make()

img=qr.make_image(fill_color="black", back_color="white" )
img.save("my_qr_code.png")

