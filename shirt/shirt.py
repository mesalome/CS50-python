import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    if len(sys.argv)!=3:
        if len(sys.argv) <3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")
    else:
        extension1 = splitext(sys.argv[1])[1].lower()
        extension2 = splitext(sys.argv[2])[1].lower()
        if check_extension(extension1) and check_extension(extension2):
            if extension1 == extension2:
                try:
                    photo = Image.open(sys.argv[1])
                    shirt = Image.open("shirt.png")
                    size = shirt.size
                    photo = ImageOps.fit(photo, size, bleed=0.0, centering=(0.5, 0.5))
                    photo.paste(shirt, shirt)
                    photo.save(sys.argv[2])

                except FileNotFoundError:
                    sys.exit("Input does not exist")

            else:
                sys.exit("Input and output have different extensions ")
        else:
            sys.exit("Invalid input")

#function checks if user's input is in allowed format
def check_extension(extension):
    allowed_extensions = ['.jpg', 'jpeg', '.png']
    for item in allowed_extensions:
        if extension == item:
            return True


if __name__ =="__main__":
    main()
