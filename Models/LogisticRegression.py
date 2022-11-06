from sklearn.model_selection import train_test_split
from Data import BCDataset

train_df, test_df = train_test_split(dataframe, test_size = 0.2, random_state = 1)

X = ['radius_mean']
y = 'diagnosis'

X_train = train_df[X]
print('X_train, our input variables:')
print(X_train.head())
print()

y_train = train_df[y]
print('y_train, our output variable:')
print(y_train.head())

logreg_model = linear_model.LogisticRegression()
logreg_model.fit(X_train, y_train)

X_test = test_df[X]
print("X_test:")
print(X_test.head())
print()
y_test = test_df[y]
print("y_test:")
print(y_test.head())

y_pred = logreg_model.predict(X_test)
test_df['predicted'] = y_pred.squeeze()
sns.catplot(x = X[0], y = 'diagnosis_cat', hue = 'predicted', data=test_df, order=['1 (malignant)', '0 (benign)'])

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# Visualize probabilities for 'X_test'
y_prob = logreg_model.predict_proba(X_test)
X_test_view = X_test[X].values.squeeze()
plt.xlabel('radius_mean')
plt.ylabel('Predicted Probability')
sns.scatterplot(x = X_test_view, y = y_prob[:,1], hue = y_test, palette=['purple','green'])
