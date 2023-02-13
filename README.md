# QR-code-generator
This script generates a QR code image from a given URL and saves it as a PNG file. The generated QR code image also includes a title above the QR code.
Prerequisites  

Before you start using the script, make sure you have the following packages installed:
- qrcode
- pillow

You can install these packages using the following command:

```pip install qrcode pillow```  

## Usage

To generate a QR code, simply modify the following lines in the script:
```
url = "https://drive.google.com/file/d/xxxxxxxxxxxxxx/view?usp=share_link"
title = "Party Invitation:"
```

Replace the url variable with the URL you want to generate a QR code for, and replace the title variable with the desired title to be displayed above the QR code.

Then, run the script using the following command:

```

python QR-code-generator.py
```

The generated QR code image will be saved as qr_code.png in the same directory as the script.  
  
! Note
This script uses the default font that is available on your system. If you want to use a specific font, you can specify the path to the font file in the following line of the script:

```

font = ImageFont.truetype("arial.ttf", 36)
```

Replace "arial.ttf" with the path to the desired font file.
