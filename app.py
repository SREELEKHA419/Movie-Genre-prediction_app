from flask import Flask, render_template, request
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

nltk.download('stopwords')

app = Flask(__name__)

# Load and preprocess dataset
df = pd.read_csv('movie_data.csv')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

df['CleanPlot'] = df['Plot'].apply(preprocess_text)

# Label encoding
le = LabelEncoder()
df['GenreEncoded'] = le.fit_transform(df['Genre'])

# TF-IDF vectorization
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['CleanPlot']).toarray()
y = df['GenreEncoded']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_genre = None
    uploaded_results = None

    if request.method == 'POST':
        # Text box submission
        if 'plot' in request.form:
            plot = request.form['plot']
            if plot.strip():
                clean = preprocess_text(plot)
                vector = tfidf.transform([clean]).toarray()
                prediction = model.predict(vector)
                predicted_genre = le.inverse_transform(prediction)[0]

        # File upload
        if 'file' in request.files:
            file = request.files['file']
            if file and file.filename.endswith(('.csv', '.txt')):
                try:
                    df_upload = pd.read_csv(file) if file.filename.endswith('.csv') else pd.DataFrame({'Plot': file.readlines()})
                    df_upload.columns = ['Plot'] if df_upload.shape[1] == 1 else df_upload.columns
                    df_upload['Clean'] = df_upload['Plot'].apply(preprocess_text)
                    vectors = tfidf.transform(df_upload['Clean']).toarray()
                    preds = model.predict(vectors)
                    df_upload['Predicted Genre'] = le.inverse_transform(preds)
                    uploaded_results = df_upload[['Plot', 'Predicted Genre']].to_dict(orient='records')
                except:
                    uploaded_results = 'error'

    return render_template('index.html', predicted_genre=predicted_genre, uploaded_results=uploaded_results)

if __name__ == '__main__':
    app.run(debug=True)
