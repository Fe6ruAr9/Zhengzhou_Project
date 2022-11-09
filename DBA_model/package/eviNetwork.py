import pandas as pd
import numpy as np
import networkx as nx
import powerlaw
import pwlf

# 创建实证数据网络类
class eviNetwork:

    def __init__(self, data):
        self.__data = data

    def toFit(self):
        G_evi = nx.from_pandas_edgelist(self.__data, source='sources', target='targets', edge_attr='weights',
                                    create_using=nx.MultiDiGraph)
        return G_evi
        # df_data = pd.DataFrame(G.degree(), columns=['nodes', 'degree'])
        # df_data = df_data.groupby(['degree']).size().reset_index(name='counts')
        # df_data = df_data.sort_values(by=['degree'], ascending=True)
        #
        # df_data['degree'] = np.log10(df_data['degree'])
        # df_data['counts'] = np.log10(df_data['counts'])
        #
        # df_data = (df_data - df_data.min()) / (df_data.max() - df_data.min())
        #
        # x_data = df_data['degree'].values
        # y_data = df_data['counts'].values
        #
        # pwlf_data = pwlf.PiecewiseLinFit(x_data, y_data)
        # res_data = pwlf_data.fit(3)
        #
        # xHat_data = np.linspace(min(x_data), max(x_data), num=10000)
        # yHat_data = pwlf_data.predict(xHat_data)
