# Module for utilitaries functions

def move(source, to): # Move file
    srcFile = open(source, "rb")
    toFile = open(to, "w") # Creates the file if not exists

    toFile.write(srcFile.read())

    srcFile.close()
    toFile.close()

    print("\nFile Moved.\n")

    delete(srcFile)

def loadSD():
    import os, machine

    os.mount(machine.SDCard(), "/sd")

    print("\nMicroSD mounted.\n")

def delete(filename): # Delete file
    import os

    os.remove(filename)

    print("\nFile Deleted.\n")