import pickle
f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)
print(data[1])
print(data[2])