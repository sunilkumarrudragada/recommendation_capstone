## Deployment

The recommendation system was deployed as a Flask web application using Docker on Render.

- **Backend:** Flask  
- **Model:** Collaborative Filtering  
- **Environment:** Docker (Python 3.12)  
- **Hosting Platform:** Render  

🔗 **Live URL:**  
https://recommendation-capstone-1.onrender.com/

The application loads pre-trained model artifacts and serves real-time product recommendations based on the username provided.

---

## Requirements

The following software and libraries are required to run the application locally:

- Python **3.12.x**
- Flask
- NumPy
- Pandas
- Scikit-learn
- Gunicorn
- Docker (optional, for containerized execution)

All required Python dependencies are listed in the `requirements.txt` file.

---

## Project Structure

```text
recommendation_capstone/
├── app.py
├── model.py
├── tfidf_vectorizer.pkl
├── sentiment_model.pkl
├── reviews_df.pkl
├── user_item_pivot.pkl
├── item_similarity.pkl
├── templates/
│   └── index.html
├── Dockerfile
├── requirements.txt
└── recommendation_capstone.ipynb

