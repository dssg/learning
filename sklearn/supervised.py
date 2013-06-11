#!/usr/bin/python

'''
An Example of Using SciKitLearn for Machine Learning (supervised)
'''

# import pylab as pl
from sklearn import datasets, svm, metrics, neighbors, tree


def main():

    #
    # GET DATA
    #

    digits = datasets.load_digits()

    n_samples = len(digits.images)

    # for performance, work with vector instead of 8x8 grid
    # -1 indicates "dont use this dimension"
    data = digits.images.reshape((n_samples, -1))

    # Training Data
    train_X = data[:n_samples // 2]
    train_Y = digits.target[:n_samples // 2]

    # // is integer division, won't result in a floating point
    # (Python 2) 1/2 == 0
    # (Python 3) 1/2 == 0.5

    # Test Data
    test_X = data[n_samples // 2:]
    test_Y = digits.target[n_samples // 2:]

    #
    # PREDICT
    #

    # Choose your classifer, fit data to it
    # classifier = tree.DecisionTreeClassifier()
    classifier = svm.SVC(gamma=0.001) # svm = support vector machine
    # classifier = neighbors.KNeighborsClassifier(3)

    classifier.fit(train_X, train_Y)

    # Predict values on test data... how well does it match?
    predicted_Y = classifier.predict(test_X)
    print "Acc score:", metrics.accuracy_score(test_Y, predicted_Y)  # Acc score: 0.749721913237

    #
    # TRAINING EXPLANATION
    #

    # View how your classifier has been trained
    print
    print classifier
    
    # all of the parameters here come from default config + what we specified.
    # also contains what we learned from the data, e.g. weights found during
    # linear regression

    #
    # PERFORMANCE
    #

    # View your performance
    # - how you're doing at predicting different classes
    print
    print metrics.classification_report(test_Y, predicted_Y)

    # - details of what mistakes you made
    print
    print metrics.confusion_matrix(test_Y, predicted_Y)

    # Recall - a classifier doesnt exactly give you a classification. It gives you a score.
    # You as a human are the one who sets the thresholds.


if __name__ == "__main__":
    main()
