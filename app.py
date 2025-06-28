from flask import Flask, render_template, request, redirect
import os
from google.cloud import firestore

app = Flask(__name__)

# Firestore authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firebase-key.json"
db = firestore.Client()

students = []
notices = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'name' in request.form:
            # Student data submitted
            name = request.form['name']
            roll = request.form['roll']
            department = request.form['department']
            marks = int(request.form['marks'])
            attendance = int(request.form['attendance'])
            status = 'Pass' if marks >= 40 else 'Fail'

            student_data = {
                'name': name,
                'roll': roll,
                'department': department,
                'marks': marks,
                'attendance': attendance,
                'status': status
            }

            # Save to Firestore
            db.collection("students").add(student_data)

        elif 'notice' in request.form:
            # Notice submitted
            notice_text = request.form['notice']
            db.collection("notices").add({'notice': notice_text})

        return redirect('/')  # ✅ Prevent form re-submission on reload

    # 🔄 Load data from Firestore
    students.clear()
    notices.clear()

    students_docs = db.collection("students").stream()
    for doc in students_docs:
        students.append(doc.to_dict())

    notices_docs = db.collection("notices").stream()
    for doc in notices_docs:
        notices.append(doc.to_dict().get('notice', ''))

    return render_template('index.html', students=students, notices=notices)

if __name__ == '__main__':
    app.run(debug=True)
