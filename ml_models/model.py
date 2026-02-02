import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
  # Input Layer   -> 9 (dropping studentID)
  # Hidden Layer1 -> 12
  # Hidden Layer2 -> 12
  # Hidden Layer3 -> 24
  # Hidden Layer4 -> 16
  # Output        -> 2 (True/False)

  def __init__(self, inp, h1, h2, h3, h4,  out) -> None:
    super().__init__()

    self.fc1 = nn.Linear(inp,h1)
    self.fc2 = nn.Linear(h1,h2)
    self.fc3 = nn.Linear(h2, h3)
    self.fc4 = nn.Linear(h3, h4)
    self.out = nn.Linear(h4, out)

  def forward(self, x): # shape of x = (batch_size, inp)
    x = F.relu(self.fc1(x)) # xnew​=x⋅WT+b -> shape of x changes -> shape(x) = (batch_size, h1)
    x = F.relu(self.fc2(x)) # shape(x) = (batch_size, h2)
    x = F.relu(self.fc3(x)) # shape(x) = (batch_size, h3)
    x = F.relu(self.fc4(x)) # shape(x) = (batch_size, h4)
    x = self.out(x) # shape(x) = (batch_size, out)

    return x