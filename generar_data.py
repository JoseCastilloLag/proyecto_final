import pandas as pd
import numpy as np

np.random.seed(42)

n = 120

df = pd.DataFrame({
    "genero": np.random.choice(["M","F"], n),
    "horas_estudio": np.random.normal(12,4,n),
    "ausencias": np.random.normal(3,2,n),
    "nota_parcial": np.random.normal(3.5,0.8,n)
})

df["nota_final"] = (
    0.4*df["nota_parcial"] +
    0.2*df["horas_estudio"] -
    0.1*df["ausencias"] +
    np.random.normal(0,0.5,n)
)

df.to_csv("data/data.csv", index=False)

print("Datos generados correctamente")