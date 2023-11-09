# This line is a Python import statement. The "qrcode" library is a Python module that allows you to generate QR(Quick Response) code.
import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=5)

qr.add_data("https://twitter.com/rohitrajput31")

qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")

img.save("image.png")
