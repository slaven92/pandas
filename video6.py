import pandas as pd
df  = pd.read_csv("Y:\\Slaven\\pythonStuff\\projects\\pandas\\diamonds\\diamonds.csv", index_col=0)
df.head()

# %%
df["cut"].unique()
# df["cut"].astype("category").cat.codes
cut_class_dict = {"Fair": 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}
clarity_dict = {"I3": 1, "I2": 2, "I1": 3, "SI2": 4, "SI1": 5, "VS2": 6, "VS1": 7, "VVS2": 8, "VVS1": 9, "IF": 10, "FL": 11}
color_dict = {"J": 1,"I": 2,"H": 3,"G": 4,"F": 5,"E": 6,"D": 7}

# %%
df['cut'] = df['cut'].map(cut_class_dict)
df['clarity'] = df['clarity'].map(clarity_dict)
df['color'] = df['color'].map(color_dict)
df.head()
# %%
import sklearn
from sklearn import svm, preprocessing

df = sklearn.utils.shuffle(df)

X = df.drop("price", axis=1).values
X = preprocessing.scale(X)
y = df['price'].values

test_size = 200

X_train = X[:-test_size]
y_train = y[:-test_size]

X_test = X[-test_size:]
y_test = y[-test_size:]

clf = svm.SVR(kernel='linear')
clf.fit(X_train, y_train)

# %%
clf.score(X_test,y_test)

# %%

for X,y in zip(X_test, y_test):
    print(f"Model: {clf.predict([X])[0]}, Actual: {y}")

# %% rbf kernal

clf2 = svm.SVR(kernel='rbf')
clf2.fit(X_train, y_train)
clf2.score(X_test,y_test)
for X,y in zip(X_test, y_test):
    print(f"Model: {clf2.predict([X])[0]}, Actual: {y}")
