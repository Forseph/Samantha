from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pandas as pd

def analyze(train, test):

    train = pd.read_csv(train)
    train = train.loc[:, ~train.columns.str.contains('^Unnamed')]
    test = pd.read_csv(test)
    test = test.loc[:, ~test.columns.str.contains('^Unnamed')]

    train['Label_num'] = train.Sentiment.map({'Positive':1, 'Negative':0})
    test['Label_num'] = test.Sentiment.map({'Positive':1, 'Negative':0})

    X_train = train.Review
    y_train = train.Label_num
    X_test = test.Review
    y_test = test.Label_num
    vector = CountVectorizer()
    X_train_dtm = vector.fit_transform(X_train.values.astype('U'))
    X_test_dtm = vector.transform(X_test.values.astype('U'))

    nb = MultinomialNB()
    nb.fit(X_train_dtm, y_train)
    y_pred_class = nb.predict(X_test_dtm)

    print metrics.accuracy_score(y_test, y_pred_class) 
    conf_matrix = metrics.confusion_matrix(y_test, y_pred_class)
    print conf_matrix
    false_pos = X_test[y_pred_class > y_test]
    #print "\nFalse Positives"
    #print false_pos
    false_neg = X_test[y_pred_class < y_test]
    #print "\nFalse Negatives"
    #print false_neg

analyze("train1.csv", "test1.csv")
analyze("train2.csv", "test2.csv")
analyze("train3.csv", "test3.csv")
analyze("train4.csv", "test4.csv")
analyze("train5.csv", "test5.csv")
