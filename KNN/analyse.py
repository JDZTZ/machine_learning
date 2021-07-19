import matplotlib
import matplotlib.pyplot as plt
from numpy.lib.shape_base import tile
import numpy as np

class Analyse(object):
    def __init__(self) -> None:
        super().__init__()
        
    def draw_relation(self, title, *args, **kwargs):
        list_x, list_y = [], []
        title_x, title_y = [], []       
        for i in range(len(args)-1):
            for j in range(i+1,len(args)):
                list_x.append(args[i])
                list_y.append(args[j])
                title_x.append(title[i])
                title_y.append(title[j])
        len_show = len(list_x)
        labels = [v for k, v in kwargs.items()]

        for show in range(len_show):
            plt.figure()
            ax = plt.subplot(111)
            ax.set_xlabel(title_x[show])
            ax.set_ylabel(title_y[show])
            scatter = ax.scatter(list_x[show], list_y[show], c = labels, cmap = 'autumn') 
            a,b = scatter.legend_elements()
            b = ['$\\mathdefault{didnotlike}$',
                '$\\mathdefault{smallDoses}$',
                '$\\mathdefault{largeDoses}$',]
            legend_title = ax.legend(a,b,title='')
            plt.savefig('result'+str(show)+'.jpg')
            plt.close()
    

    def autoNorm(self,dataSet):
        minVal = dataSet.min(0)
        maxVal = dataSet.max(0)
        interval = maxVal - minVal
        normDataSet = np.zeros(dataSet.shape)
        m = dataSet.shape[0]
        normDataSet = dataSet-tile(minVal, (m,1))
        normDataSet = normDataSet/tile(interval, (m,1))
        return normDataSet, interval, minVal
