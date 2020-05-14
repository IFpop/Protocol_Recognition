import os
import pandas as pd

# filename为文件路径，scale为比例

def split(filename,scale):
    # 设置每个文件需要有的行数,初始化为1000W
    chunksize=10000
    data1=pd.read_table(filename,chunksize=chunksize,sep=',',encoding='gbk')
    # print(data1)
    # num表示总行数
    num=0
    for chunk in data1:
        num+=len(chunk)
    # print(num)
    # chunksize表示每个文件需要分配到的行数
    chunksize1=round(num*scale)
    # print(chunksize)
    # 分离文件名与扩展名os.path.split(filename)
    data2=pd.read_table(filename,chunksize=chunksize1,sep=',',encoding='gbk')
    i='train'
    for chunk in data2:
        chunk.to_csv('{0}.csv'.format(i),header=None,index=False)
        # print('保存第{0}个数据'.format(i))
        i = 'verify'

if __name__ == '__main__':
    split('./data.csv', 0.8)

