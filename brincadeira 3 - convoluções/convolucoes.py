# Apply convolve
import numpy as np
from PIL import Image
from scipy import ndimage

def main():
    # Open image
    image = Image.open('images/img.jpg')
    image.show()

    # convert image to numpy array    
    npImage = np.array(image).astype(int)
    #kernel
    k = np.array([[0,0,0],[0,1,0],[0,0,0]])
    npImage = ndimage.convolve(npImage,k, cval=0.0)
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/a.jpg')
    
    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[1,0,-1],[0,0,0],[-1,0,1]])
    npImage = ndimage.convolve(npImage,k, cval=0.0, mode='nearest')
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/b.jpg')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/c.jpg')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/d.jpg')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/e.jpg')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
    npImage = ndimage.convolve(npImage,k, mode='constant', cval=0.0,)
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/f.jpg')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]])
    npImage = ndimage.convolve(npImage,k, mode='constant', cval=0.0,)
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/g.jpg')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[1/256,4/256,6/256,4/256,1/256],[4/256,16/256,24/256,16/256,4/256],[6/256,24/256,36/256,24/256,6/256],[4/256,16/256,24/256,16/256,4/256],[1/256,4/256,6/256,4/256,1/256]])
    npImage = ndimage.convolve(npImage,k, mode='constant', cval=0.0,)
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/h.jpg')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[-1/256,-4/256,-6/256,-4/256,-1/256],[-4/256,-16/256,-24/256,-16/256,-4/256],[-6/256,-24/256,476/256,-24/256,-6/256],[-4/256,-16/256,-24/256,-16/256,-4/256],[-1/256,-4/256,-6/256,-4/256,-1/256]])
    npImage = ndimage.convolve(npImage,k, mode='constant', cval=0.0,)
    image2 = Image.fromarray(npImage)
    image2.show()
    image2.convert('L').save('images/i.jpg')

if __name__ == "__main__":
    main()