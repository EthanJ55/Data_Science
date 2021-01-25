import pandas as pd
import jieba
import csv
import os


def remove(s):  # 去除空格和回车
    paras = s.split('\n')
    s = ''
    for each in paras:
        s += each
    paras = s.split()
    s = ''
    for each in paras:
        s += each
    return s


def get_article(url):
    file = open(url)
    raw_text = ''
    lines = file.readlines()
    for line in lines:
        raw_text += line
    res = remove(raw_text)
    file.close()
    return res


def get_score(text):  # 基于BosonNLP情感词典计算情感值
    df = pd.read_table(r'BosonNLP_sentiment_score/BosonNLP_sentiment_score.txt', sep=' ', names=['key', 'score'])
    key = df['key'].values.tolist()
    score = df['score'].values.tolist()
    # jieba分词
    segs = jieba.lcut(text, cut_all=False)  # 返回list
    # 计算得分
    score_list = [score[key.index(x)] for x in segs if(x in key)]
    return sum(score_list)


if __name__ == '__main__':
    path = 'data/'
    dates = os.listdir(path)
    dates.sort()
    dates = dates[1:]
    f = open('data_sets.csv', 'w', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(['日期', '标题', '分数', '标签'])
    for date in dates:
        dir_name = path + date + '/'
        news = os.listdir(dir_name)
        for each in news:
            raw_content = get_article(dir_name + each)
            content = remove(raw_content)
            sc = get_score(content)  # 分数
            writer.writerow([date, each, sc])
        print(date + ' done')
    f.close()
