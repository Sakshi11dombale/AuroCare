def analyze_vitals(vitals):
    issues = []
    remedies = []
    if vitals["temperature"] > 38.0:
        issues.append("High fever")
    if vitals["SpO2"] < 92:
        issues.append("Low oxygen")
    if vitals["heart_rate"] > 110:
        issues.append("High heart rate")
    return issues