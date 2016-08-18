# # Import statements 
# # Libraries
import numpy as np
import pandas as pd
import sklearn
import scipy.stats as stats
from sklearn.calibration import CalibratedClassifierCV
import matplotlib.pyplot as plt
from time import time

# # Libraries for metric functions
# from sklearn.metrics import (f1_score, accuracy_score, make_scorer, fbeta_score, 
#                              brier_score_loss, precision_score, recall_score)
# from sklearn.metrics import classification_report, confusion_matrix

# # Libraries used for classification models
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC, LinearSVC
# from sklearn import neighbors
# from sklearn import tree
# from sklearn.naive_bayes import GaussianNB

# # Other utilities
# from sklearn import cross_validation
# from sklearn.cross_validation import train_test_split
# from sklearn.grid_search import GridSearchCV
# from sklearn.feature_selection import RFE
# from sklearn.calibration import CalibratedClassifierCV, calibration_curve

# # Libraries for metric functions
from sklearn.metrics import (f1_score, accuracy_score, make_scorer, fbeta_score, 
                             brier_score_loss, precision_score, recall_score)
from sklearn.metrics import classification_report, confusion_matrix

# # Libraries used for classification models
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC, LinearSVC
# from sklearn import neighbors
# from sklearn import tree
# from sklearn.naive_bayes import GaussianNB

# # Other utilities
# from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
# from sklearn.feature_selection import RFE
# from sklearn.calibration import CalibratedClassifierCV, calibration_curve


# =================================================
# PART 1: EXPLORING THE DATA
# Investigating the dataset to determine how many students we have,
# graduation rate, etc.
# @n_students : the total number of students
# @n_features : the number of students who passed
# @n_failed : the number of students who failed
# @grad_rate : graduation rate in percent
# =================================================

# # Read student data
# student_data = pd.read_csv("student-data.csv")
# print "Student data read successfully!"

# # create another dataframe for playing around with!
# df = pd.read_csv("student-data.csv")

# # Identify data and create variables
# # Calculate number of students
# n_students = student_data.shape[0]

# # Calculate number of features
# n_features = student_data.shape[1]

# # Calculate passing students
# n_passed = len(student_data[student_data.passed == "yes"])

# # Calculate failing students
# n_failed = len(student_data[student_data.passed == "no"])

# # Calculate graduation rate
# grad_rate = float(n_passed) / n_students * 100

# =================================================
# PART 2: PREPARING THE DATA
# Identify feature and target columns and
# seperate data into feature and target columns
# =================================================

# # Extract feature columns
# feature_cols = list(student_data.columns[:-1])

# # Extract target column 'passed'
# target_col = student_data.columns[-1]

# # Separate the data into feature data and target data
# X_all = student_data[feature_cols]
# y_all = student_data[target_col]

# # Create an instance of target labels in binary format
# y_all_num = y_all.replace(['yes', 'no'], [1, 0])


# Preprocess feature columns
def preprocess_features(X):
    ''' Preprocesses the student data and converts
    non-numeric binary variables into binary (0/1) variables.
    Converts categorical variables into dummy variables. '''

    # Initialize new output DataFrame
    output = pd.DataFrame(index=X.index)

    # Investigate each feature column for the data
    for col, col_data in X.iteritems():

        # If data type is non-numeric, replace all yes/no values with 1/0
        if col_data.dtype == object:
            col_data = col_data.replace(['yes', 'no'], [1, 0])

        # If data type is categorical, convert to dummy variables
        if col_data.dtype == object:
            # Example: 'school' => 'school_GP' and 'school_MS'
            col_data = pd.get_dummies(col_data, prefix=col)

        # Collect the revised columns
        output = output.join(col_data)

    return output

# X_all = preprocess_features(X_all)


# Set the number of training points
# I decided to be more specific with my training points,
# calculating 75% of testing points and
# cast it to int so that the result is a whole number
# num_train = int(n_students * 0.75)

# Set the number of testing points
# num_test = X_all.shape[0] - num_train

# Shuffle and split the dataset into the number of
# training and testing points above
# X_train, X_test, y_train, y_test = cross_validation.train_test_split(
#     X_all,
#     y_all,
#     test_size=num_test,
#     train_size=num_train,
#     random_state=0)

# # find a feature normalization:
# X_norm = np.mean(X_train, axis=0)

# =================================================
# Part 3: Training and Evaluating Models
# =================================================

# @train_classifier -
# takes as input a classifier and training data,
# fits the classifier to the data.

# @predict_labels -
# takes as input a fit classifier, features, and a target
# labeling and makes predictions using the F1 score.

# @train_predict -
# takes as input a classifier, and the training and testing data,
# and performs train_clasifier and predict_labels.
# This function will report the F1 score for both the
# training and testing data separately.


