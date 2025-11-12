from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
clf = DecisionTreeClassifier()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy of Decision Tree Classifier:",accuracy)
print("Enter the sample data")
a=int(input("Enter sepal length in cm="))
b=int(input("Enter sepal width in cm="))
c=int(input("Enter petal length in cm="))
d=int(input("Enter petal width in cm="))
sample=[[a,b,c,d]]
pred=clf.predict(sample)
pred_v=[iris.target_names[p] for p in pred]
print(pred_v)

plt.figure(figsize=(35,30))
plot_tree(clf,filled=True,rounded=True,class_names=iris.target_names,feature_names=iris.feature_names,fontsize=10)
plt.show()
