#!flask/bin/python
import os
from flask import Flask
from flask import request
from flask import jsonify
from keras.models import load_model
from keras.preprocessing import sequence, text
import numpy as np

model = load_model('./my_model.h5')

app = Flask(__name__)

@app.route('/isAlive', methods=['GET'])
def index():
    return jsonify(return_value = "channa works on ML classification algorithm")

@app.route('/get_prediction', methods=['POST'])
def _get_prediction():

    filters = request.get_json()
    print("filters: ", filters)
    sentences_list = filters.get('sentences', dict())

    input_text = np.array(sentences_list)
    tk = text.Tokenizer(nb_words=2000, lower=True,split=" ")
    tk.fit_on_texts(input_text)
    predicted_values = model.predict(sequence.pad_sequences(tk.texts_to_sequences(input_text),maxlen=500))
    
    return_res = []
    for a_sentence, pred_val in zip(sentences_list, predicted_values.tolist()):
        return_res.append((a_sentence, pred_val))

    return jsonify(ret_pred_values = return_res)

if __name__ == '__main__':
    pass