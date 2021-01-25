import numpy as np
from sklearn import svm
from sklearn import model_selection
import os
import csv

data = np.loadtxt('data_final.csv', str, delimiter=',')
labeled_data = data[1: 301]  # 该部分数据是人工打上标签的数据
# 分割X和y数据
X, y = np.split(labeled_data, (2,), axis=1)

# 分割训练集和测试集，测试集数据占30%
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, random_state=1, test_size=0.3)

# 开始训练，经多次测试发现gamma=10，C=0.8时效果较好
clf = svm.SVC(kernel='rbf', gamma=10, decision_function_shape='ovo', C=0.8)
clf.fit(X_train, y_train)

# 预测测试数据标签
print('预测结果：')
predict_list = clf.predict(X_test)
for i in range(len(X_test)):
    print(str(i + 1) + '.特征参数' + str(X_test[i]) + ': ' + str(int(predict_list[i])))
print()

# 输出准确率
print("SVM训练集的准确率为：", clf.score(X_train, y_train))
print("SVM测试集的准确率为：", clf.score(X_test, y_test))

unlabeled_data = data[301:]
unlabeled_data = unlabeled_data[:, :2]
predict_list = clf.predict(unlabeled_data)
with open(os.path.join(os.path.dirname(__file__), 'data_final.csv')) as csvFile:
    rows = csv.reader(csvFile)
    with open(os.path.join(os.path.dirname(__file__), 'result.csv'), 'w') as f:
        count = 0
        writer = csv.writer(f)
        for row in rows:
            if count < 301:
                writer.writerow(row)
                count += 1
            else:
                row[2] = predict_list[count - 301]
                writer.writerow(row)
                count += 1
