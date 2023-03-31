import torch
import torch.nn as nn
import torch.nn.functional as torchFunc

class Net(nn.Module):
  def __init__(self):
    super(Net, self).__init__()

    self.conv1 = nn.Conv2d(1,3,3)
    #self.conv2 = nn.Conv2d(6,16,3)

    #self.fc1 = nn.Linear(16*6*6,120)
    #self.fc2 = nn.Linear(120,84)
    #self.fc3 = nn.Linear(84,10)

  def forward(self, x):
    x = torchFunc.relu(self.conv1(x))

    #x = torchFunc.max_pool2d(torchFunc.relu(self.conv1(x)), 2)
    #x = torchFunc.max_pool2d(torchFunc.relu(self.conv2(x)), 2)

    #x = x.view(-1, 16*6*6)
    #x = torchFunc.relu(self.fc1(x))
    #x = torchFunc.relu(self.fc2(x))

    #x = self.fc3(x)

    return x

  def randInput(self):
    x = torch.rand(1, 32, 32)
    print(x.size())
    y = x.unsqueeze(0)
    print(y.size())
    z = torch.unsqueeze(x, 0)
    print(z.size())

net = Net()
print(net)

x = torch.rand(1,3,3)
print(x)
out = net(x)
print(out)

for parameters in net.named_parameters():
  print(name, ":", parameters.)

#target = torch.rand(1,10)
#loss_func = nn.MSELoss()
#loss = loss_func(out, target)
#print(loss)

#net.zero_grad()
#loss.backward()
#print(net.conv1.bias.grad)
