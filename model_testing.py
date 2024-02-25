import pickle
import torch

from model_preparation import Net


if __name__ == "__main__":
    with open('./train/model.pkl', 'rb') as fp:
        net = pickle.load(fp)
    with open('./test/testloader.pkl', 'rb') as fp:
        testloader = pickle.load(fp)

    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')