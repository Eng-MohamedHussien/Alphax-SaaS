import json
import re
import string
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten, Conv1D, MaxPooling1D


def clean_doc(doc):
    tokens = doc.split()
    punctuation_filter = re.compile('[%s]' % re.escape(string.punctuation))
    tokens = [punctuation_filter.sub('', w) for w in tokens]
    tokens = [w for w in tokens if w.isalpha()]
    tokens = [w for w in tokens if w not in stopwords.words('english')]
    tokens = [w for w in tokens if len(w) > 1]
    return tokens


def define_model(max_features, embed_size, max_length):
    model = Sequential()
    model.add(Embedding(max_features, embed_size, input_length=max_length))
    model.add(Conv1D(filters=32, kernel_size=8, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def predict_sentiment(review, nlp_tokenizer, model):
    tokens = clean_doc(review)
    line = ' '.join(tokens)
    encoded = nlp_tokenizer.texts_to_sequences([line])
    x = pad_sequences(encoded, maxlen=128, padding='post')
    y = model.predict(x, verbose=0)
    percent_pos = y.tolist()[0][0]
    if round(percent_pos) == 0:
        return (1-percent_pos)*100, 'NEGATIVE'
    return percent_pos*100, 'POSITIVE'







