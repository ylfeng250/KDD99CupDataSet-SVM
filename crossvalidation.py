from sklearn import cross_validation
from sklearn import svm


def read_data(filename):
    train_set = []
    label_set = []
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip('\n').split(',')
            train_set.append(line[:-1])
            label_set.extend([line[-1]])
    return train_set,label_set


clf = svm.SVC(kernel='linear', C=100)  # 创建分类器
train_set,label_set = read_data("second.kddcup.data.corrected.csv")
# print(len(train_set))
# print(len(label_set))
score = cross_validation.cross_val_score(clf, train_set, label_set, cv=5, scoring='accuracy')

print(score)

with open('crossvalidation.txt','a') as f:
    f.write(str(score))
