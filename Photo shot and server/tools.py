# Module for utilitaries functions

def move(source, to): # Move file (but not delete it from source)
    srcFile = open(source, "rb")
    toFile = open(to, "w") # Creates the file if not exists

    toFile.write(srcFile.read())

    srcFile.close()
    toFile.close()

    print("\nFile Moved.\n")

def loadSD():
    import os, machine

    os.mount(machine.SDCard(), "/sd")

    print("\nMicroSD mounted.\n")