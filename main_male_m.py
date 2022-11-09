import pandas as pd
import numpy as np
import time
import os
from package.genNetwork import *
from package.eviNetwork import *
import math
import decimal

def edge_diff(a,b):
    edge_count1 = len(a.edges())
    edge_count2 = len(b.edges())
    diff = abs(edge_count1 - edge_count2)
    return diff

if __name__ == '__main__':
    plist = [decimal.Decimal(i) / decimal.Decimal(50) for i in range(1, 50)]
    m = 100
    Final_Result = {}

    file_path = "./Data/Male"
    all_file_list = os.listdir(file_path)

    for single_file in all_file_list:
        Result = []
        data = pd.read_csv(os.path.join(file_path, single_file), header=None)
        data.columns = ['id', 'sources', 'targets', 'weights']
        print(single_file + ' is processing...')
        for i in range(50):
            Edge_count = {}
            for p_value in plist:
                evinetwork = eviNetwork(data).toFit()
                gennetwork = genNetwork(num=4000, m1=m, p=p_value).toFit()

                Edge_diff = edge_diff(evinetwork, gennetwork)
                Edge_count[p_value] = Edge_diff

            Result.append(min(Edge_count, key=Edge_count.get))
            print(Result)
            print("has completed ", i + 1, " loops")
        max_result = max(Result, key=Result.count)
        print("Converges at {} after 50 loops，The number of occurrences is {}".format(max_result,Result.count(max_result)))
        Final_Result[single_file] = max_result
        print('Convergence data has been acquired')
    df = pd.DataFrame.from_dict(Final_Result, orient='index', columns=['Param_p'])
    df = df.reset_index().rename(columns={'index': 'file_name'})
    df.to_csv('./Result/Male.csv')
