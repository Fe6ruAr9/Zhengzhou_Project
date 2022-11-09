import pandas as pd
import numpy as np
import time
import os
from package.genNetwork import *
from package.eviNetwork import *
import math
import decimal

# 计算三段拟合函数x,y
def calFunc(n):
    xmin = n.break_0
    xmax = n.break_n
    X = np.linspace(xmin, xmax, 1000)
    Y = np.array([])
    for i in range(3):
        x = X[np.where(X < n.fit_breaks[i + 1])]
        x = x[np.where(x >= n.fit_breaks[i])]
        s = n.slopes[i]
        intercept = n.intercepts[i]
        y = s * x + intercept
        Y = np.concatenate((Y, y))
        if i == 2:
            x = np.array([xmax])
            y = s * x + intercept
            Y = np.concatenate((Y, y))
    return X, Y


# 计算SSE，R
def diffunc(a, b):   #a = data b = gen
    x1, y1 = calFunc(a)
    x2, y2 = calFunc(b)
    SSE = sum((y1 - y2) ** 2)
    # y_mean = sum(y1) / len(y1)
    # SST = sum((y1 - y_mean) ** 2)
    # R = 1 - SSE / SST
    return SSE

def edge_diff(a,b):
    edge_count1 = len(a.edges())
    edge_count2 = len(b.edges())
    diff = abs(edge_count1 - edge_count2)
    return diff

# 计算x的取值范围
# def x_range(a, b):
#     if a.break_0 > b.break_0:
#         xmin = b.break_0
#     else:
#         xmin = a.break_0
#     if a.break_n > b.break_n:
#         xmax = a.break_n
#     else:
#         xmax = b.break_n
#     return xmin, xmax


if __name__ == '__main__':
    # plist = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
    plist = [decimal.Decimal(i) / decimal.Decimal(50) for i in range(1, 50)]
    m = 55
    Final_Result = {}

    file_path = "./Data/Female"
    all_file_list = os.listdir(file_path)

    for single_file in all_file_list:
        Result = []
        data = pd.read_csv(os.path.join(file_path, single_file), header=None)
        data.columns = ['id', 'sources', 'targets', 'weights']
        print(single_file + ' is processing...')
        for i in range(50):
            Edge_count = {}
            # for m in range(1, 20):
            for p_value in plist:
                evinetwork = eviNetwork(data).toFit()
                gennetwork = genNetwork(num=4000, m1=m, p=p_value).toFit()

                # pwlf_data, xHat_data, yHat_data = evinetwork.toFit()
                # pwlf_dual, xHat_dual, yHat_dual = gennetwork.toFit()
                #
                # sse, r = diffunc(pwlf_data, pwlf_dual)
                Edge_diff = edge_diff(evinetwork, gennetwork)

                Edge_count[p_value] = Edge_diff
                # print(Edge_diff)

            Result.append(min(Edge_count, key=Edge_count.get))
            print(Result)
            print("完成了", i + 1, "次循环")
        max_result = max(Result, key=Result.count)
        print("50次循环后收敛在{}，出现的次数为{}".format(max_result,Result.count(max_result)))
        Final_Result[single_file] = max_result
        print('收敛数据已被获取')
    df = pd.DataFrame.from_dict(Final_Result, orient='index', columns=['Param_p'])
    df = df.reset_index().rename(columns={'index': 'file_name'})
    df.to_csv('./Result/Female.csv')
