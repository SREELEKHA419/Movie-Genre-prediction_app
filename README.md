
  Movie Genre Prediction using NLP

This web-based application predicts the genre of a movie based on its description using Natural Language Processing (NLP) and Machine Learning techniques.

---

 Project Structure

```

movie-genre-prediction/
├── app.py                # Flask app to take user input and predict movie genre
├── movie\_data.xlsx       # Dataset with movie plots and corresponding genres
├── sample.xlsx           # Sample input data for testing
├── templates/            # HTML templates for frontend
│   ├── index.html        # Input form for movie description
│   └── result.html       # Output result page
├── OUTPUTS/              # Optional: stores logs or prediction screenshots
├── requirements.txt      # Required Python libraries (if created)
└── README.md             # Documentation

````

---

 How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/movie-genre-prediction.git
   cd movie-genre-prediction
````

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *(If requirements.txt is missing, install manually: Flask, scikit-learn, pandas, etc.)*

3. **Start the Flask App**

   ```bash
   python app.py
   ```

4. **Open in Browser**

   ```
   http://localhost:5000
   ```

---

## 🧠 ML Model Details

* **Features Used**: Movie description (text)
* **Technique**: TF-IDF Vectorizer + Multinomial Naive Bayes (or Logistic Regression)
* **Output**: Predicted genre (e.g., Action, Comedy, Drama, etc.)

---

Dataset

* `movie_data.xlsx`: Contains movie descriptions and genres.
* `sample.xlsx`: Sample entries for user testing.

---

 Features

* Clean and simple web UI (built with Flask and Jinja2)
* Predicts genre using ML model trained on real data
* Interactive result display

---

 License

This project is licensed under the [MIT License](LICENSE).

---

 Author

Sreelekha A S
B.Tech CSE | B.S. Abdur Rahman Crescent Institute of Science and Technology
[GitHub](https://github.com/SREELEKHA419)


