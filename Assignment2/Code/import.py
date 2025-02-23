import mnist_reader #DATA\fashion-mnist\utils\mnist_reader.py
import some crazy shit

X_train, y_train = mnist_reader.load_mnist('../DATA/fashion-mnist/data/fashion', kind='train')
X_test, y_test = mnist_reader.load_mnist('../DATA/fashion-mnist/data/fashion', kind='t10k')

print(X_train.head())

