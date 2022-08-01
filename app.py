from flask import Flask, request
from Services import *
import json

app = Flask(__name__)


@app.route("/nlp", methods=["GET", "POST"])
def do_nlp():
    result = None
    if request.method == 'POST':
        data = json.loads(request.data)
        result = {}
        if "char_freq" in data["requested_nlp"]:
            result.update({"char_freq": char_freq(data["text"])})
        if "part_of_speech" in data["requested_nlp"]:
            result.update({"char_freq": part_of_speech(data["text"])})
        if "word_definition" in data["requested_nlp"]:
            result.update({"char_freq": word_definition(data["text"])})
        if "word_frequency" in data["requested_nlp"]:
            result.update({"char_freq": word_frequency(data["text"])})
        if "Word_Sentiment" in data["requested_nlp"]:
            result.update({"char_freq": Word_Sentiment(data["text"])})
        if "word_translator" in data["requested_nlp"]:
            result.update({"char_freq": word_translator(data["text"], "en", "it")})

    return result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)