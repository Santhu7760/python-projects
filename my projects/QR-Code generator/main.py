import qrcode
import qrcode.constants

qr=qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2
)

qr.add_data("hello di!") #add your own URL here
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="black")
img.save("image.png")
