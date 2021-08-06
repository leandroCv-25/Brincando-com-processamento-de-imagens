import numpy as np
from PIL import Image  
from numpy import asarray

def main():
    # Open image
    image = Image.open('images/img4.jpg')

    # convert image to numpy array    
    npImage = np.array(image) 
    print(type(npImage ))
    # summarize shape
    print(npImage.shape)
    
    # value of pixel 0 0
    
    #Change values of lines 10 - 25
    npImage[10:25,:] = 255

    #Change values of columns 10 - 25
    npImage[:,10:25] = 0

    npImage = 255 - npImage

    #Convert ndarray image to Pillow image
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.save('images/img4_inverted.jpg')

if __name__ == "__main__":
    main()