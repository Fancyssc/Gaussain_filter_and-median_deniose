from PIL import Image
import numpy as np

#中值降噪
def median(img, x, y,bandrange):
    L = []
    for i in range(x-bandrange,x+bandrange):
        for j in range(y-bandrange,y+bandrange):
            gray = img.getpixel((i, j))  # 取出灰度值
            L.append(gray)
    L.sort()
    c = L[12]
    return c


def denoise_median(path1, path2,bandwidth):
    img1 = Image.open(path1)
    img1 = img1.convert('L')  # 将图像1转换为灰度图
    w, h = img1.size
    img2 = Image.new('L', (w, h), 'white')  # 图像2
    for x in range(bandrange, w -bandrange):
        for y in range(bandrange, h - bandrange):
            c = median(img1, x, y,bandrange)  # 求中值
            img2.putpixel((x, y), c)  # 将灰度设置为中值
    img2.save(path2)
##############中值结束#####################

#均值降噪
def average(img, x, y,bandrange):
    L=0
    for i in range(x - bandrange, x + bandrange):
        for j in range(y - bandrange, y + bandrange):
            gray = img.getpixel((i, j))  # 取出灰度值
            L=L+gray
    return int(L/((bandrange*2)**2-1))

def denoise_average(path1, path2,bandwidth):
    img1 = Image.open(path1)
    img1 = img1.convert('L')  # 将图像1转换为灰度图
    w, h = img1.size
    img2 = Image.new('L', (w, h), 'white')  # 图像2
    for x in range(bandrange, w -bandrange):
        for y in range(bandrange, h - bandrange):
            c = average(img1, x, y,bandrange)  # 求中值
            img2.putpixel((x, y), c)  # 将灰度设置为中值
    img2.save(path2)
################均值结束#####################


#高斯降噪
#创建高斯核，输入参数是高斯核的窗宽
def gaussian_kernel(kernel_size):
    start=-1
    end=1
    mean_x = 0
    mean_y = 0
    sigma=1#均值为0，方差为1
    X = np.linspace(start, end,kernel_size)
    Y = np.linspace(start, end,kernel_size)
    x, y = np.meshgrid(X, Y)
    gaussian=1/(2*np.pi*sigma**2)*np.exp(-((x-mean_x)**2+(y-mean_y)**2)/(2*sigma**2))
    return gaussian

#获取灰度值
def gaussian(img, x, y,bandrange):
    tmp_gaussian = gaussian_kernel(bandwidth)
    tmp=0
    for i in range(x - bandrange, x + bandrange):
        for j in range(y - bandrange, y + bandrange):
            tmp = tmp + img.getpixel((i, j))*tmp_gaussian[i-(x-bandrange)][j-(y-bandrange)]  # 取出灰度值
    return int(tmp)+60#调亮

def denoise_gaussian(path1, path2,bandwidth):
    img1 = Image.open(path1)
    img1 = img1.convert('L')  # 将图像1转换为灰度图
    w, h = img1.size
    img2 = Image.new('L', (w, h), 'white')  # 图像2
    for x in range(bandrange, w -bandrange):
        for y in range(bandrange, h - bandrange):
            c = gaussian(img1, x, y,bandrange)  # 求中值
            img2.putpixel((x, y), c)  # 将灰度设置为中值
    img2.save(path2)

##################高斯结束#####################



path1 = "noise1.jpg"  # 带噪声的图像
path2 = "3(1)+60.jpg"  # 降噪后的图像

bandwidth=3#窗宽
bandrange=int(bandwidth/2)
#denoise_median(path1, path2,bandwidth)
#denoise_average(path1, path2,bandwidth)
denoise_gaussian(path1, path2,bandwidth)