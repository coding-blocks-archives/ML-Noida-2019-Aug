import pickle

with open("vectorizer.pkl", "rb") as vectorizer_fl:
    vectorizer = pickle.load(vectorizer_fl)
with open("model.pkl", "rb") as model_fl:
    model = pickle.load(model_fl)

def predict(sent):    
    vect = vectorizer.transform([sent])
    return model.predict(vect)[0]