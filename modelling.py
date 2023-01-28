from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_grid_classifier(search_result, X_test, y_test, X_train, y_train, pos_label='1',model_name='Grid search', confusion_matrix=True):
    """
    Print evaluation metrics of the best classifier estimator found from the grid search.
        * recall
        * precision
        * F1
        * AUC score (only if class labels are integers)
    Plot:
        * confusion matrix
        * ROC (only if class labels are integers)
    Parameters:
    - pos_label (str or int): Class label for positive class. Default is 1.
    - model_name (string, optional): Name of model printing purposes.

    Returns evaluation metrics for test data set as a dictionary
    """
    
    best_model = search_result.best_estimator_

    y_pred = best_model.predict(X_test)

    y_pred_train = best_model.predict(X_train)

    # Metrics for test data
    recall = recall_score(y_test, y_pred, pos_label=pos_label)
    precision = precision_score(y_test, y_pred, pos_label=pos_label)
    f1score = f1_score(y_test, y_pred, pos_label=pos_label)
    accuracy = accuracy_score(y_test, y_pred)
    metrics = {
        'recall': recall,
        'precision': precision,
        'f1' : f1score,
        'accuracy': accuracy
    }

    # Metrics for training data
    recall_train = recall_score(y_train, y_pred_train, pos_label=pos_label)
    precision_train = precision_score(y_train, y_pred_train, pos_label=pos_label)
    f1score_train = f1_score(y_train, y_pred_train, pos_label=pos_label)
    accuracy_train = accuracy_score(y_train, y_pred_train)

    print(f'\n{model_name} evaluation metrics: \n\tTest data\tTraining data\t\tDifference')
    print(f'Accuracy: \t{100*accuracy:.2f}%\t\t{100*accuracy_train:.2f}%\t\t{100*(accuracy-accuracy_train):.2f}%')
    print(f'Recall: \t{100*recall:.2f}%\t\t{100*recall_train:.2f}%\t\t{100*(recall-recall_train):.2f}%')
    print(f'Precision: \t{100*precision:.2f}%\t\t{100*precision_train:.2f}%\t\t{100*(precision-precision_train):.2f}%')
    print(f'F1: \t\t{100*f1score:.2f}%\t\t{100*f1score_train:.2f}%\t\t{100*(f1score-f1score_train):.2f}%')
    if type(y_test) == 'int':
        auc = roc_auc_score(y_test, y_pred)
        auc_train = roc_auc_score(y_train, y_pred_train)
        print(f'AUC: \t\t{100*auc:.2f}%\t\t{100*auc_train:.2f}%\t\t{100*(auc-auc_train):.2f}%')
        RocCurveDisplay.from_estimator(best_model, X_train, y_train)
        metrics['auc'] = auc
    
    print(f'Best model parameters from randomized search: {search_result.best_params_}')
    ConfusionMatrixDisplay.from_estimator(best_model, X_train, y_train)
    return metrics

