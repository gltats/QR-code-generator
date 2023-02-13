import qrcode
from PIL import Image, ImageDraw, ImageFont

def create_qr_with_title(title, url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    qr_img.save("qr_code.png")

url = "https://drive.google.com/file/d/1aJCln75OyTys8CCsslRl7L5JPVIoMKhO/view?usp=share_link"
title = "Party Invitation:"
create_qr_with_title(title, url)