from flask import Flask, render_template, request
from model import get_top_5_recommendations
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    error = None

    if request.method == 'POST':
        username = request.form.get('username')

        if not username:
            error = "Please enter a username."
        else:
            recommendations = get_top_5_recommendations(username)

            if not recommendations:
                error = "No recommendations found for this user."

    return render_template(
        'index.html',
        recommendations=recommendations,
        error=error
    )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

