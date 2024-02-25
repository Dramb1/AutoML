import pickle

import torch
import torchvision
import torchvision.transforms as transforms


transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
batch_size = 4


if __name__ == "__main__":
    trainset = torchvision.datasets.CIFAR10(
        root='./train', train=True, transform=transform
    )
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=batch_size, shuffle=True, num_workers=2
    )

    testset = torchvision.datasets.CIFAR10(
        root='./test', train=False, transform=transform
    )
    testloader = torch.utils.data.DataLoader(
        testset, batch_size=batch_size, shuffle=False, num_workers=2
    )

    with open('./train/trainloader.pkl', 'wb') as fp:
        pickle.dump(trainloader, fp)

    with open('./test/testloader.pkl', 'wb') as fp:
        pickle.dump(testloader, fp)
