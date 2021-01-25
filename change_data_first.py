import csv
import os


words = ['美国', '丹麦', '外媒', '世卫', '国际', 'WHO', '美媒', '外国', '澳', '意大利', '韩国', '瑞典', '英国', '特朗普', '集体免疫', '群体免疫', '菲律宾', '罗斯福', '邻国', '抗议总指挥', '人类', '伊朗', '盖茨', '阿根廷', '俄', '外籍', '美方', 'CNN', '纽约', '秘鲁', '外交部', '中非', '日本', '巴西', '朝鲜', '普京', 'BBC', '匈牙利', '法国', '塞尔维亚']
words = set(words)


def set_location(s):  # s为文章标题
    for each in words:
        if each in s:
            return 0
    return 100


with open(os.path.join(os.path.dirname(__file__), 'data_sets.csv')) as csvFile:
    rows = csv.reader(csvFile)
    with open(os.path.join(os.path.dirname(__file__), 'data_sets_new.csv'), 'w') as f:
        writer = csv.writer(f)
        for row in rows:
            row.append(set_location(row[1]))
            writer.writerow(row)
