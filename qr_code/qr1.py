import qrcode as qr
img=qr.make("https://www.geeksforgeeks.org/yolo-you-only-look-once-real-time-object-detection/")
img.save("output/qr_image.png")
