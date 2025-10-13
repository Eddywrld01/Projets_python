import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=5,
    border=4,
)
qr.add_data("https://imgs.search.brave.com/-bnUfhGb4i7GF1moYMfIQveN8nmKOsfmmvnhz_JmWrI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hLnRo/dW1icy5yZWRkaXRt/ZWRpYS5jb20vN2tH/Zi1qYzNRcDBRR0xI/a1M4ZWt0XzdfS3BF/S2xhLWVSb1lXME53/V1B5OC5qcGc")
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color = "white")
img.save("qrcode.png")