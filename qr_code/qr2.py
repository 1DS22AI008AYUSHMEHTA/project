import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=5)
qr.add_data("https://en.wikipedia.org/wiki/2025_India%E2%80%93Pakistan_conflict")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("output/colored_qr.png")