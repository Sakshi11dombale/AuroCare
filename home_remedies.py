import tkinter as tk
from tkinter import ttk, messagebox

# Enhanced medicine data with age group dosage info
symptom_data = {
    "headache": {
        "remedies": ["Cold compress", "Dark room rest", "Peppermint oil massage"],
        "medicines": [{
            "name": "Ibuprofen",
            "dosage": "200mg",
            "usage": "Every 8 hours",
            "description": "Children: 100mg, Adults: 200mg, Seniors: 100mg"
        }]
    },
    "cold": {
        "remedies": ["Ginger tea", "Steam inhalation", "Salt water gargle"],
        "medicines": [{
            "name": "Paracetamol",
            "dosage": "500mg",
            "usage": "Every 6 hours",
            "description": "Children: 250mg, Adults: 500mg, Seniors: 250–500mg"
        }]
    },
    "fever": {
        "remedies": ["ORS", "Cold compress", "Tulsi tea"],
        "medicines": [{
            "name": "Paracetamol",
            "dosage": "500mg",
            "usage": "Every 6 hours",
            "description": "Children: 250mg, Adults: 500mg, Seniors: 250–500mg"
        }]
    },
    "dizziness": {
        "remedies": ["Glucose Intake", "Lemon water", "Honey + Apple cider vinegar(	Mix 1 tsp honey and 1 tsp ACV in warm water. Helps with low blood sugar or pressure.)","Eat a banana"," Avoid sudden movements"],
        "medicines": [{
            "name": "Ondansetron",
            "dosage": "4–8 mg ",
            "usage": "Take at the onset of symptoms",
            "description": "Children: 	2 mg, Adults: 	4–8 mg, Seniors: 4 mg"
        }]
    },
     "Frequent Urination": {
        "medicines": [{
        "name": "Tolterodine",
        "dosage": "2–4 mg",
        "usage": "Once or twice daily",
        "description": "Children: Not recommended, Adults: 4 mg, Seniors: 2 mg. Used for overactive bladder. Avoid in glaucoma patients."

        }]
    },
    " Frequent Infections": {
        "medicines": [{
        "name": "Amoxicillin",
        "dosage": "250–500 mg",
        "usage": "Every 8 hours for 5–7 days",
        "description": "Children: 250 mg, Adults: 500 mg, Seniors: 250–500 mg. Use for bacterial infections like UTI or skin infections."
        }]

    },
}

critical_diseases = {
    "diabetes": {
        "symptoms": ["frequent urination", "excessive thirst", "blurred vision","dizziness"," Frequent infections"],
        "advice": ["Limit sugar intake", "Exercise regularly", "Monitor blood glucose"],
        "medicines": [{
            "name": "Metformin",
            "dosage": "500mg",
            "usage": "Twice daily",
            "description": "Consult doctor for dosage based on glucose level"
        }]
    },
    "cancer": {
        "symptoms": ["unexplained weight loss", "lumps", "persistent cough"],
        "advice": ["Regular screenings", "Avoid smoking", "Eat antioxidant-rich foods"],
        "medicines": []
    },
    "covid": {
        "symptoms": ["fever", "dry cough", "loss of smell"],
        "advice": ["Isolate immediately", "Take a COVID test", "Stay hydrated"],
        "medicines": [{
            "name": "Paracetamol",
            "dosage": "500mg",
            "usage": "Every 6 hours",
            "description": "For fever and body ache"
        }]
    }
}



def is_vitals_normal(temp: float, pulse: int) -> bool:
    return 36.1 <= temp <= 37.2 and 60 <= pulse <= 100

class DoctorConsultationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Consultation with Remedies & Age-Specific Medicines")

        self.symptom_vars = {}
        self.setup_ui()

    def setup_ui(self):
        # Vitals input
        frame = ttk.Frame(self.root, padding=10)
        frame.pack()

        ttk.Label(frame, text="👨‍⚕️ Patient Vitals", font=("Helvetica", 14, "bold")).grid(column=0, row=0, columnspan=2, pady=5)

        ttk.Label(frame, text="Temperature (°C):").grid(column=0, row=1, sticky='e')
        self.temp_entry = ttk.Entry(frame)
        self.temp_entry.grid(column=1, row=1)

        ttk.Label(frame, text="Pulse Rate (bpm):").grid(column=0, row=2, sticky='e')
        self.pulse_entry = ttk.Entry(frame)
        self.pulse_entry.grid(column=1, row=2)

        self.check_button = ttk.Button(frame, text="Check Vitals", command=self.check_vitals)
        self.check_button.grid(column=0, row=3, columnspan=2, pady=10)

        # Symptom selection
        self.symptom_frame = ttk.Labelframe(self.root, text="🩺 Select 1–3 Symptoms", padding=10)
        row = 0
        for symptom in symptom_data.keys():
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(self.symptom_frame, text=symptom.title(), variable=var)
            chk.grid(column=row % 2, row=row // 2, sticky='w', padx=5, pady=2)
            self.symptom_vars[symptom] = var
            row += 1

        self.get_suggestions_button = ttk.Button(self.symptom_frame, text="Get Suggestions", command=self.show_suggestions)

        # Output area
        self.output_box = tk.Text(self.root, height=25, width=80, state='disabled')

    def check_vitals(self):
        try:
            temp = float(self.temp_entry.get())
            pulse = int(self.pulse_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for temperature and pulse.")
            return

        self.vitals_ok = is_vitals_normal(temp, pulse)

        if self.vitals_ok:
            messagebox.showinfo("Vitals Normal", "Vitals are normal. We will suggest home remedies.")
        else:
            messagebox.showwarning("Vitals Not Normal", "Vitals are not normal. Medicines will be included.")

        self.symptom_frame.pack(pady=10)
        self.get_suggestions_button.grid(column=0, row=(len(self.symptom_vars) + 1) // 2, columnspan=2, pady=10)

    def show_suggestions(self):
        selected = [sym for sym, var in self.symptom_vars.items() if var.get()]
        if not (1 <= len(selected) <= 3):
            messagebox.showwarning("Select Symptoms", "Please select 1 to 3 symptoms.")
            return

        self.output_box.configure(state='normal')
        self.output_box.delete("1.0", tk.END)

        for symptom in selected:
            data = symptom_data.get(symptom, {})
            remedies = data.get("remedies", [])
            medicines = data.get("medicines", [])

            self.output_box.insert(tk.END, f"🔸 {symptom.title()}\n")
            self.output_box.insert(tk.END, "🌿 Home Remedies:\n")
            for remedy in remedies:
                self.output_box.insert(tk.END, f"• {remedy}\n")

            if not self.vitals_ok:
                self.output_box.insert(tk.END, "\n💊 Suggested Medicines:\n")
                for med in medicines:
                    self.output_box.insert(tk.END, f"• {med['name']} - {med['dosage']} - {med['usage']}\n")
                    self.output_box.insert(tk.END, f"  ⤷ Age Groups: {med['description']}\n")
            self.output_box.insert(tk.END, "\n")

        self.output_box.configure(state='disabled')
        self.output_box.pack(pady=10)

# Run the app
root = tk.Tk()
app = DoctorConsultationApp(root)
root.mainloop()
