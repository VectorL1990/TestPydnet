import torch

x = torch.ones(2,2,requires_grad=True)
y = x + 2
z = y*y*3
z = z.mean()
#print(z)
print(z)
z.backward()
print(x.grad)

#print(z.grad_fn)
