# NAMA  : NAILA IZZATUR ROHMAH
# NIM   : 5301414047
# TUGAS 3 : MENGOLAH GAMBAR PADA WEBCAM LAPTOP MENJADI NEGATIF


import numpy as np
import cv2

cap = cv2.VideoCapture(0) 
#untuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada laptop.
print(cap.isOpened()) 
#untuk menampilkan gambar

while(True): 
    #untuk looping imshow, sehingga camera akan menangkap objek video secara realtime.
    ret, frame = cap.read() 
    #untuk menangkap gambar dengan format berwarna
    abu=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #untuk mengkonversi objek video dari berwarna menjadi grayscale(skala keabuan) sebelum diubah menjadi gambar negatif.
    cv2.imshow('webcam', 255-abu) 
    #untuk mengubah gambar dari skala keabuan menjadi gambar dengan skala negatif. 
    if cv2.waitKey(1) & 0xFF == ord('s'): 
        #perintah untuk menutup program dengan menekan tombol s pada keyboard
        break


cap.realease()
cv2.destroyAllwindows()
 