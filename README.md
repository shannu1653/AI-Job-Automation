AI Job Application Automation

Requirements

Python 3.13+

Ollama

Gmail App Password

Installation

1.

git clone <repo>

2.

cd AI_Job_Automation

3.

python -m venv venv

4.

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

5.

pip install -r requirements.txt

6.

Install Ollama

7.

Pull model

ollama pull llama3.2:1b

8.

Copy

.env.example

to

.env

9.

Update Gmail credentials

10.

Run

python src/main.py