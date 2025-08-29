import sqlite3
import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

# Rename columns for SQL style
df.rename(columns={
    "sepal length (cm)": "sepal_length",
    "sepal width (cm)": "sepal_width",
    "petal length (cm)": "petal_length",
    "petal width (cm)": "petal_width"
}, inplace=True)

# Connect to SQLite (in-memory)
conn = sqlite3.connect(":memory:")
df.to_sql("iris", conn, index=False, if_exists="replace")

# --- Example Queries ---
queries = {
    "All data": "SELECT * FROM iris LIMIT 5;",
    "Count by species": "SELECT species, COUNT(*) as count FROM iris GROUP BY species;",
    "Average petal length by species": "SELECT species, AVG(petal_length) as avg_petal_length FROM iris GROUP BY species;",
    "Max sepal length": "SELECT MAX(sepal_length) as max_sepal_length FROM iris;",
    "Flowers with petal_length > 5.0": "SELECT * FROM iris WHERE petal_length > 5.0 LIMIT 5;"
}

for title, q in queries.items():
    print(f"\n--- {title} ---")
    print(pd.read_sql(q, conn))
NEXT
import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
df.rename(columns={
    "sepal length (cm)": "sepal_length",
    "sepal width (cm)": "sepal_width",
    "petal length (cm)": "petal_length",
    "petal width (cm)": "petal_width"
}, inplace=True)

# Example "Python queries"
print("\n--- Count by species ---")
print(df.groupby("species").size())

print("\n--- Average petal length by species ---")
print(df.groupby("species")["petal_length"].mean())

print("\n--- Max sepal length ---")
print(df["sepal_length"].max())

print("\n--- Flowers with petal_length > 5.0 ---")
print(df[df["petal_length"] > 5.0].head())
