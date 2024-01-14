import time
import pandas as pd
import psycopg2
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import OneClassSVM
from sklearn.impute import KNNImputer
import numpy as np
from prettytable import PrettyTable




# establishing the connection. before running the file, open psql shell and configure the below parameters.
conn = psycopg2.connect(
    database="postgres", user='postgres', password='7410', host='127.0.0.1', port='5432'
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

sql = '''
WITH dem
     AS (SELECT sex,
                age,
                seqno
         FROM   demographics),
     tob
     AS (SELECT regsmok,
                seqno
         FROM   tobacco),
     bp
     AS (SELECT hyper,
                syscat,
                seqno
         FROM   blood_pressure),
     diab
     AS (SELECT diabet,
                seqno
         FROM   diabetes),
     phys
     AS (SELECT seqno,
                bmicat,
                whrcat
         FROM   physical_measurements),
     facts
     AS (SELECT ascvd_score,
                framingham_score,
                seqno
         FROM   cardiac_fact
         WHERE  ascvd_score != 999
                AND framingham_score != 999)
SELECT *
FROM   dem
       INNER JOIN tob using(seqno)
       INNER JOIN bp using(seqno)
       INNER JOIN diab using(seqno)
       INNER JOIN phys using(seqno)
       INNER JOIN facts using(seqno) 
    '''

cursor.execute(sql)

data_dictionary = {'sex': [], 'age': [], 'regsmok': [], 'hyper': [], 'syscat': [], 'diabet': [],
                   'bmicat': [], 'whrcat': [], 'ascvd_score_category': [], 'framingham_score_category': [],
                   'ascvd_svm': []}

for row in cursor.fetchall():
    data_dictionary['sex'].append(row[1])
    data_dictionary['age'].append(row[2])

    if row[3]==9:
        data_dictionary['regsmok'].append(None)
    else:
        data_dictionary['regsmok'].append(row[3])

    data_dictionary['hyper'].append(row[4])

    if row[5]==9:
        data_dictionary['syscat'].append(None)
    else:
        data_dictionary['syscat'].append(row[5])

    if row[6]==7 or row[6]==9:
        data_dictionary['diabet'].append(None)
    else:
        data_dictionary['diabet'].append(row[6])

    if row[7] == 7 or row[7] == 9:
        data_dictionary['bmicat'].append(None)
    else:
        data_dictionary['bmicat'].append(row[7])

    if row[8] == 7 or row[8] == 9:
        data_dictionary['whrcat'].append(None)
    else:
        data_dictionary['whrcat'].append(row[8])

    if row[9] < 5:
        data_dictionary['ascvd_score_category'].append('low')
    elif row[9] >= 5 and row[9] < 7.5:
        data_dictionary['ascvd_score_category'].append('borderline')
    elif row[9] >= 7.5 and row[9] < 20:
        data_dictionary['ascvd_score_category'].append('intermediate')
    elif row[9] >= 20:
        data_dictionary['ascvd_score_category'].append('high')
    if row[9] <= 20:
        data_dictionary['ascvd_svm'].append(0)
    elif row[9] > 20:
        data_dictionary['ascvd_svm'].append(1)
    if row[10] < 10:
        data_dictionary['framingham_score_category'].append('low')
    elif row[10] >= 10 and row[10] < 20:
        data_dictionary['framingham_score_category'].append('intermediate')
    elif row[10] >= 20:
        data_dictionary['framingham_score_category'].append('high')

data_frame = pd.DataFrame.from_dict(data_dictionary)
tb = PrettyTable()
tb.field_names = ["Algorithm", "Accuracy", "Precision", "Recall", "Training Time"]


def normalize_data_frame():
    scaler=MinMaxScaler()
    column_names_to_normalize = ['sex', 'age', 'regsmok', 'hyper', 'syscat', 'diabet', 'bmicat', 'whrcat']
    x = data_frame[column_names_to_normalize].values
    x_scaled = scaler.fit_transform(x)
    df_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index=data_frame.index)
    data_frame[column_names_to_normalize] = df_temp


def impute_data_frame():
    imputer = KNNImputer(n_neighbors=10,weights='uniform')
    column_names_to_impute = ['sex', 'age', 'regsmok', 'hyper', 'syscat', 'diabet', 'bmicat', 'whrcat']
    df_temp= data_frame[column_names_to_impute]
    df_temp = pd.DataFrame(imputer.fit_transform(df_temp), columns=df_temp.columns)
    data_frame[column_names_to_impute] = df_temp