def evaluate_classifier(classifier, X_test, y_test, X_train, y_train, pos_label=1,model_name='classifier', confusion_matrix=True):
    """
    Print evaluation metrics of the classifier. Classifier should be fit prior 
    to calling this function. Make sure to use `.best_estimator` if using grid/randomized search result.
        * recall
        * precision
        * F1
        * AUC score (only if class labels are integers)
    Plot:
        * confusion matrix
        * ROC (only if class labels are integers)
    Parameters:
    - pos_label (str or int): Class label for positive class. Default is 1.
    - model_name (string, optional): Name of model printing purposes.
    - confusion_matrix (bool): If True (default), print the confusion matrix. 

    Returns 2 dictionaries:
    - evaluation metrics for test data
    - evaluation metrics train data set
    """
    
    best_model = classifier

    y_pred = best_model.predict(X_test)

    y_pred_train = best_model.predict(X_train)

    # Metrics for test data
    metrics = dict()
    if len(set(y_test)) == 2:
        recall = recall_score(y_test, y_pred, pos_label=pos_label)
        precision = precision_score(y_test, y_pred, pos_label=pos_label)
        f1score = f1_score(y_test, y_pred, pos_label=pos_label)
        metrics['recall'] = recall
        metrics['precision'] = precision
        metrics['f1'] = f1score

    accuracy = accuracy_score(y_test, y_pred)
    metrics['accuracy'] = accuracy

    # Metrics for training data
    metrics_train = dict()
    if len(set(y_test)) == 2:
        recall_train = recall_score(y_train, y_pred_train, pos_label=pos_label)
        precision_train = precision_score(y_train, y_pred_train, pos_label=pos_label)
        f1score_train = f1_score(y_train, y_pred_train, pos_label=pos_label)
        metrics_train['recall'] = recall_train
        metrics_train['precision'] = precision_train
        metrics_train['f1'] = f1score_train
    accuracy_train = accuracy_score(y_train, y_pred_train)
    metrics_train['accuracy'] = accuracy_train

    print(f'\n{model_name} evaluation metrics: \n\tTest data\tTraining data\t\tDifference')
    print(f'Accuracy: \t{100*accuracy:.2f}%\t\t{100*accuracy_train:.2f}%\t\t{100*(accuracy-accuracy_train):.2f}%')
    if len(set(y_test)) == 2:
        print(f'Recall: \t{100*recall:.2f}%\t\t{100*recall_train:.2f}%\t\t{100*(recall-recall_train):.2f}%')
        print(f'Precision: \t{100*precision:.2f}%\t\t{100*precision_train:.2f}%\t\t{100*(precision-precision_train):.2f}%')
        print(f'F1: \t\t{100*f1score:.2f}%\t\t{100*f1score_train:.2f}%\t\t{100*(f1score-f1score_train):.2f}%')
        if type(y_test) == 'int':
            auc = roc_auc_score(y_test, y_pred)
            auc_train = roc_auc_score(y_train, y_pred_train)
            print(f'AUC: \t\t{100*auc:.2f}%\t\t{100*auc_train:.2f}%\t\t{100*(auc-auc_train):.2f}%')
            RocCurveDisplay.from_estimator(best_model, X_train, y_train)
            metrics['auc'] = auc
    if confusion_matrix==True:
        ConfusionMatrixDisplay.from_estimator(best_model, X_train, y_train)
    return metrics, metrics_train

from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
def evaluate_classifier2(classifier, X_test, y_test, y_train, y_pred_train, pos_label=1,model_name='classifier', confusion=True,roc=True):
    """
    Print evaluation metrics of the classifier. Classifier should be fit prior to calling this function.
        * recall
        * precision
        * F1
        * AUC score (only if class labels are integers)
    Plot:
        * confusion matrix
        * ROC (only if class labels are integers)
    Parameters:
    - y_pred_train: Prediction for training set.
    - pos_label (str or int): Class label for positive class. Default is 1.
    - model_name (string, optional): Name of model printing purposes.
    - confusion_matrix (bool): If True (default), print the confusion matrix. 
    - roc (bool): If true, provide roc-auc score and plot.
    - confusion (bool): If true, plot ROC-AUC curve.

    Returns:
    - evaluation metrics for test data (dictionary)
    - evaluation metrics train data set (dictionary)
    - predictions for test set
    - confusion matrix values (array)
    """
    
    best_model = classifier
    print(best_model.best_estimator_)

    y_pred = best_model.predict(X_test)

    # y_pred_train = best_model.predict(X_train)

    # Metrics for test data
    metrics = dict()
    if len(set(y_test)) == 2:
        recall = recall_score(y_test, y_pred, pos_label=pos_label)
        precision = precision_score(y_test, y_pred, pos_label=pos_label)
        f1score = f1_score(y_test, y_pred, pos_label=pos_label)
        metrics['recall'] = recall
        metrics['precision'] = precision
        metrics['f1'] = f1score

    accuracy = accuracy_score(y_test, y_pred)
    metrics['accuracy'] = accuracy

    # Metrics for training data
    metrics_train = dict()
    if len(set(y_test)) == 2:
        recall_train = recall_score(y_train, y_pred_train, pos_label=pos_label)
        precision_train = precision_score(y_train, y_pred_train, pos_label=pos_label)
        f1score_train = f1_score(y_train, y_pred_train, pos_label=pos_label)
        metrics_train['recall'] = recall_train
        metrics_train['precision'] = precision_train
        metrics_train['f1'] = f1score_train
    accuracy_train = accuracy_score(y_train, y_pred_train)
    metrics_train['accuracy'] = accuracy_train

    print(f'\n{model_name} evaluation metrics: \n\tTest data\tTraining data\t\tDifference')
    print(f'Accuracy: \t{100*accuracy:.2f}%\t\t{100*accuracy_train:.2f}%\t\t{100*(accuracy-accuracy_train):.2f}%')
    if len(set(y_test)) == 2:
        print(f'Recall: \t{100*recall:.2f}%\t\t{100*recall_train:.2f}%\t\t{100*(recall-recall_train):.2f}%')
        print(f'Precision: \t{100*precision:.2f}%\t\t{100*precision_train:.2f}%\t\t{100*(precision-precision_train):.2f}%')
        print(f'F1: \t\t{100*f1score:.2f}%\t\t{100*f1score_train:.2f}%\t\t{100*(f1score-f1score_train):.2f}%')
        if roc==True:
            auc = roc_auc_score(y_test, y_pred)
            auc_train = roc_auc_score(y_train, y_pred_train)
            RocCurveDisplay.from_predictions(y_test, y_pred)
            metrics['auc'] = auc
            print(f'AUC: \t\t{100*auc:.2f}%\t\t{100*auc_train:.2f}%\t\t{100*(auc-auc_train):.2f}%')
    if confusion==True:
        ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)

    return metrics, metrics_train, y_pred, matrix

