#from ipywidgets import interact, interactive, fixed
#import ipywidgets as widgets

A = rgb2gray(imread('images/nanamori-2018a.jpg'))
imshow(A)
plt.show()

def LgTrans(x):
    C = 1/log(1+1) # max value
    return C * log(1+x)

im = np.abs(np.fft.fft2(A)) # imはfloat64になる

h, w = im.shape
im = np.roll(im, h//2, 0)
im = np.roll(im, w//2, 1)

for i in range(h):
    for j in range(w):
        im[i][j] = LgTrans(im[i][j])
        
imshow(im, vmin=0)
plt.colorbar()
plt.axis('off')
plt.show()

print("max: ", im.max())
print("min: ", im.min())
