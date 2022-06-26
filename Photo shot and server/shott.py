import camera
import os

def take_photo(filename, variable=0, saturation="", brightness="", contrast="", quality="", flip="", mirror="", 
                    framesize="", speffect="", whitebalance="", dirLocal=""):

    print('Starting camera...')
    camera.init(0, format=camera.JPEG)
    print('Camera started!\n')

    # Camera configuration

    if saturation: camera.saturation(saturation) # -2 to 2 
    if brightness: camera.brightness(brightness) # -2 to 2
    if contrast: camera.contrast(contrast) # -2 to 2
    if quality: camera.quality(quality) # 10 (high) to 63 (low)
    if flip: camera.flip(flip) # 0 or 1
    if mirror: camera.mirror(mirror) # 0 or 1
    if framesize: camera.framesize(framesize) 
    if speffect: camera.speffect(speffect)
    if whitebalance: camera.whitebalance(whitebalance)

    print('Taking photo...')
    buf = camera.capture()

    try:
        if len(buf): # Check if the photo is ok
            print('Saving photo...')

            imageFile = open(filename + ".jpg", 'w')
            imageFile.write(buf)
            imageFile.close()

            print("Photo taked!")
            print(os.listdir(dirLocal))

        else:
            print("Photo not taked, an error occurred.")

        if variable:
            imgFile = open(filename + ".jpg", 'r')
            img = imgFile.read()
            imgFile.close()

            return img
    except Exception as e:
        print("An error has occured, \n" + str(e))
    
    camera.deinit() # Close Camera