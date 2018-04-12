from __future__ import division
import numpy as np
import pandas as pd
from scipy import stats

from datetime import datetime


def fill_fre_top_5(x):
    if len(x) <= 5:
        new_array = np.full(5, np.nan)
        new_array[0:len(x)] = x
        return new_array


def eda_analysis(missSet=[np.nan, 9999999999, -999999], df=None):
    # (11)Count distinct# 总个数
    count_un = df.apply(lambda x: len(x.unique()))
    count_un = count_un.to_frame('count')

    # (2)Zero Values# 零的个数
    count_zero = df.apply(lambda x: np.sum(x == 0))
    count_zero = count_zero.to_frame('count_zero')

    # (3)Mean Values# 平均数
    df_mean = df.apply(lambda x: np.mean(x[~np.isin(x, missSet)]))
    df_mean = df_mean.to_frame('mean')

    # (4)Median Values# 中位数
    df_median = df.apply(lambda x: np.median(x[~np.isin(x, missSet)]))
    df_median = df_median.to_frame('median')

    # (5)Mode Values# 众数
    df_mode = df.apply(lambda x: stats.mode(x[~np.isin(x, missSet)])[0][0])
    df_mode = df_mode.to_frame('mode')

    # (6)Mode Percentage# 众数比例
    df_mode_count = df.apply(
        lambda x: stats.mode(x[~np.isin(x, missSet)])[1][0])
    df_mode_count = df_mode_count.to_frame('mode_count')

    df_mode_perct = df_mode_count / df.shape[0]
    df_mode_perct.columns = ['mode_perct']

    # (7)Min Values# 最小值
    df_min = df.apply(lambda x: np.min(x[~np.isin(x, missSet)]))
    df_min = df_min.to_frame('min')

    # (8)Max Values# 最大值
    df_max = df.apply(lambda x: np.max(x[~np.isin(x, missSet)]))
    df_max = df_max.to_frame('max')

    # (9)quantile values 分位点
    json_quantile = {}

    for i, name in enumerate(df.columns):
        # print('the %d columns: %s' % (i, name))
        json_quantile[name] = np.percentile(
            df[name][~np.isin(df[name], missSet)], (1, 5, 25, 50, 75, 95, 99))

    df_quantife = pd.DataFrame(json_quantile)[df.columns].T
    df_quantife.columns = ['quan01', 'quan05', 'quan25',
                           'quan50', 'quan75', 'quan95', 'quan99']

    # (10)Frequent Values 频数
    json_fre_name = {}
    json_fre_count = {}

    for i, name in enumerate(df.columns):
        index_name = df[name][~np.isin(
            df[name], missSet)].value_counts().iloc[0:5, ].index.values
        index_name = fill_fre_top_5(index_name)

        json_fre_name[name] = index_name

        values_count = df[name][~np.isin(
            df[name], missSet)].value_counts().iloc[0:5, ].values
        values_count = fill_fre_top_5(values_count)

        json_fre_count[name] = values_count

    df_fre_name = pd.DataFrame(json_fre_name)[df.columns].T
    df_fre_count = pd.DataFrame(json_fre_count)[df.columns].T

    df_fre = pd.concat([df_fre_name, df_fre_count], axis=1)
    df_fre.columns = ['value1', 'value2', 'value3', 'value4',
                      'value5', 'freq1', 'freq2', 'freq3', 'freq4', 'freq5']

    # (11)Miss Values 缺失值
    df_miss = df.apply(lambda x: np.sum(np.isin(x, missSet)))
    df_miss = df_miss.to_frame('freq_miss')

    #####12.Combine All Informations##### 组合
    df_eda_summary = pd.concat(
        [count_un, count_zero, df_mean, df_median, df_mode,
         df_mode_count, df_mode_perct, df_min, df_max, df_fre,
         df_miss, df_quantife], axis=1
    )

    return df_eda_summary


if __name__ == "__main__":
    df = pd.read_csv('dos.kddcup.data.corrected.csv')
    label = df['label']
    df = df.drop(['protocol_type', 'service','flag','label'], axis=1)
    df_eda_summary = eda_analysis(missSet=[np.nan], df=df) # 本次的数据集完整没有缺失值
    df_eda_summary.to_csv('dos_01.csv', sep=',', header=True, index=True)