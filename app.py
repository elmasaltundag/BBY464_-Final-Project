from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "42d12a14a053aaca80be935809013a88"
API_URL = "https://api.themoviedb.org/3/search/tv"

@app.route("/", methods=["GET", "POST"])
def index():
    drama = None
    error = None

    if request.method == "POST":
        query = request.form["query"]
        params = {
            "api_key": API_KEY,
            "query": query,
            "language": "ko-KR"
        }

        try:
            response = requests.get(API_URL, params=params)
            response.raise_for_status()
            data = response.json()

            if data["results"]:
                drama = data["results"][0]  # İlk sonucu al
            else:
                error = "Sonuç bulunamadı."
        except Exception as e:
            error = f"Hata oluştu: {str(e)}"

    return render_template("index.html", drama=drama, error=error)

if __name__ == "__main__":
    app.run(debug=True)
