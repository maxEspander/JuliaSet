import tkinter as tk
from math import sqrt
from PIL import Image

HEIGHT = 600
WIDTH = 600

setparameters = {'maxIter': 50,
                 'central_pt': [0, 0],
                 'magnif': 1,
                 'C':  -0.77544 + 0.113011j,
                 'xmin': 0,
                 'xmax': 0,
                 'ymin': 0,
                 'ymax': 0}

im = Image.new('RGB', (WIDTH, HEIGHT))

def getJuliaSet():
    set_map = []
    get_iter_list = []
    r = calculate_r(setparameters['C'])
    max_iter = 0
    setXYField()
    xmin = setparameters['xmin']
    xmax = setparameters['xmax']
    ymin = setparameters['ymin']
    ymax = setparameters['ymax']

    dx = (xmax - xmin) / WIDTH
    dy = (ymax - ymin) / HEIGHT

    for i in range(WIDTH):
        set_map.append([])
        for j in range(HEIGHT):
            x = xmin + i * dx
            y = ymin + j * dy
            z = complex(x, y)
            get_iter_list = getIterList(z, setparameters['C'], setparameters['maxIter'], r)
            count_iteration = len(get_iter_list)
            set_map[i].append(count_iteration - 1)
            print('make map ', set_map[i][j])
            if max_iter < count_iteration:
                max_iter = count_iteration

    printJuliaSet(set_map, max_iter)

def setXYField():
    r = calculate_r(setparameters['C'])
    xmin = setparameters['xmin']
    xmax = setparameters['xmax']
    ymin = setparameters['ymin']
    ymax = setparameters['ymax']
    if xmin == 0 or xmax == 0 or ymin == 0 or ymax == 0:
        setparameters['xmin'] = setparameters['central_pt'][0] - r
        setparameters['xmax'] = setparameters['central_pt'][0] + r
        setparameters['ymin'] = setparameters['central_pt'][1] - r
        setparameters['ymax'] = setparameters['central_pt'][1] + r

def printJuliaSet(s_map, maxIteration):
    xmin = setparameters['xmin']
    xmax = setparameters['xmax']
    ymin = setparameters['ymin']
    ymax = setparameters['ymax']
    dx = (xmax - xmin) / WIDTH
    dy = (ymax - ymin) / HEIGHT

    for i in range(WIDTH):
        for j in range(HEIGHT):
            x = xmin + dx * i
            y = ymin + dy * j
            z = complex(x, y)
            print('print map ', s_map[i][j])
            set_color = setHeatMap(s_map[i][j], 0, maxIteration, z, calculate_r(setparameters['C']))
            im.putpixel((i, j), set_color)
    im.show()

def setHeatMap(value, min, max, z, r):
    val = (value - min)/(max - min)
    red = int(255 * val)
    green = int(255 * (1 - val)*0.5)
    if (abs(z) / r) > 1:
        blue = 255
    else:
        blue = int(abs(z) / r)
    return (red, green, blue)

def getIterList(z0, c, maxIter, r):
    ret = [z0]
    z = z0
    for i in range(maxIter):
        z = z * z + c
        if abs(z) > r:
            break
        ret.append(z)
    return ret

def calculate_r(c):
    return (1 + sqrt(1 + 4 * abs(c)))/2


def fromRGB(rgb):
    return '#%02x%02x%02x' % rgb

def main():
    root = tk.Tk()
    paramframe = tk.Frame(root)
    imgframe = tk.Frame(root)
    complcLabel = tk.Label(master=paramframe, text='Коэффициент С:')
    complcLabel.pack(side=tk.TOP)
    complc = tk.Entry(paramframe)
    complc.pack(side=tk.TOP)
    radiuslabel = tk.Label(paramframe, text='Коеффициент масшаба')
    radiuslabel.pack(side=tk.TOP)
    radius = tk.Entry(paramframe)
    radius.pack(side=tk.TOP)
    paramframe.pack(side=tk.LEFT)
    imgframe.pack(side=tk.LEFT)
    root.geometry(str(400) + 'x' + str(400))
    getJuliaSet()
    #root.mainloop()

if __name__ == '__main__':
    main()