def random_forest(target, data_frame):
    X, y = data_frame.drop(['ascvd_score_category', 'framingham_score_category','ascvd_svm'], axis=1), data_frame[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    rf = RandomForestClassifier()
    # start the timer
    st = time.process_time()
    # Train the model on training data
    rf.fit(X_train, y_train)
    # end the timer
    et = time.process_time()
    # Use the forest's predict method on the test data
    y_pred = rf.predict(X_test)
    tb.add_row(["Random Forest",
                round(metrics.accuracy_score(y_test, y_pred), 3),
                round(metrics.precision_score(y_test, y_pred, average='macro'), 3),
                round(metrics.recall_score(y_test, y_pred, average='macro'), 3),
                round(et - st, 3)])


def gradient_boosting(target, data_frame):
    X, y = data_frame.drop(['ascvd_score_category', 'framingham_score_category','ascvd_svm'], axis=1), data_frame[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    gb_params = {'n_estimators': 20,
                 'max_features': 3,
                 'max_depth': 5,
                 'learning_rate': 0.5,
                 'random_state': 0}
    # Create an instance of gradient boosting regressor
    gb = GradientBoostingClassifier(**gb_params)
    # start the timer
    st = time.process_time()
    # Train the model on training data
    gb.fit(X_train, y_train)
    # end the timer
    et = time.process_time()
    # Use the predict method on the test data
    y_pred = gb.predict(X_test)
    tb.add_row(["Gradient Boosting",
                round(metrics.accuracy_score(y_test, y_pred), 3),
                round(metrics.precision_score(y_test, y_pred, average='macro'), 3),
                round(metrics.recall_score(y_test, y_pred, average='macro'), 3),
                round(et - st, 3)])


def decision_tree(target, data_frame):
    X, y = data_frame.drop(['ascvd_score_category', 'framingham_score_category','ascvd_svm'], axis=1), data_frame[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    tr = DecisionTreeClassifier(random_state=0)
    # start the timer
    st = time.process_time()
    # Train the model on training data
    tr.fit(X_train, y_train)
    # Use the predict method on the test data
    # end the timer
    et = time.process_time()
    y_pred = tr.predict(X_test)
    tb.add_row(["Decision Tree",
                round(metrics.accuracy_score(y_test, y_pred), 3),
                round(metrics.precision_score(y_test, y_pred, average='macro'), 3),
                round(metrics.recall_score(y_test, y_pred, average='macro'), 3),
                round(et - st, 3)])




def detect_outliers(target, data_frame):
    X, y = data_frame.drop(['ascvd_score_category', 'framingham_score_category', 'ascvd_svm',
                            'diabet', 'sex', 'bmicat', 'hyper'], axis=1), data_frame[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    model = OneClassSVM(nu=0.01, kernel='rbf', gamma='auto')
    model.fit(X_train)
    prediction = model.predict(X_test)
    outlier_index = np.where(prediction == -1)
    outlier_values = data_frame.iloc[outlier_index]
    print('The number of outliers in the data frame is', len(outlier_values.index))
    print('The number of outlier patients categorized as low risk who are diabetic or hypertensive',
          len(outlier_values[(outlier_values["ascvd_svm"] == 0) &((outlier_values["diabet"] == 1)|(outlier_values["hyper"] == 1))]))

    print('The number of outlier patients categorized as high risk who are not diabetic or hypertensive',
          len(outlier_values[(outlier_values["ascvd_svm"] == 1) &((outlier_values["diabet"] == 0)|(outlier_values["hyper"] == 0))]))

    print(outlier_values.to_string())


normalize_data_frame()
impute_data_frame()

print("The Shape of the Data Frame is", data_frame.shape)
print("The Data Frame Contains Null/Missing Values:",data_frame.isnull().values.any())

print()
print("Classification Results for ASCVD Score")
random_forest('ascvd_score_category', data_frame)
gradient_boosting('ascvd_score_category', data_frame)
decision_tree('ascvd_score_category', data_frame)
print(tb)
tb.clear_rows()
print()

print("Classification Results for Framingham Score")
random_forest('framingham_score_category', data_frame)
gradient_boosting('framingham_score_category', data_frame)
decision_tree('framingham_score_category', data_frame)
print(tb)
print()

detect_outliers('ascvd_svm', data_frame)

cursor.close()
