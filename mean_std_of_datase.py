import torch
from torchvision import datasets, transforms
from torch.utils.data import Dataset, DataLoader

from load_data import seeds_dataset                          # load the data Set


# dataset = datasets.ImageFolder('train',
#                  transform=transforms.ToTensor())

batch_size = 256  

train_txt_path='data/train_data_file.csv' 
train_img_dir='data/train'
test_text_path='data/test_data_file.csv'
test_img_dir='data/validation'

# Load dataset. train and test
train_dataset = seeds_dataset(train_txt_path,train_img_dir)
test_dataset = seeds_dataset(test_text_path,test_img_dir)

train_loader = DataLoader(train_dataset, batch_size=batch_size)
validation_loader = DataLoader(test_dataset, batch_size=batch_size)


mean = 0.
std = 0.
for images, _ in validation_loader :
    batch_samples = images.size(0) # batch size (the last batch can have smaller size!)
    images = images.view(batch_samples, images.size(1), -1)
    mean += images.mean(2).sum(0)
    std += images.std(2).sum(0)

mean /= len(validation_loader.dataset)
std /= len(validation_loader.dataset)

print(f'Mean: {mean}')

print(f'Std: {std}')
