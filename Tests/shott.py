import camera
import os

## ESP32-CAM (default configuration) - https://bit.ly/2Ndn8tN
print('Iniciando camera...')
camera.init(0, format=camera.JPEG)
print('Camera iniciada!\n')
# The parameters: format=camera.JPEG, xclk_freq=camera.XCLK_10MHz are standard for all cameras.
# You can try using a faster xclk (20MHz), this also worked with the esp32-cam and m5camera
# but the image was pixelated and somehow green.




# quality
#camera.quality(63)
# 10-63 lower number means higher quality

print('Tirando foto...')
buf = camera.capture()

print('Salvando foto...')
if len(buf): # Check if the photo is ok
    imageFile = open("teste.jpg", 'w')
    imageFile.write(buf)
    imageFile.close()

    print("Photo taked!")
    print(os.listdir())

else:
    print("Photo not taked, an error occurred.")