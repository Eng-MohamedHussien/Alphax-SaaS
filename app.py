from flask import Flask, render_template, request
from SentimentAnalyzer.sentimentanalyse import *
from tensorflow.keras.preprocessing.text import tokenizer_from_json
app = Flask(__name__)
# to load tokenizer
with open('./SentimentAnalyzer/tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

nlp_model = define_model(16384, 64, 128)
# to load sentiment analysis model
nlp_model.load_weights('./SentimentAnalyzer/eng_sentimentAnalyzer.h5')


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')


@app.route('/sentiment_analysis')
def sentiment_analysis():
	return render_template('try.html')


@app.route('/sentiment_analysis_try', methods=['POST', 'GET'])
def sentiment_analysis_try():
	if request.method == 'POST':
		review = request.form['review']
		confidence, tag = predict_sentiment(review, tokenizer, nlp_model)
		return render_template('try.html', tag=tag, confidence=str(round(confidence, 2))+'%')


if __name__ == '__main__':
	app.run(host='0.0.0.0')

