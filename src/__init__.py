import pandas as pd

data = {
    "Name": ["alice", "bob", "Charlie", "David"],
    "Age": [24, 27, 22, 23],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(data)


df.head(2)
df.tail(2)
df.info()

df = df.replace("alice", "Alice Smith")
