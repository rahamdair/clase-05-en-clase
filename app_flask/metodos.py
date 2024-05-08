
import pickle

def load_models():
    '''
    Replace '..path/' by the path of the saved models.
    '''
    
    # Load the vectoriser.
    file = open('data_generada_demo/vectoriser-ngram-1-2.pickle', 'rb')
    vectoriser = pickle.load(file)
    file.close()
    # Load the LR Model.
    file = open('data_generada_demo/Sentiment-LR.pickle', 'rb')
    LRmodel = pickle.load(file)
    file.close()
    
    return vectoriser, LRmodel

def predict(vectoriser, model, text):
    # Predict the sentiment
    # textdata = vectoriser.transform(preprocess(text))
    textdata = vectoriser.transform([text])
    sentiment = model.predict(textdata)
    sentiment = tipo_prediccion(sentiment)
    
    # print("%s - %s " % (sentiment, text))
    return sentiment

def tipo_prediccion(sentimiento):
    """
        0 - negativo
        1 - positivo
    """
    
    valor = int(list(sentimiento)[0])
    # print(valor)
    tipo = (-1, None)
    if valor == 0:
        tipo = (0, "negativo")
    else:
        if valor == 1:
            tipo = (1, "positivo")
    print(tipo)
    return tipo
        

