# QR Code Generator

### Pre-requisites:

- So First we install the required package named as `qrcode`.

```bash
pip3 install qrcode
```

![Screenshot from 2023-11-09 16-31-32](https://github.com/Rohit312001/GitDemo/assets/76991475/c75e5f6b-eede-4313-a3ca-e8b73a4c1d7f)

### Process:

- **This line is a Python import statement. It's used to include the "qrcode" module from the "qrcode" package in your Python code.**

```python
import qrcode
```

- This code first import Image from Python Imaging Library (PIL) module and then open an image file (.png, .jpg, .bmp, etc.) using the open() function.

```python
from PIL import Image
```

- This line of code creates a `QR code` configuration with **specific version**, **error correction level**, **box size**, and **border size settings**. This configuration is stored in the `variable qr`, and you can use it to generate a QR code with these settings.

```python
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=5)
# Version- QR Code can have different versions ranging from 1 to 40.Highest version means more data can be stored in the QR code.

# error_correction=qrcode.constants.ERROR_CORRECT_H - QR codes can have error correction to recover data if it's damaged or partially obscured. "H" is a higher level of error correction.

# box_size=10 - This variable controls how many pixels each "box" of the QR code is.

# border=5 - This variable controls how many boxes thick the border should be (the default is 4, which is the minimum according to the QR standard).
```

- This line of code adds data to the QR code configuration. In this case, it's a simple text string. You can also add URLs, phone numbers, SMS messages, email addresses, and more.

```python
qr.add_data("Add your Data or Link for QR to be generated")
```

- This line of code generates the QR code image using the data stored in the `qr` variable. The `fit` parameter tells the QR code generator to resize the code image so that it fits in a 200x200 pixel square.

```python
qr.make(fit=True)
```

- This line of code creates an image from the QR code instance stored in the `qr` variable. The `fill_color` and `back_color` parameters control the foreground and background colors of the QR code.

```python
img = qr.make_image(fill_color="black", back_color="white")
```

- This line of code saves the image to a file named `image.png` in the current working directory.

```python
img.save("image.png")
```

### Summary:

- So,this code initializes a **QR Code** generation using the "qrcode" package, specifying the input **Data or Link**, the output **QR Code Image**, and then performs the generation, and saves the image when finished.

---

### OUTPUT:

- Python Code Runned Successfully on Terminal.

![image](https://github.com/Rohit312001/GitDemo/assets/76991475/4b2422db-16e3-4e34-8a3d-afe6829a7c23)

- Generated QR Code Image.

![image](https://github.com/Rohit312001/GitDemo/assets/76991475/53beb5c3-aabd-4d9c-861a-eeba72097dda)

![image](https://github.com/Rohit312001/GitDemo/assets/76991475/4a8494a3-8ab8-4924-8126-7421d57b29aa)

---
