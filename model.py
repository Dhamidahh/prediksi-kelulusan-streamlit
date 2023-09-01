#Masukkan Library
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
import joblib

data = pd.read_csv("DATA.csv")

X = data.drop(['Agama', 'Ketahanan_Pangan', 'Pancasila', 'Pendidikan_Kewarganegaraan',
              'Studi_Kebantenan', 'Tata_Tulis_dan_Komunikasi_Ilmiah', 'Kuliah_Kerja_Mahasiswa',
              'Seminar_Pendidikan_Agama', 'Status_Kelulusan'], axis=1)
y = data['Status_Kelulusan']

# Bagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Number of trees in random forest
n_estimators = [int(X) for X in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['log2', 'sqrt', None]
# Maximum number of levels in tree
max_depth = [int(X) for X in np.linspace(10, 110, num = 11)]
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

# Inisialisasi model Random Forest
rf = RandomForestClassifier(random_state = 42)
model = RandomizedSearchCV(estimator=rf, param_distributions=random_grid,
                              n_iter = 100, scoring='neg_mean_absolute_error',
                              cv = 3, verbose=2, random_state=42, n_jobs=-1,
                              return_train_score=True)

# Latih model
model.fit(X_train, y_train)

# Prediksi pada data uji
y_pred = model.predict(X_test)

# Simpan model
joblib.dump(model, 'random_forest_model.pkl')

# Simpan data yang digunakan untuk training (X_train)
joblib.dump(X_train, 'X_train.pkl')

# Simpan label yang digunakan untuk training (y_train)
joblib.dump(y_train, 'y_train.pkl')