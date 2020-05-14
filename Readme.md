# Start

## 数据集格式

### Train数据集

| label | 0~783  |
| ----- | ------ |
| 0~9   | 字节码 |

### Test数据集

| 0~783  |
| ------ |
| 字节码 |

## 简易使用

+ 测试模型

  ```bash
  python3 start.py -T  -m ./malwareAnalysis/module/DenseNet.pt  -d ./malwareAnalysis/data/test.csv -t ./ans.log
  ```

+ 训练模型

  ```bash
  python3 start.py -M -d ./malwareAnalysis/data/train.csv -t ./module/DenseNet.pt
  ```


 