import pandas as pd
import numpy as np
import networkx as nx
import pwlf


# 创建生成网络类
class genNetwork:

    def __init__(self, m1, p, num, m2=1):
        self.num = num
        self.__m1 = m1
        self.__m2 = m2
        self.__p = p

    def toFit(self):
        G_gen = nx.dual_barabasi_albert_graph(self.num, self.__m1, self.__m2, self.__p)
        return G_gen
        # df_dual = pd.DataFrame(G.degree(), columns=['nodes', 'degree'])
        # df_dual = df_dual.groupby(['degree']).size().reset_index(name='counts')
        # df_dual = df_dual.sort_values(by=['degree'], ascending=True)
        # df_dual['degree'] = np.log10(df_dual['degree'])
        # df_dual['counts'] = np.log10(df_dual['counts'])
        #
        # df_dual = (df_dual - df_dual.min()) / (df_dual.max() - df_dual.min())
        # x_dual = df_dual['degree'].values
        # y_dual = df_dual['counts'].values
        #
        # pwlf_dual = pwlf.PiecewiseLinFit(x_dual, y_dual)
        # res_dual = pwlf_dual.fit(3)
        #
        # xHat_dual = np.linspace(min(x_dual), max(x_dual), num=10000)
        # yHat_dual = pwlf_dual.predict(xHat_dual)
        #
        # return pwlf_dual, xHat_dual, yHat_dual

    @property
    def p(self):
        return self.__p

    @property
    def m1(self):
        return self.__m1

    @property
    def m2(self):
        return self.__m2