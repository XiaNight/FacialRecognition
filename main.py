import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import autokeras as ak

# load data
train_data = np.load('train_data.npy')
test_data = np.load('test_data.npy')

# split data
X_train, X_test, y_train, y_test = train_test_split(
    train_data, test_data, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


fig = plt.figure()
bin = np.arange(3)

ax = fig.add_subplot(1, 2, 1)
ax.set_xticks(bin)
plt.hist(y_train, bins=bin, edgecolor='black')
plt.title('Train Data')

ax = fig.add_subplot(1, 2, 2)
ax.set_xticks(bin)
plt.hist(y_test, bins=bin, edgecolor='black')
plt.title('Test Data')

plt.show()
