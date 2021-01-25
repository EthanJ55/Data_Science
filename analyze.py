import matplotlib.pyplot as plt  # 引入绘图库

if __name__ == '__main__':

    # 打开文本文件 读取数据
    with open("result.csv", 'r', encoding='utf-8') as f:
        data_lines = f.readlines()

    table = []
    for i in range(1, len(data_lines)):
        temp = data_lines[i].split(',')
        time = int(temp[0].split('/')[1])
        score = float(temp[2])
        if temp[3] == '100':
            area = 1
        else:
            area = 0
        label = int(temp[4])
        table.append([time, score, area, label])
    print(table)
    l_score = []
    l_civil = []
    l_foreign = []
    l_area = []
    l_label = []
    month = 1
    sum_score = table[0][1]
    sum_label = table[0][2]
    civil = 1
    foreign = 0
    ind = 0
    count = 1
    while ind <= len(table):
        if ind == len(table):
            l_score.append(sum_score/count)
            l_civil.append(civil)
            l_foreign.append(foreign)
            l_label.append(sum_label/count)
            break
        elif table[ind][0] == month:
            sum_score += table[ind][1]
            sum_label += table[ind][3]
            if table[ind][2] == 0:
                foreign += 1
            else:
                civil += 1
            ind += 1
            count += 1
        else:
            l_score.append(sum_score / count)
            l_civil.append(civil)
            l_foreign.append(foreign)
            l_label.append(sum_label / count)
            l_area.append(civil / foreign)
            month = table[ind][0]
            sum_score = table[ind][1]
            sum_label = table[ind][3]
            if table[ind][2] == 0:
                civil = 0
                foreign = 1
            else:
                civil = 1
                foreign = 0
    months = [i for i in range(1, 13)]

    # 情感分数
    plt.plot(months, l_score, 'o-', color='r', linestyle='--')
    plt.xlabel('month')
    plt.ylabel('score')
    plt.text(months[-1], l_score[-1], l_score[-1], ha='right', va='top', fontsize=10)
    plt.show()

    # 情感标签
    plt.plot(months, l_label, 'o-', color='r', linestyle='--')
    plt.xlabel('month')
    plt.ylabel('label')
    plt.text(months[-1], l_label[-1], l_label[-1], ha='right', va='top', fontsize=10)
    plt.show()

    # 国内外新闻数量
    plt.plot(months, l_civil, 'o-', color='r', linestyle='--')
    plt.plot(months, l_foreign, 'o-', color='b', linestyle='--')
    plt.xlabel('month')
    plt.ylabel('area')
    plt.text(months[-1], l_civil[-1], l_civil[-1], ha='right', va='top', fontsize=10)
    plt.text(months[-1], l_foreign[-1], l_foreign[-1], ha='right', va='top', fontsize=10)
    plt.show()
