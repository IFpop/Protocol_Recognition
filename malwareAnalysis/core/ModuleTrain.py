import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from malwareAnalysis.api.DataSet import MyDataSet
from malwareAnalysis.config.Config import configuration
from malwareAnalysis.module.CnnModule import DenseNet_BC
from malwareAnalysis.utils.splite import split


def ModuleTrain(dataFrom, moduleTo):

################### config #####################

    batch_size = int(configuration.batchSize)
    EPOCH = int(configuration.EPOCH)
    LR = float(configuration.LR)

################################################

################### init ######################

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    cnn = DenseNet_BC().to(device)
    # optimizer
    optimizer = torch.optim.Adam(cnn.parameters(), lr=LR, betas=(0.9, 0.999))

###############################################



    # split(dataFrom)
    trainData = MyDataSet(dataFrom)
    trainDataLoader = DataLoader(trainData, batch_size=batch_size, shuffle=True)
    # verifyData = MyDataSet('../utils/verify.csv')
    # verfyDataLoader = DataLoader(verifyData, batchSize=batchSize, shuffle=True)



    # loss_fun
    loss_func = nn.CrossEntropyLoss()
    loss_count = []
    # training loop
    with open(moduleTo, "a") as f:
        for epoch in range(EPOCH):
            for i, trainData in enumerate(trainDataLoader):

                if (i == 200):
                    break
                x, y = trainData
                x = x.view(x.size(0), 1, 28, 28)
                x = x.float()
                x = x.to(device)
                y = y.to(device)
                # 输入训练数据
                output = cnn(x)
                cnn.train()
                # 清空上一次梯度
                optimizer.zero_grad()
                # 计算误差
                loss = loss_func(output, y)
                # 误差反向传递
                loss.backward()
                iter_loss = loss.item()
                # 优化器参数更新
                optimizer.step()
                _, predlabel = torch.max(output.data, 1)
                correct = (predlabel == y).sum()
                iter_total = y.size(0)
                f.write('Epoch:%03d   iter:%05d | Loss:%.03f | Acc:%.3f'
                        % (epoch + 1, i + 1, float(iter_loss), float(correct) / iter_total))
                f.write('\n')
                f.flush()
                if i > 0 and i % 20 == 19:
                    loss_count.append(loss)
                    # print('{}:\t'.format(i), loss.item())
                    torch.save(cnn.state_dict(), './DenseNet.pt')


