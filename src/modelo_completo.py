import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score
from scipy import stats

df = pd.read_csv("../data/data.csv")

# -----------------------
# BOOTSTRAP
# -----------------------
def bootstrap_ci(data):
    means = []
    for _ in range(1000):
        sample = np.random.choice(data, size=len(data), replace=True)
        means.append(np.mean(sample))
    return np.percentile(means, [2.5, 97.5])

print("Intervalo confianza:", bootstrap_ci(df["nota_final"]))

# -----------------------
# HIPÓTESIS
# -----------------------
hombres = df[df["genero"]=="M"]["nota_final"]
mujeres = df[df["genero"]=="F"]["nota_final"]

stat, p = stats.ttest_ind(hombres, mujeres)
print("p-valor:", p)

# -----------------------
# REGRESIÓN
# -----------------------
X = df[["horas_estudio","ausencias","nota_parcial"]]
y = df["nota_final"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

modelo = LinearRegression()
modelo.fit(X_train,y_train)

y_pred = modelo.predict(X_test)

print("R2:", r2_score(y_test,y_pred))

# -----------------------
# LOGÍSTICA
# -----------------------
df["aprobado"] = (df["nota_final"] >= 3).astype(int)

X = df[["horas_estudio","ausencias"]]
y = df["aprobado"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

log_model = LogisticRegression()
log_model.fit(X_train,y_train)

y_pred = log_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test,y_pred))