def train_classifier(clf, X_train, y_train):
    ''' Fits a classifier to the training data. '''

    # Start the clock, train the classifier, then stop the clock
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    train_time = end - start

    # Print the results
    print "Trained model in \t\t\t{:.4f}".format(train_time)


def train_classifier_noP(clf, X_train, y_train):
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    train_time = end - start
    return train_time


def predict_labels(clf, features, target):
    ''' Makes predictions using a fit classifier based on F1 score. '''

    # Start the clock, make predictions, then stop the clock
    start = time()
    y_pred = clf.predict(features)
    end = time()

    # Print and return results
    print "Made predictions in \t\t\t{:.4f}".format(end - start)
    return f1_score(target.values, y_pred, pos_label='yes')


def predict_labels_noP(clf, features, target):
    start = time
    y_pred = clf.predict(features)
    end = time()
    predict_time = end - start
    predict_f1_score = f1_score(target.values, y_pred, pos_label='yes')
    return predict_time, predict_f1_score


def train_predict(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score. '''

    # Indicate the classifier and the training set size
    print "Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train))

    # Train the classifier
    train_classifier_noP(clf, X_train, y_train)

    # Print the results of prediction for both training and testing
    print "F1 score for training set: \t\t{:.4f}".format(predict_labels(clf, X_train, y_train))
    print "F1 score for test set: \t\t\t{:.4f}".format(predict_labels(clf, X_test, y_test))


def train_predict_noP(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score. '''

    # Training time
    tc = train_classifier_noP(clf, X_train, y_train)

    # Training set
    pl_1 = predict_labels_noP(clf, X_train, y_train)

    # Test set
    pl_2 = predict_labels_noP(clf, X_test, y_test)

    return tc, pl_1[0], pl_1[1], pl_2[0], pl_2[1]


def train_predict_print(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score, 
    format and print the results. '''

    # Indicate the classifier and the training set size
    print "Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train))

    tc = train_classifier_noP(clf, X_train, y_train)
    print "Trained model in \t\t\t\t\t{:.4f}".format(tc)

    # Training set
    pl_1 = predict_labels_noP(clf, X_train, y_train)
    print "Made predictions on training set in: \t\t\t{:.4f}".format(pl_1[0])
    print "F1 score for training set: \t\t\t\t{:.4f}".format(pl_1[1])

    # Test set
    pl_2 = predict_labels_noP(clf, X_test, y_test)
    print "Made predictions on test set in: \t\t\t{:.4f}".format(pl_2[0])
    print "F1 score for test set: \t\t\t\t\t{:.4f}".format(pl_2[1])


# Functions for training and testing
# Functions perform same operations as the above functions but also identify variables for inbetween steps
# @ train_classifier_noP: stands for train classifier no print


def train_classifier_noP(clf, X_train, y_train):
    ''' Fits a classifier to the training data. '''
    
    # Start the clock, train the classifier, then stop the clock, return the time it takes
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    
    # Store and return results
    train_time = end - start # variable @train_time
    return train_time # return variable @train_time: the time it takes to fit/ train the model

def predict_labels_noP(clf, features, target):
    ''' Makes predictions using a fit classifier based on F1 score. '''
    # Start the clock, make predictions, then stop the clock, return the time it takes with f1 scores
    start = time()
    y_pred = clf.predict(features)
    end = time()
    
    # Store calculated variables
    # variable @predict_time
    predict_time = end - start 
    # variable @predict_f1_score
    predict_f1_score = f1_score(target.values, y_pred, pos_label='yes')
    
    # return variables @predict_time and @predict_f1_score
    return predict_time, predict_f1_score


def train_predict_noP(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score. '''
    
    # Training time
    tc = train_classifier_noP(clf, X_train, y_train)
    
    # Training set
    pl_1 = predict_labels_noP(clf, X_train, y_train)
    
    # Test set
    pl_2 = predict_labels_noP(clf, X_test, y_test)
    
    return tc, pl_1[0], pl_1[1], pl_2[0], pl_2[1]


def train_predict_print(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score, 
    format and print the results. '''
    
    # Indicate the classifier and the training set size
    print "Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train))
    
    tc = train_classifier_noP(clf, X_train, y_train)
    print "Trained model in \t\t\t\t\t{:.4f}".format(tc)
    
    # Training set
    pl_1 = predict_labels_noP(clf, X_train, y_train)
    print "Made predictions on training set in: \t\t\t{:.4f}".format(pl_1[0])
    print "F1 score for training set: \t\t\t\t{:.4f}".format(pl_1[1])
    
    # Test set
    pl_2 = predict_labels_noP(clf, X_test, y_test)
    print "Made predictions on test set in: \t\t\t{:.4f}".format(pl_2[0])
    print "F1 score for test set: \t\t\t\t\t{:.4f}".format(pl_2[1])


def clf_stats_all(clf, clf_info):
    '''Get and print calculated statistics for a model'''
    print "Statistics for {} model. . .".format(clf.__class__.__name__)
    print "Mean training time: {:,.4f}".format(np.mean(clf_info[0]))
    print "Mean prediction time: {:,.4f}".format(np.mean(clf_info[1]))
    print "Mean F1 score for training sets: {:,.4f}".format(np.mean(clf_info[2]))
    print "Mean testing time: {:,.4f}".format(np.mean(clf_info[3]))
    print "Mean F1 score for test sets: {:,.4f}".format(np.mean(clf_info[4]))


def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    '''Defines plot variables for confusion matrix'''
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    names = ["yes", "no"]
    tick_marks = np.arange(2)
    plt.xticks(tick_marks, names, rotation=45)
    plt.yticks(tick_marks, names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def clf_report(clf):
    '''Calculates classification report for a model'''
    print "\nClassification Report!"
    print classification_report(y_test, clf.predict(X_test))


def plot_mat(clf):
    '''Computes confusion matrix with and without normalization'''
    # Compute confusion matrix
    #fig = plt.figure()
    cm = confusion_matrix(y_test, clf.predict(X_test), labels=["yes","no"])
    np.set_printoptions(precision=2)
    print('Confusion matrix, without normalization')
    print(cm)
    plt.figure()
    plot_confusion_matrix(cm)

    # Normalize the confusion matrix by row (i.e by the number of samples
    # in each class)
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    print('Normalized confusion matrix')
    print(cm_normalized)
    plt.figure()
    plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix')

    plt.show()


def plot_calibration_curve(est, name, fig_index):
    """Plot calibration curve for est w/o and with calibration. """
    # Calibrated with isotonic calibration
    isotonic = CalibratedClassifierCV(est, cv=2, method='isotonic')

    # Calibrated with sigmoid calibration
    sigmoid = CalibratedClassifierCV(est, cv=2, method='sigmoid')

    # Logistic regression with no calibration as baseline
    lr = LogisticRegression(C=1., solver='lbfgs')

    fig = plt.figure(fig_index, figsize=(10, 10))
    ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)
    ax2 = plt.subplot2grid((3, 1), (2, 0))

    ax1.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
    for clf, name in [(lr, 'Logistic'),
                      (est, name),
                      (isotonic, name + ' + Isotonic'),
                      (sigmoid, name + ' + Sigmoid')]:
        clf.fit(X_train_cal, y_train_cal)
        y_pred = clf.predict(X_test_cal)
        if hasattr(clf, "predict_proba"):
            prob_pos = clf.predict_proba(X_test_cal)[:, 1]
        else:  # use decision function
            prob_pos = clf.decision_function(X_test_cal)
            prob_pos = \
                (prob_pos - prob_pos.min()) / (prob_pos.max() - prob_pos.min())

        clf_score = brier_score_loss(y_test_cal, 
                                     prob_pos, pos_label='yes')
        print("%s:" % name)
        print("\tBrier: %1.3f" % (clf_score))
        print("\tPrecision: %1.3f" % precision_score(y_test_cal, y_pred, pos_label='yes'))
        print("\tRecall: %1.3f" % recall_score(y_test_cal, y_pred, pos_label='yes'))
        print("\tF1: %1.3f\n" % f1_score(y_test_cal, y_pred, pos_label='yes'))

        fraction_of_positives, mean_predicted_value = \
            calibration_curve(y_test_cal, prob_pos, n_bins=10)

        ax1.plot(mean_predicted_value, fraction_of_positives, "s-",
                 label="%s (%1.3f)" % (name, clf_score))

        ax2.hist(prob_pos, range=(0, 1), bins=2, label=name,
                 histtype="step", lw=2)

    ax1.set_ylabel("Fraction of positives")
    ax1.set_ylim([-0.1, 1.2])
    ax1.set_xlim([0,1.2])
    ax1.legend(loc='best', fancybox=True, framealpha=0.5)
    ax1.set_title('Calibration plots  (reliability curve)')

    ax2.set_xlabel("Mean predicted value")
    ax2.set_ylabel("Count")
    ax2.set_xticks([2])
    ax2.legend(loc='best', fancybox=True, framealpha=0.5)

    plt.tight_layout()

def svc_param_select(X, y):
    start = time()
    Cs = [1, 10, 100]
    gammas = [0.01, 0, 1, 0.07]
    ks = ['sigmoid', 'linear', 'rbf']
    coefs = [-100000000, -100, 0, 1, 100]
    deg = [1,2,4]
    param_grid = {'kernel': ks, 'C': Cs, 'gamma': gammas}
    grid_search = GridSearchCV(SVC(), param_grid)
    grid_search.fit(X, y)
    grid_search.best_params_
    end = time()
    print "Best parameters: {}\n Best estimator: {}\n Best score: {}\n".format(grid_search.best_params_,
                                                                               grid_search.best_estimator_,
                                                                              grid_search.best_score_,)
    print "Finished in {} seconds.".format(end-start)