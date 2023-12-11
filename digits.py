from tinygrad.helpers import Timing
import numpy as np
from tinygrad.nn import Linear
from tinygrad.tensor import Tensor
from tinygrad.nn.optim import SGD
from tinygrad.nn.state import get_parameters, safe_save, safe_load, get_state_dict, load_state_dict
from extra.datasets import fetch_mnist


np.set_printoptions(linewidth=28*6)

class TinyNet:
    def __init__(self):
        self.l1 = Linear(784, 128, bias=False)
        self.l2 = Linear(128, 10, bias=False)

    def __call__(self, x):
        x = self.l1(x);
        x = x.leakyrelu()
        x = self.l2(x)
        # x = x.leakyrelu()
        # x = self.l3(x)
        return x


net = TinyNet()

#Tensor.sparse_categorical_crossentropy


# essas duas linhas sao iguais
#opt = SGD([net.l1.weight, net.l2.weight], lr=3e-4)
opt = SGD(get_parameters(net), lr=3e-4)


X_train, Y_train, X_test, Y_test = fetch_mnist()

print(X_train[1].T)
print(Y_train[1])
print(type(X_train))

# treina e salva os parametros
# with Tensor.train():
#     for step in range(1000):
#         sample = np.random.randint(0, X_train.shape[0], size=(64))
#         batch = Tensor(X_train[sample], requires_grad=False)
#         labels = Tensor(Y_train[sample])

#         out = net(batch)

#         loss = Tensor.sparse_categorical_crossentropy(out, labels)

#         opt.zero_grad()

#         loss.backward()
#         opt.step()


#         pred = out.argmax(axis=-1)
#         acc = (pred == labels).mean()

#         if step % 100 == 0: 
#             print(f"Step {step+1} | Loss: {loss.numpy()} | Acc: {acc.numpy()}")

# state_dict = get_state_dict(net)
# safe_save(state_dict, "teste.safetensors")


# carrega os parametros salvos
# state_dict = safe_load("teste.safetensors")
# load_state_dict(net, state_dict)



#testa
# with Timing("Time: "):
#     avg_acc = 0
#     for step in range(1000):
#         sample = np.random.randint(0, X_test.shape[0], size=(64))
#         batch = Tensor(X_test[sample], requires_grad=False)

#         labels = Y_test[sample]
#         out = net(batch)

#         pred = out.argmax(axis=-1).numpy()
#         avg_acc += (pred == labels).mean()
#     print(f"Test ACc: {avg_acc / 1000}")



