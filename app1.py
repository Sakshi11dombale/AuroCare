from flask import Flask, render_template, request
from home_remedies import symptom_data, critical_diseases
from ai_engine import analyze_vitals

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            temperature = float(request.form["temperature"])
            spo2 = int(request.form["spo2"])
            heart_rate = int(request.form["heart_rate"])
            age_group = request.form["age_group"]
            symptoms = request.form.getlist("symptoms")

            issues = analyze_vitals({
                "temperature": temperature,
                "SpO2": spo2,
                "heart_rate": heart_rate
            })

            suggestions = []
            for sym in symptoms:
                data = symptom_data.get(sym, {})
                remedies = data.get("remedies", [])
                meds = data.get("medicines", [])
                suggestions.append({
                    "symptom": sym,
                    "remedies": remedies,
                    "medicines": meds if issues else []
                })

            critical_matches = []
            for disease, data in critical_diseases.items():
                matched = any(sym in symptoms for sym in data["symptoms"])
                if matched:
                    critical_matches.append({
                        "name": disease.title(),
                        "symptoms": data["symptoms"],
                        "advice": data["advice"],
                        "medicines": data["medicines"]
                    })

            result = {
                "temperature": temperature,
                "spo2": spo2,
                "heart_rate": heart_rate,
                "issues": issues,
                "age_group": age_group,
                "suggestions": suggestions,
                "symptoms": symptoms,
                "critical_matches": critical_matches
            }
        except Exception as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result, symptoms=symptom_data.keys())

if __name__ == "__main__":
    app.run(debug=True)

