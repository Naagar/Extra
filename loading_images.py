#  loading Images


import matplotlib.pyplot as plt
import torch
from torchvision import datasets, transforms


data_dir = 'images'

#Applying Transformation
data_transforms = transforms.Compose([
                                transforms.RandomRotation(30),
                                transforms.RandomResizedCrop(128),
                                transforms.RandomHorizontalFlip(),
                                transforms.ToTensor()])

# test_transforms = transforms.Compose([transforms.Resize(255),
#                                       transforms.CenterCrop(224),
#                                       transforms.ToTensor()])
data = datasets.ImageFolder(data_dir,  
                                    transform=train_transforms)                                       
# test_data = datasets.ImageFolder(data_dir + ‘/test’, 
#                                     transform=test_transforms)

#Data Loading
data_loader = torch.utils.data.DataLoader(train_data,
                                                   batch_size=32)
# testloader = torch.utils.data.DataLoader(test_data, batch_size=32)


