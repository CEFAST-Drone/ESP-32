import camera
import os

def take_photo(filename, variable=0, saturation="", brightness="", contrast="", quality="", flip="", mirror="", 
                    framesize="", speffect="", whitebalance=""):
    ## ESP32-CAM (default configuration) - https://bit.ly/2Ndn8tN
    print('Starting camera...')
    camera.init(0, format=camera.JPEG)
    print('Camera started!\n')
    # The parameters: format=camera.JPEG, xclk_freq=camera.XCLK_10MHz are standard for all cameras.
    # You can try using a faster xclk (20MHz), this also worked with the esp32-cam and m5camera
    # but the image was pixelated and somehow green.

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
            print(os.listdir())

        else:
            print("Photo not taked, an error occurred.")

        if variable:
            imgFile = open(filename + ".jpg", 'r')
            img = imgFile.read()
            imgFile.close()

            return img
    except Exception as e:
        print(e)
    
    camera.deinit() # Close Camera