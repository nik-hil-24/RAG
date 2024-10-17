import json
import pandas as pd

f = open('corpus.json')
corpus = json.load(f)
f.close()

f = open('train.json')
train = json.load(f)
f.close()

corpus_df = pd.DataFrame(corpus)
train_df = pd.DataFrame(train)
train_df['evidence_length'] = train_df['evidence_list'].apply(lambda x: len(x))

print(train_df.question_type.unique())
print(train_df.evidence_length.unique())
