import numpy as np
from knn import KNN 
from dataload import Data 
from analyse import Analyse
import argparse
analyse_data = Analyse()
dataset = Data()

def main(args):
    
    datingmat, datinglabel = dataset.data_load(args.path)
    tuple = (datingmat[:,1],datingmat[:,2],datingmat[:,0])
    
    if args.draw:
        analyse_data.draw_relation(['airplane mileage','game rate','ice cream'],
                            datingmat[:,0],datingmat[:,1],datingmat[:,2],
                            a = datinglabel)
    if args.autonorm:
        datingmat, interVal, minVal = analyse_data.autoNorm(datingmat)
    knn = KNN()
    count = 0.0

    knn.dating = datingmat
    knn.datinglabel = datinglabel
    knn.k = args.k
    knn.ratio = args.ratio
    

    '''
    网格搜索
    '''
    if args.grid_search:
        rate1 = [x*0.01+0.05 for x in range(20)]
        rate2 = [y*0.01+1.8 for y in range(20)]
        rate3 = [z*0.01 for z in range(20)]
        max_acc = 0.9
        for i in rate1:
            for j in rate2:
                for z in rate3:      
                    knn.dating = (np.array([i,j,z]).reshape(1,3))*datingmat
                    accuracy = knn.result()
                    if accuracy >= max_acc:
                        max_acc = accuracy
                        max_i,max_j,max_z = i, j, z
                        
        print('The best accuracy is : {:.1f}%\n The best parameter configuration is :\n airplane mileage:{:.2f} \tgame rate:{:.2f}\tice cream:{:.2f}'.format(max_acc*100, max_i, max_j, max_z))
    else:
        accuracy = knn.result()
        print('The best accuracy is : {:.1f}%'.format(accuracy*100))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--path', type=str, default= './datingTestSet2.txt', help='data path')
    parser.add_argument('--autonorm', action='store_true', help='Whether normalize')
    parser.add_argument('--grid_search', action='store_true', help='Whether use the grid search')
    parser.add_argument('--k', type=int, default=10, help='The K of nearest neighbors')
    parser.add_argument('--ratio', type=float, default=0.1, help='The test ratio of data')
    parser.add_argument('--draw', action='store_true', help='Whether draw the scatter diagram')

    args = parser.parse_args()

    main(args)