def plot_training_metrics(history):
    """
    Plot the history of the evaluation metrics from a Keras neural network model:
    - Loss
    - Accuracy

    Parameters: Output from keras model `.fit()`
    """
    fig, ax = plt.subplots(1, 2)
    sns.lineplot(history.history['loss'], ax=ax[0], label='train')
    sns.lineplot(history.history['val_loss'], ax=ax[0], label='test')
    ax[0].set_title('Loss')

    sns.lineplot(history.history['accuracy'], ax=ax[1], label='train')
    sns.lineplot(history.history['val_accuracy'], ax=ax[1], label='test')
    ax[1].set_title('Accuracy')
    plt.tight_layout()


def evaluate_regression(y_test, y_pred, y_train, y_pred_train, model_name='regressor',plot=True):
    """
    * Print model evalutation metrics: 
        * RMSE
        * Mean absolute error (MAE)
        * R^2 score
        * Pearson correlation coefficient
    * If plot=True : Provide scatterplot of true vs. predicted values.
    Params:
    - plot (bool): If true, plot true vs. predicted values using test data set from train-test split.

    Returns: 
    - Evaluation metrics for train and test data subsets:
        - `.r2_train` and `.r2`
        - `.rmse_train` and `.rmse`
        - `.mean_abs_error_train` and `.mean_abs_error`
    """
    # Metrics for test data

    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mean_abs_error = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Metrics for training data

    rmse_train = mean_squared_error(y_train, y_pred_train)
    mean_abs_error_train = mean_absolute_error(y_train, y_pred_train)
    r2_train = r2_score(y_train, y_pred_train)
    
    # Calculate Pearson Correlation between predicted and true values:
    pearson = stats.pearsonr(y_test, y_pred)

    print(f'\n{model_name} evaluation metrics: \n\tTest data\tTraining data\t\tDifference')
    print(f'RMSE: \t\t{rmse:.2f}\t\t{rmse_train:.2f}\t\t{(rmse - rmse_train):.2f}')
    print(f'MAE: \t\t{mean_abs_error:.2f}\t\t{mean_abs_error_train:.2f}\t\t{(mean_abs_error - mean_abs_error_train):.2f}')
    print(f'R^2: \t\t{r2:.2f}\t\t{r2_train:.2f}\t\t{(r2 - r2_train):.2f}')
    print(f'\nPearson correlation coefficient (r) for predicted and true values: {pearson.statistic:.2f} (p-value of {pearson.pvalue:.2f}).')

    if plot:
        fig = sns.scatterplot(x=y_test, y=y_pred)
        fig.set_xlabel('Predicted')