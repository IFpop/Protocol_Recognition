import torch
import pandas
import warnings
warnings.filterwarnings("ignore")

# 定义是否使用GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def process(modul,data_loader,threshold=0.98):
    num_correct = 0
    size = 0
    label = list()
    with torch.no_grad():
        for data in data_loader:
            modul.eval()
            img = data
            img = img.view(img.size(0), 1, 28, 28)
            img = img.float()
            modul.eval()

            img = img.to(device)
            out = modul(img)

            outputprobability = torch.exp(out) / torch.sum(torch.exp(out), dim=1).unsqueeze(1)
            probability, number = torch.max(outputprobability.data, 1)
            for i in range(len(data)):
                if probability[i].item() > threshold:
                    label.append(number[i].item())
                else:
                    label.append(404)

    return label

