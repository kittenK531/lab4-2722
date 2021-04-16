import numpy as np
from sklearn.linear_model import LinearRegression

i=0
lambdaa_index = 1
lambdaa = np.array(['364','402.8','434','544.4'])
Lambda = lambdaa[lambdaa_index]

def background():
    background = np.loadtxt('background_noLV.txt')
    bg = np.zeros((77,2),float)
    y_bg = background[0:76,1]
    return y_bg

def Loaddata(i, y_bg):
    wavelength = [f"{Lambda}_1",f"{Lambda}_2", f"{Lambda}_3", f"{Lambda}_4", f"{Lambda}_5", f"{Lambda}_6", f"{Lambda}_7"]
    filename=f"{wavelength[i]}.txt"
    data=np.loadtxt(filename)
    x = data[:,0]
    y = data[:,1] - y_bg
    return x, y

def strip(j, x, y):
    return x[0:j], y[0:j], x[j+1:77], y[j+1:77]

def fit(x,y):
    model = LinearRegression().fit(x.reshape((-1,1)), y)
    #print('intercept:', model.intercept_)
    #print('slope:', model.coef_)

    [m] = model.coef_

    y_pred = model.predict(x) #numerical data
    #y_pred = model.intercept_ + model.coef_ * x #analytical graph equation
    return y_pred, m, model.intercept_

def intersect(m1,m2,c1,c2):
    x = (c2-c1)/(m1-m2)
    y = m2* x +c2

    #print(f'intersection point = ({x},{y})')
    return x,y    

def predicted(j):

    y_bg = background()
    x, y = Loaddata(0,y_bg)
    x1, y1, x2, y2 = strip(j,x,y)

    y_pred1, m1, c1 = fit(x1.reshape((-1,1)),y1)
    y_pred2, m2, c2 = fit(x2.reshape((-1,1)),y2)

    x_i, y_i = intersect(m1, m2, c1, c2)

    return m1, x_i, y_i

def getIndex():
    m = 1
    m_MAX = 0
    index = 0

    for i in np.arange(51,62,1):
        m, x_i, y_i = predicted(i)
        if m > m_MAX:
            m_MAX = m
            #print(m)
            index = i

    return index

def main():

    i = getIndex()
    m, x, y = predicted(i)

    print(f'intersection point = ({x},{y})')

main()
