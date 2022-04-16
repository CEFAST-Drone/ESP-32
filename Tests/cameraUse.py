import camera
import os

def takePicture():
    img = camera.capture()
    if len(img): # Check if the photo is ok
        imageFile = open(f"teste.jpeg", 'w')
        imageFile.write(img)
        imageFile.close()

        print("Photo taked!")
        print(os.listdir())

    else:
        print("Photo not taked, an error occurred.")