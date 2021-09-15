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
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/a.tiff')
    
    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[1,0,-1],[0,0,0],[-1,0,1]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/b.tiff')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/c.tiff')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/d.tiff')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/e.tiff')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/f.tiff')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/g.tiff')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[1/256,4/256,6/256,4/256,1/256],[4/256,16/256,24/256,16/256,4/256],[6/256,24/256,36/256,24/256,6/256],[4/256,16/256,24/256,16/256,4/256],[1/256,4/256,6/256,4/256,1/256]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/h.tiff')

    # convert image to numpy array   
    npImage = np.array(image).astype(int)
    k = np.array([[-1/256,-4/256,-6/256,-4/256,-1/256],[-4/256,-16/256,-24/256,-16/256,-4/256],[-6/256,-24/256,476/256,-24/256,-6/256],[-4/256,-16/256,-24/256,-16/256,-4/256],[-1/256,-4/256,-6/256,-4/256,-1/256]])
    npImage = ndimage.convolve(npImage,k, mode='reflect')
    npImage = np.where(npImage<0, 0, npImage)
    image2 = Image.fromarray(npImage.astype('uint8'))
    image2.show()
    image2.save('images/i.tiff')

if __name__ == "__main__":
    main()