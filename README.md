

 Movie Genre Prediction using NLP

A machine learning web application that predicts the **genre of a movie** based on its plot description.  
Built using **Python**, **Flask**, **scikit-learn**, and **NLP techniques**, this project demonstrates how text classification can be applied to real-world problems like movie genre detection.

---

 Project Overview

This project takes a movie's plot summary as input and predicts the most likely genre (e.g., Action, Comedy, Drama).  
It uses TF-IDF vectorization to convert text into feature vectors and a classification model (Multinomial Naive Bayes / Logistic Regression) for prediction.

---

 Features

- Genre classification from movie plot text
- TF-IDF-based feature extraction
- Trained machine learning model
- User-friendly web interface using Flask

---

 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- HTML / CSS (Frontend)
- NLP: TF-IDF Vectorizer

---

 Project Structure

```
movie-genre-prediction/
├── app.py # Flask backend
├── genre_model.pkl # Trained model
├── tfidf_vectorizer.pkl # TF-IDF vectorizer
├── templates/
│ └── index.html # Single page interface
├── requirements.txt # Required packages
└── README.md # Project documentation

````

---

1.   How to Run

1. Clone the Repository
   ```bash
   git clone https://github.com/SREELEKHA419/movie-genre-prediction.git
   cd movie-genre-prediction
````

2. Install Requirements

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask App

   ```bash
   python app.py
   ```

4. Visit in Browser

   ```
   http://127.0.0.1:5000/
   ```

---

 Example

Input:
"A retired CIA agent travels across Europe to rescue his kidnapped daughter."

Output:
Predicted Genre: Action / Thriller

---
License

This project is licensed under the **MIT License**.
Feel free to use and modify with attribution.

---
 Developed By

Sreelekha A S
B.Tech Computer Science and Engineering
B. S. Abdur Rahman Crescent Institute of Science and Technology, Chennai
