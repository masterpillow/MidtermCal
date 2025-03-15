📌 Project Overview
This is a simple Flask-based calculator that supports basic arithmetic operations: addition, subtraction, multiplication, and division. The application provides separate routes for each operation and handles division by zero properly. The results are displayed using Flask templates.

🚀 Features
Addition (/add/<int:a>/<int:b> → returns a + b)

Subtraction (/subtract/<int:a>/<int:b> → returns a - b)

Multiplication (/multiply/<int:a>/<int:b> → returns a * b)

Division (/divide/<int:a>/<int:b> → returns a / b)

Handles division by zero gracefully

Uses Flask templates to display results

Git workflow includes at least one feature branch

🛠️ Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/masterpillow/MidtermCal.git
cd MidtermCal

2️⃣ Set Up a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # For macOS

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Flask Application

python3 app.py
To run on a specific port (e.g., 8080):

python3 app.py --host=0.0.0.0 --port=8080

🌍 Usage
Once the server is running, open a browser and test the API using the following routes:

Addition:

http://127.0.0.1:8080/add/10/5

Subtraction:

http://127.0.0.1:8080/subtract/10/5

Multiplication:

http://127.0.0.1:8080/multiply/10/5

Division:

http://127.0.0.1:8080/divide/10/5

