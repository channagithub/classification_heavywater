import pandas as pd
from joblib import dump
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("./data/shuffled-full-set-hashed.csv",
            names = ['class', 'doc'])
df.dropna(inplace = True)
print("Read data done")

tfidf = TfidfVectorizer(sublinear_tf=True, 
                        min_df=5, norm='l2', 
                        encoding='latin-1', ngram_range=(1, 2), 
                        max_features = 2000)

tfidf.fit(df.doc)

print("TFIDF step done")

dump(tfidf, 'pkl_files/tfidf.pkl')
