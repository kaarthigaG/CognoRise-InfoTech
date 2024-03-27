import qrcode
import cv2
from pyzbar.pyzbar import decode

def encode_qr_code(data, filename):
    #create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    #add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)


    #create an image from the QR code
    img = qr.make_image(fill_color="black",back_color="white")


    #save the image
    img.save(filename)
    print(f"qr code saved as filename!")


def decode_qr_code(filename):
    #read the QR code image
    image = cv2.imread(filename)


    #decode the QR code
    decoded_objects = decode(image)

    #print decoded data
    for obj in decoded_objects:
        print("data:", obj.data.decode ("utf-8"))


    #dispaly the qr code image
    cv2.imshow("qr code",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    #example data to be encoded
    data_to_encode = "hello, here is the qr code!"


    #file name for saving and reading the QR code image
    qr_code_filename = "qrcode.png"


    # encode QR code
    encode_qr_code(data_to_encode,qr_code_filename)

    #decode QR code
    decode_qr_code(qr_code_filename)


