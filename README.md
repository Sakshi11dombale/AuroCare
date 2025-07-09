 🩺 AuroCare - AI Health Monitoring & Suggestion System
       AuroCare is an AI-powered health assistant that simulates sensor-based vitals monitoring, detects abnormalities,
       and provides real-time home remedies and medicine suggestions through a beautiful web dashboard.


🚀 Features
-  Vitals Monitoring: Input temperature, heart rate, SpO₂
-  AI Health Engine: Analyzes vitals to flag abnormal conditions
-  Symptom-Based Suggestions: Choose up to 3 symptoms for remedies/meds
 - Critical Disease Detection: Detects patterns related to:
       - Diabetes
       - COVID-19
       - Cancer
- Home Remedies & Medicines: Personalized for children, adults, and seniors
- Alerts & Prevention Tips: Helps users take early action
- Modern Web UI: Built using Flask + Bootstrap



🧠 Technologies Used

- Python 3.10+
- Flask
- Jinja2 Templates
- Bootstrap 5
- `home_remedies.py` – Remedy & medicine knowledge base
- `ai_engine.py` – Vitals analyzer


🛠️ Setup Instructions

1. Clone this repo:
     ```bash
       git clone https://github.com/yourusername/aurocare.git
       cd app_design
2. Install dependencies:
       pip install flask
3. Run the app:
	   python app1.py
4. Open in browser:
	   http://127.0.0.1:5000/


📁 Folder Structure
       
	aurocare(app_design)/
        
	 └── README.md               # Project documentation
	 
         ├── app1.py                  # Flask app
         
	 ├── ai_engine.py            # Vitals analysis logic
         
	 ├── home_remedies.py        # Remedies & disease detection
         
	 ├── static/
         
	 │   └── styles.css          # UI styling
         
	 ├── templates/
         
	 │   └── index.html          # Web UI (Jinja2)
         
	 
