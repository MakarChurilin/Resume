import qrcode
import os


def create_qr_code():
    text = input("Введите текст для QR-кода: ")
    filename = input("Введите имя файла для сохранения QR-кода: ") + ".png"
    img = qrcode.make(text)
    img.save(filename)
    print(f'QR-код успешно создан и сохранен в файл {filename}.')
    os.startfile(filename)


create_qr_code()
