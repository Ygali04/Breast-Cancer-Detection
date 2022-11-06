from sklearn import metrics
from Models import MultiVarLogisticRegression

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)

class_names = [0,1] # Diagnosis labels

fig, ax = plt.subplots()

tick_marks = np.arange(len(class_names)) 
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g') # Creating heatmap
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y = 1.1)
plt.ylabel('Actual diagnosis')
plt.xlabel('Predicted diagnosis')
