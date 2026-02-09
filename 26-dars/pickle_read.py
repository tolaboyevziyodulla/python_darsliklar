import pickle

with open('info.pcl', 'rb') as file:
    student1 = pickle.load(file)
    student2 = pickle.load(file)

print(student1)
print(student2)