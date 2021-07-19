import os
import numpy as np
import pandas as pd

class Data(object):
    def __init__(self) -> None:
        super().__init__()
    
    def data_load(self,filename):
        fr = open(filename)
        arrayOnlines = fr.readlines()
        numberOflines = len(arrayOnlines)
        Mat = np.zeros((numberOflines,3))
        classLabelVector = []
        index = 0
        for line in arrayOnlines:
            line = line.strip()
            listFromLine = line.split('\t')
            Mat[index,:] = listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
        return Mat, classLabelVector
    def read_csv(self,*args):
        sum_data = []
        for data in range(1,len(args[0])):
            data_x = pd.read_csv(args[0][0],sep = ',')[args[0][data]].values
            sum_data.append(data_x)
        return np.array(sum_data)
