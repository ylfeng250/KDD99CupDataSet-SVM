# KDD99CupDataSet-SVM
clean data ,feature selection , svm based kdd99

## 数据清洗

数据集来源:KDD99入侵检测数据集 [http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

* 筛选出发生在TCP层的Dos流量和normal流量 `get_train_data.py`
其中Dos流量的标签`'back.', 'land.', 'neptune.','smurf.', 'teardrop.', 'pod.'`
normal流量的标签`'normal.'`
生成文件`dos.kddcup.data.corrected.csv`
最后标签类别如下
normal -> 1 attack -> -1

|normal|attack|
|:----|:----- |
| 768670|1074241|

* 通过统计特征进行数据筛选 `wrap_up.py`

* 随机森林对特征重要性进行排序
```
 [(0.9824, 'same_srv_rate'), (0.0106, 'dst_host_serror_rate'), (0.0011, 'count'), (0.0009, 'srv_count'), (0.0009, 'dst_host_same_src_port_rate'), (0.0008, 'dst_host_count'), (0.0007, 'dst_host_srv_count'), (0.0005, 'dst_host_srv_rerror_rate'), (0.0005, 'dst_host_diff_srv_rate'), (0.0003, 'dst_host_srv_serror_rate'), (0.0003, 'dst_host_rerror_rate'), (0.0002, 'srv_rerror_rate'), (0.0002, 'dst_host_srv_diff_host_rate'), (0.0001, 'srv_serror_rate'), (0.0001, 'srv_diff_host_rate'), (0.0001, 'serror_rate'), (0.0001, 'dst_host_same_srv_rate'), (0.0, 'rerror_rate'), (0.0, 'diff_srv_rate')]
```
 |label|rate|text|
 |:----|:----|:----|
 |same_srv_rate|0.9824|过去两秒内，与当前连接具有相同目标主机的连接中，与当前连接具有相同服务的百分比|
 |dst_host_serror_rate|0.0106|前100个连接中，与当前连接具有相同目标主机的连接中，出现SYN错误的连接所占的百分比|
 |count|0.0011|过去两秒内，与当前连接具有相同的目标主机的连接数|
 |srv_count|0.0009|过去两秒内，与当前连接具有相同服务的连接数|
 |dst_host_same_src_port_rate|0.0009|前100个连接中，与当前连接具有相同目标主机相同源端口的连接所占的百分比|
 |dst_host_count|0.0008|前100个连接中，与当前连接具有相同目标主机的连接数|
 |dst_host_srv_count|0.0007|前100个连接中，与当前连接具有相同目标主机相同服务的连接数|
 |dst_host_srv_rerror_rate|0.0005|前100个连接中，与当前连接具有相同目标主机相同服务的连接中，出现REJ错误的连接所占的百分比|
 |dst_host_diff_srv_rate|0.0005|前100个连接中，与当前连接具有相同目标主机不同服务的连接所占的百分比|
 |dst_host_srv_serror_rate|0.0003|前100个连接中，与当前连接具有相同目标主机相同服务的连接中，出现SYN错误的连接所占的百分比|
 |dst_host_rerror_rate|0.0003|前100个连接中，与当前连接具有相同目标主机的连接中，出现REJ错误的连接所占的百分比|
 |srv_rerror_rate|0.0002|过去两秒内，在与当前连接具有相同服务的连接中，出现“REJ” 错误的连接的百分比|
 |dst_host_srv_diff_host_rate|0.0002|前100个连接中，与当前连接具有相同目标主机相同服务的连接中，与当前连接具有不同源主机的连接所占的百分比|
 |srv_serror_rate|0.0001|过去两秒内，在与当前连接具有相同服务的连接中，出现“SYN” 错误的连接的百分比|
 |srv_diff_host_rate|0.0001|过去两秒内，在与当前连接具有相同服务的连接中，与当前连接具有不同目标主机的连接的百分比|
 |serror_rate|0.0001|过去两秒内，在与当前连接具有相同目标主机的连接中，出现“SYN” 错误的连接的百分比|
 |dst_host_same_srv_rate|0.0001|前100个连接中，与当前连接具有相同目标主机相同服务的连接所占的百分比|
 |rerror_rate|0.0|过去两秒内，在与当前连接具有相同目标主机的连接中，出现“REJ” 错误的连接的百分比|
 |diff_srv_rate|0.0|过去两秒内，在与当前连接具有相同目标主机的连接中，与当前连接具有不同服务的连接的百分比|


## 5折交叉验证结果

```
[0.99440018 0.99969071 0.99905041 0.99903956 0.99788378]
```

## 

* get_train_data.py 第一步
* get_train_data2.py 第二步
* get_train_data3.py 第三步
* wrap_up.py 统计特征信息
* crossvalidation.py 交叉验证