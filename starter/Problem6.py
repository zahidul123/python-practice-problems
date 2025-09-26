### Problem-6: Write a function named "isLandscape" that takes 2 numbers (image width and height) as arguments and the function returns Landscape if the image width has a higher value than height. Returns Portrait otherwise
def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        #height > width
        return "Portrait"

imageHeight = int(input("Enter image height: "))
imageWidth = int(input("Enter image width: "))

print(isLandscape(imageWidth, imageHeight))
