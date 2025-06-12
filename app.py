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
            "language": "en-US"
        }

        try:
            response = requests.get(API_URL, params=params)
            response.raise_for_status()
            data = response.json()

            if data["results"]:
                result = data["results"][0]  # İlk sonucu al

                drama = {
                    "name": result.get("name"),
                    "original_name": result.get("original_name"),
                    "overview": result.get("overview"),
                    "first_air_date": result.get("first_air_date"),
                    "vote_average": result.get("vote_average"),
                    "vote_count": result.get("vote_count"),
                    "popularity": result.get("popularity"),
                    "poster_path": result.get("poster_path")
                }
            else:
                error = "Sonuç bulunamadı."
        except Exception as e:
            error = f"Hata oluştu: {str(e)}"

    return render_template("index.html", drama=drama, error=error)

if __name__ == "__main__":
    app.run(debug=True)
