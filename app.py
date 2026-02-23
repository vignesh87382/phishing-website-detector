from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

html = """
<h2>Phishing Website Detector</h2>
<form method="post">
    Enter features (comma separated):<br>
    <input name="features">
    <input type="submit">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        features = list(map(float, request.form["features"].split(",")))
        prediction = model.predict([features])
        if prediction[0] == 1:
            return "⚠️ Phishing Website"
        else:
            return "✅ Legit Website"
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
