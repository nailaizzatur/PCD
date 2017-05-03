# NAMA  : NAILA IZZATUR ROHMAH
# NIM   : 5301414047
# TUGAS 3 : MENGOLAH GAMBAR PADA WEBCAM LAPTOP MENJADI BRIGHTNESS


import numpy as np
import cv2

cap = cv2.VideoCapture(0) 
#untuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada laptop.
print(cap.isOpened()) 
#untuk menampilkan gambar


while(True): 
    #untuk looping imshow, sehingga kamera akan menangkap objek video secara realtime.
    ret, frame = cap.read() 
    #untuk menangkap gambar dengan format berwarna
    bright = cv2.addWeighted(frame,1.5, np.zeros(frame.shape, frame.dtype), 0, 60) 
    #untuk meningkatkan nilai kecerahan gambar
    cv2.imshow('webcam',bright) 
    #untuk menampilkan gambar yang telah diubah tingkat kecerahannya.
    if cv2.waitKey(1) & 0xFF == ord('s'): 
        #perintah untuk menutup program dengan menekan tombol s pada keyboard
        break 
        # untuk menghentikan program


cap.realease()
cv2.destroyAllwindows()
