# Apply a mean filter
import numpy as np
from PIL import Image  
from numpy import asarray
import matplotlib.pyplot as plt
  
def main():
    area = 1
    # Open image
    image = Image.open('enhance-me.gif')
    image.show()

    # convert image to numpy array    
    npImage = np.array(image) 
    npImageMean = np.array(image) 

    m = npImageMean.shape[0] # qtd lines
    n = npImageMean.shape[1] # qtd cols
    for x in range(area, m-area-1):
        for y in range (area, n-area-1):
            w = npImageMean[x-area:x+area , y-area:y+area]
            #print(x,y)
            #print(w)
            #print(np.mean(w).astype(int))
            npImageMean[x,y] = np.mean(w).astype(int)
    
    # values os a windows 5 X 5 
    #print(npImage[0:5, 0:5])        
    #Convert ndarray image to Pillow image
    image2 = Image.fromarray(npImageMean)
    image2.show()

    # create the histogram
    # p=plt.hist(npImage, density=True) 
    # # plt.bar(p.density,weights=histogram.weights)
    # plt.show()

    histogram = instantiate_histogram()
    histogram = count_intensity_values(histogram, npImage)
    plot_hist(histogram)

    n_pixels = npImage.shape[0] * npImage.shape[1]
    hist_proba = get_hist_proba(histogram, n_pixels)
    accumulated_proba = get_accumulated_proba(hist_proba)
    new_gray_value = get_new_gray_value(accumulated_proba)

    npImage = equalize_hist(npImage,new_gray_value)

    image3 = Image.fromarray(npImage)
    image3.show()

    histogram = instantiate_histogram()
    histogram = count_intensity_values(histogram, npImage)
    plot_hist(histogram)


def equalize_hist(img, new_gray_value):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            img[row][column] = new_gray_value[str(int(img[row] [column]))]
    return img


def get_accumulated_proba(hist_proba): 
    acc_proba = {}
    sum_proba = 0
    
    for i in range(0, 256):
        if i == 0:
            pass
        else: 
            sum_proba += hist_proba[str(i - 1)]
            
        acc_proba[str(i)] = hist_proba[str(i)] + sum_proba
    return acc_proba

def get_new_gray_value(acc_proba):
    new_gray_value = {}
    
    for i in range(0, 256):
        new_gray_value[str(i)] = np.ceil(acc_proba[str(i)] * 255)
    return new_gray_value



def get_hist_proba(hist, n_pixels):
    hist_proba = {}
    for i in range(0, 256):
        hist_proba[str(i)] = hist[str(i)] / n_pixels
    
    return hist_proba


def instantiate_histogram():    
    hist_array= []
    
    for i in range(0,256):
        hist_array.append(str(i))
        hist_array.append(0)
    
    hist_dct = {hist_array[i]: hist_array[i + 1] for i in range(0, len(hist_array), 2)} 
    
    return hist_dct


def count_intensity_values(hist, img):
    for row in img:
        for column in row:
            hist[str(int(column))] = hist[str(int(column))] + 1
     
    return hist

def plot_hist(hist, hist2=''):
    if hist2 != '':
        figure, axarr = plt.subplots(1,2, figsize=(20, 10))
        axarr[0].bar(hist.keys(), hist.values())
        axarr[1].bar(hist2.keys(), hist2.values())
    else:
        plt.bar(hist.keys(), hist.values())
        plt.xlabel("Níveis intensidade")
        ax = plt.gca()
        ax.axes.xaxis.set_ticks([])
        plt.grid(True)
        plt.show()
    

if __name__ == "__main__":
    main()