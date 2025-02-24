def load_mnist(path, kind='train'):


    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte.gz'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte.gz'
                               % kind)

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8,
                               offset=8)

    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8,
                               offset=16).reshape(len(labels), 784)

    return images, labels

    #what do I want to do?
#decide what k is -> ie how many sample sizes Ill have
def kfcv(x, y, model, k):
  score_list = []
  size = len(x)
  #print(size)
  indices = np.array(range(size))
  #print(indices)
  np.random.shuffle(indices)
  #print(indices)

  fold = np.array_split(indices, k)
  #print(fold)

  for i in range(k):
    fold_values = fold[i]


    train_indices = np.concatenate(fold[:i] + fold[i+1:])
    #print(train_indices)
    validation_indices = fold[i]
    #print(validation_indices)



    x_validation, y_validation = x[validation_indices], y[validation_indices]
    #print(f"VALIDATION SHAPE IS : {x_validation.shape}")
    x_temp, y_temp = x[train_indices], y[train_indices]
    #print(f"TRAIN SHAPE IS : {x.shape}")
    model.fit(x, y)
    score_list.append(1-model.score(x_validation, y_validation))

  return score_list

def main():
    file_path = '/content/drive/MyDrive/Colab Notebooks/SENG 474/Assignment2/Assignment2/DATA/fashion-mnist/data/fashion'

    #load data
x_train, y_train = load_mnist(file_path, kind='train')
x_test, y_test = load_mnist(file_path, kind='t10k')

#setup filter for 5 & 7 results
x_train_filtered = []
y_train_filtered = []

#filter og test dataset and grab only 5 or 7 and set to binary classification
for i in range(0,len(x_train)):
  if(y_train[i] == 5):
    x_train_filtered.append(x_train[i])
    y_train_filtered.append(0)
  elif(y_train[i] == 7):
    x_train_filtered.append(x_train[i])
    y_train_filtered.append(1)

    #setup filter for 5 & 7 results
x_test_filtered = []
y_test_filtered = []

#filter og test dataset and grab 5 and 7 to binary classification
for i in range(0,len(x_test)):
  if(y_test[i] == 5):
    x_test_filtered.append(x_test[i])
    y_test_filtered.append(0)
  elif(y_test[i] == 7):
    x_test_filtered.append(x_test[i])
    y_test_filtered.append(1)

#convert to np array
x_train_filtered = np.array(x_train_filtered)
y_train_filtered = np.array(y_train_filtered)
x_test_filtered = np.array(x_test_filtered)
y_test_filtered = np.array(y_test_filtered)

#pull 2000 examples from training set of 12000
x_train = x_train_filtered[:2000]
y_train = y_train_filtered[:2000]
x_test = x_test_filtered
y_test = y_test_filtered

#normalize
#might be worth having [-1, 1] and [0,1]

x_train = x_train / 255.0
x_test = x_test / 255.0

#c value test 
c_value_list = [0.0001, 0.001, 0.01,0.1,1,10,100,1000,10000]

#c_value_list = c_list
#C0 > 0 and b > 1
#so c0 at 0.001
#then b starts at 2 and goes

c_loss_train_list = []
c_loss_test_list = []

for c in c_value_list:
  #new_c = math.log(c)

  svm = SVC(kernel='linear', C=c)
  c_loss_train_list.append(kfcv(x_train, y_train, svm, 10))
  c_loss_test_list.append(1-svm.score(x_test, y_test))


if __name__ == "__main__":
    main()