# fourier_transform-

## 概要
画像のフーリエ変換と逆フーリエ変換を行う実装を行う。

## File of fourier_transform

女優 森七菜の画像のフーリエ変換を行った。
カラー画像であったので、rgb2grayを用いて白黒画像に変換し、入力信号の周波数を計算した。
NumpyはFFTを計算するための関数 np.fft.fft2() を用意しているためこれを用いる。
この関数は複素数型の配列を出力する。
また各画素に対し, 対数変換を実行する。
実行した画像は,"fourier_morinana.png"に保存してある。


## File of inverse_fourier_transform

スペイン　バルセロナ県にある世界遺産、サグラダファミリアをフーリエ変換したものを逆フーリエ変換を行った。
OpenCVはDFTを行う"cv2.dft()" とIDFTを行う"cv2.idft()"という関数を用意しいる。
最初のチャンネルは結果の実部，二つ目のチャンネルが虚部に対応している。入力画像は np.float32 型に変換される必要がある。

※cv2.cartToPolar() 関数を使い振幅と位相の両方を取得.
IDFTを行う。ローパスフィルタ(高周波成分の除去)を試行する。ローパスフィルタは画像にボケを加える．まず初めに低周波領域に高い値を持ち，高周波領域が0となるマスクを作成する。

## 参考URL/参考文献
  - numpyとopenCVを使った画像のフーリエ変換と逆変換
  https://www.hello-python.com/2018/02/16/numpyとopencvを使った画像のフーリエ変換と逆変換/
  - OPENCV Table of Contents フーリエ変換
  http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html

## Python 実行環境
  - Microsoft Azure Notebooks Python3 Powered by Jupyter
  - Anaconda-Navigator
  
## 追加で実行したモジュール等（余分なものが入っている可能性あり）
!pip install scikit-image==0.12.3
import numpy as np
from numpy.random import rand
from numpy import uint8, float32, float64, log, pi, sin, cos, abs, sqrt
import matplotlib.pyplot as plt
%matplotlib inline
plt.gray();
from matplotlib.pyplot import imshow
from skimage.io import imread, imsave
from skimage.color import rgb2gray, rgb2hsv
from skimage.transform import rotate, resize
import skimage
skmajor, skminor, sknumber = skimage.__version__.split(".")
if int(skminor) >= 11:
    from skimage.filters import threshold_otsu # version 0.11 and after
else:
    from skimage.filter import threshold_otsu # version 0.10 and before
from scipy.ndimage.filters import convolve
from __future__ import print_function, division
from os.path import getsize
from time import time
