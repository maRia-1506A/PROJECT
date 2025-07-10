import qrcode
info = input("Enter the text or URL for the Qr code: ").strip()  # remove space
file = input("Enter the filename: ").strip()  # remove space

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(info)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file)

print(f"QR code saved as {file}")
