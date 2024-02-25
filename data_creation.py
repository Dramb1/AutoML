import torchvision


if __name__ == "__main__":
    torchvision.datasets.CIFAR10(root='./train', train=True, download=True)
    torchvision.datasets.CIFAR10(root='./test', train=False, download=True)