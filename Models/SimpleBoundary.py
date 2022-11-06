import BCDataset

def boundary_classifier(target_boundary, radius_mean_series):
  predictions = []
  for radius_mean in radius_mean_series:
    if radius_mean > target_boundary:
      predictions.append(1)
    else:
      predictions.append(0)
  return predictions

chosen_boundary = 15 #Changeable value

y_pred = boundary_classifier(chosen_boundary, dataframe['radius_mean'])
dataframe['predicted'] = y_pred

y_true = dataframe['diagnosis']

sns.catplot(x = 'radius_mean', y = 'diagnosis_cat', hue = 'predicted', data = dataframe, order=['1 (malignant)', '0 (benign)'])
plt.plot([chosen_boundary, chosen_boundary], [-.2, 1.2], 'g', linewidth = 2)

accuracy = accuracy_score(y_true,y_pred)
print(accuracy)
