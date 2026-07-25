# 🤖 AI Job Application Automation

An intelligent AI-powered Job Application Automation system built with **Python**, **Ollama (Llama 3.2)**, **SQLite**, and **Gmail SMTP**.

This project automatically reads a copied Job Description, extracts job details using AI, generates a professional job application email, attaches your resume, sends the email to the recruiter, and stores the application history in a local SQLite database.

---

# 🚀 Features

- 📋 Read Job Description directly from Clipboard
- 🤖 AI-powered Job Description Analysis using Ollama
- 🔄 Automatic Fallback Parser if AI fails
- 📧 AI-generated Professional Job Application Email
- 📎 Automatic Resume Attachment
- 📨 Send Email using Gmail SMTP
- 💾 Save Applications into SQLite Database
- 🧠 Intelligent Skill Extraction
- 🏢 Company & Role Inference
- ⚡ Works with Multiple Job Platforms

---

# ✅ Supported Job Sources

- LinkedIn Jobs
- Naukri
- Indeed
- WhatsApp Recruiter Posts
- Telegram Job Posts
- Email Job Posts
- Skills-only Posts
- Incomplete Job Descriptions

---

# 🛠 Tech Stack

- Python 3.13
- Ollama
- Llama 3.2 (1B)
- SQLite
- Gmail SMTP
- PyMuPDF
- pyperclip
- python-dotenv

---

# 📂 Project Structure

```
AI_Job_Automation/
│
├── src/
│   ├── main.py
│   ├── job_analyzer.py
│   ├── parser.py
│   ├── ai_email_generator.py
│   ├── resume_reader.py
│   ├── email_sender.py
│   ├── database.py
│   ├── input_handler.py
│   ├── config.py
│   └── skills.py
│
├── resumes/
│   └── master_resume.pdf
│
├── outputs/
│
├── templates/
│
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Job_Automation.git
```

```bash
cd AI_Job_Automation
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download Ollama

https://ollama.com/download

Verify Installation

```bash
ollama --version
```

Download Model

```bash
ollama pull llama3.2:1b
```

Verify Model

```bash
ollama list
```

Expected Output

```
llama3.2:1b
```

---

# 🔐 Gmail SMTP Setup

## Enable 2-Step Verification

Go to

Google Account

↓

Security

↓

2-Step Verification

Enable it.

---

## Generate Gmail App Password

Google Account

↓

Security

↓

App Passwords

Choose

App

```
Mail
```

Device

```
AI Job Automation
```

Copy the generated 16-character App Password.

Example

```
abcd efgh ijkl mnop
```

---

# 📄 Create .env File

Copy

```
.env.example
```

Rename to

```
.env
```

Example

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

---

# 👤 Update config.py

Update your personal information.

```python
NAME = "Your Name"

TITLE = "Python Full Stack Developer"

PHONE = "+91XXXXXXXXXX"

EMAIL = "your_email@gmail.com"

LINKEDIN = "https://linkedin.com/in/your-profile"

GITHUB = "https://github.com/yourusername"

PORTFOLIO = "https://yourportfolio.com"
```

---

# 📄 Add Resume

Place your resume here

```
resumes/
```

Rename it

```
master_resume.pdf
```

Or update

```python
MASTER_RESUME
```

inside

```
config.py
```

---

# ▶️ Run Project

Copy any Job Description.

Then run

```bash
python src/main.py
```

---

# 🔄 Workflow

```
Copy Job Description
        │
        ▼
Clipboard Reader
        │
        ▼
Ollama Job Analyzer
        │
        ├──────── Success
        │
        ▼
AI Email Generator
        │
        ▼
Attach Resume
        │
        ▼
Send via Gmail SMTP
        │
        ▼
Save to SQLite Database
        │
        ▼
Application Completed
```

If AI cannot parse the Job Description

```
Ollama
   │
   ▼
Failed
   │
   ▼
Regex Parser
   │
   ▼
Continue Workflow
```

---

# 📊 Extracted Information

The AI extracts

- Company
- Role
- Recruiter Email
- Phone Number
- Location
- Experience
- Education
- Skills
- Salary
- Job Type
- Work Mode
- Deadline

---

# 🗄 Database

Every application is saved with

- Company
- Role
- Recruiter Email
- Date
- Status

---

# ❌ Common Errors

## Recruiter email not found

The copied Job Description does not contain a recruiter email.

---

## Ollama not found

Install Ollama

```
https://ollama.com/download
```

---

## Model not found

Run

```bash
ollama pull llama3.2:1b
```

---

## SMTP Authentication Failed

Use Gmail App Password

NOT

Your Gmail Login Password.

---

## Clipboard Empty

Copy the Job Description before running the project.

---

## ModuleNotFoundError

Run

```bash
pip install -r requirements.txt
```

---

# 🔒 Security

Never upload

```
.env
```

Never upload

```
database.db
```

Never upload

```
venv/
```

Use

```
.env.example
```

instead.

---

# 📌 Future Improvements

- Multi Resume Selection
- ATS Resume Optimization
- Cover Letter Generation
- LinkedIn Auto Apply
- Naukri Auto Apply
- AI Resume Customization
- Recruiter Follow-up Emails
- Interview Tracking Dashboard
- Streamlit Web Interface
- Docker Support
- REST API
- Multi-user Authentication

---

# 👨‍💻 Author

**Shanmukha Penta**

Python Full Stack Developer

📧 Email

```
pentashanmukha2002@gmail.com
```

🔗 LinkedIn

```
https://www.linkedin.com/in/shanmukhapenta/
```

💻 GitHub

```
https://github.com/shannu1653
```

🌐 Portfolio

```
https://shanmukha-portfolio-three.vercel.app/
```

---

# ⭐ Support

If you found this project useful,

please ⭐ Star this repository and share it with others.

Happy Coding! 🚀