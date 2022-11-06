from Data import BCDataset

X = ['radius_mean','symmetry_mean', 'concavity_mean']
y = 'diagnosis'

train_df, test_df = train_test_split(dataframe, test_size = 0.2, random_state = 1)

X_train = train_df[X]
y_train = train_df[y]
X_test = test_df[X]
y_test = test_df[y]

model = linear_model.LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
test_df['predicted'] = y_pred.squeeze()
sns.catplot(x = X[0], y = 'diagnosis_cat', hue = 'predicted', data=test_df, order=['1 (malignant)', '0 (benign)'])

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
