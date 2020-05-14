import time

import torch
from torch.utils.data import DataLoader

from malwareAnalysis.api.DataSet import MyDataSet
from malwareAnalysis.config.Config import configuration
from malwareAnalysis.module.CnnModule import DenseNet_BC


def TestModule(moduleFrom, dataFrom, resultTo):

################### config #####################

    batch_size = int(configuration.batchSize)
    EPOCH = int(configuration.EPOCH)
    LR = float(configuration.LR)

################################################

################### init ######################

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    cnn = DenseNet_BC().to(device)
    # optimizer
    optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)

###############################################


    cnn.load_state_dict(torch.load(moduleFrom))

    ######################输入测试集的位置和名
    dataset = MyDataSet(dataFrom)
    dataLoader = DataLoader(dataset, batch_size=batch_size, shuffle=False)


    with open(resultTo, "a") as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.write('\n')
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        numTest = 0
        numCorrect = 0
        iteration = 0
        with torch.no_grad():
            for data in dataLoader:
                img, label = data
                img = img.view(img.size(0), 1, 28, 28)
                img = img.float()
                cnn.eval()
                img = img.to(device)
                label = label.to(device)
                out = cnn(img)
                _, pred = torch.max(out.data, 1)
                numCorrect += (pred == label).sum()
                numTest = numTest + label.size(0)

        finalCorrect = float(numCorrect.item()) / float(numTest)

        f.write("Epoch= %02d,Iter= %03d,Accuracy= %.4f" % (EPOCH, iteration, finalCorrect))
        f.write('\n')
        f.flush()

    return finalCorrect