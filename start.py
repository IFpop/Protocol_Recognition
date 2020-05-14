# coding: utf-8
"""UserManage
Usage:
   start.py (-h | --help)
   start.py (-v | --version)
   start.py (-P | --PreProcessData) (-d | --data) <dataLocation> (-t | --to) <toDataLocation>
   start.py (-M | --ModuleTrain) (-d | --data) <dataLocation> (-t | --to) <toModuleLocation>
   start.py (-T | --TestModule) (-m | --module) <moduleLocation> (-d | --data) <dataLocation> (-t | --to) <toResultLocation>
   start.py (-I | --IdentifyData) (-m | --module) <moduleLocation> (-d | --data) <dataLocation> (-t | --to) <toResultLocation>


Options:
  -h --help            帮助.
  -v --version         查看版本号.
  -l --label           是否需要label
  -m --module          模型文件位置
  -d --data            数据文件位置
  -t --to              处理完数据（模型）（结果）位置
  -P --PreProcessData  预处理数据
  -M --ModuleTrain     训练模型
  -T --TestModule      测试模型
  -I --IdentifyData    识别数据
  @Author Aerfafish
  @Version 1.0
"""

from docopt import docopt
import torch
import warnings

import torch.nn as nn

from malwareAnalysis.module.CnnModule import DenseNet_BC

warnings.filterwarnings("ignore")
torch.manual_seed(1)


EPOCH = 1
BATCH_SIZE = 50
LR = 0.001
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments['--PreProcessData']:
        from malwareAnalysis.core import PreprocessData
        PreprocessData.preprocessData(arguments['<dataLocation>'], arguments['<toDataLocation>'])

    elif arguments['--ModuleTrain']:
        from malwareAnalysis.core import ModuleTrain
        ModuleTrain.ModuleTrain(arguments['<dataLocation>'], arguments['<toModuleLocation>'])

    elif arguments['--TestModule']:
        from malwareAnalysis.core import TestModule
        TestModule.TestModule(arguments['<moduleLocation>'] ,arguments['<dataLocation>'], arguments['<toResultLocation>'])

    elif arguments['--IdentifyData']:
        from malwareAnalysis.core import IdentifyData
        IdentifyData.IdentifyData(arguments['<moduleLocation>'], arguments['<dataLocation>'], arguments['<toResultLocation>'])

