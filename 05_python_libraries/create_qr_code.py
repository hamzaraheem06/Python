import qrcode as qc

website_link = input("Enter your destination link: ")

version = int(input("Enter version number (Size of the image 1-40): "))
box_size = int(input("Enter the box size: "))
border = int(input("Enter border length: "))

qr = qc.QRCode(version=version, box_size=box_size, border=border)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = "black", back_color = "white")

img.save("generate_qr.png")