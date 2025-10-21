import pandas as pd

from matplotlib import pyplot as plt


df = pd.read_csv("C:/Users/Mahin/OneDrive/Documents/MachineLearning/insurance.csv")
X = df[['age']]
y = df[['Insurance']]

from sklearn.model_selection import train_test_split

X_train , X_text , y_train , y_test = train_test_split(X,y ,test_size= 0.2 , random_state= 42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train,y_train)

prediction = model.predict(X_text)


plt.scatter(X_text, y_test, color='blue', label='Actual values')
plt.scatter(X_text, prediction, color='red', label='Predicted values')

# best fit line
plt.plot(X_text, prediction, color='green', linestyle='-', label='Best Fit Line')

# Adding labels and title
plt.xlabel('Age')
plt.ylabel('No of Insurance')
plt.title('Best Fit Line')
plt.legend()
plt.show()
