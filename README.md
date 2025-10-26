Skill
Skill is an AI-powered resume optimization tool designed to help job seekers enhance their resumes for better ATS (Applicant Tracking System) compatibility and job matching.

Features
Upload your resume in PDF format
Analyze your resume against a job description
Get AI-driven feedback, skills gap analysis, and personalized recommendations
Generate an optimized, ATS-friendly PDF resume
Built with Python and Streamlit
Integrates Google Generative AI (Gemini 1.5 Flash)
Model Used
SkillSync uses the Google Generative AI model: Gemini 1.5 Flash for resume analysis, feedback, and optimization.

How It Works
Upload your resume (PDF)
Paste the job description
Receive actionable insights and suggestions from the AI
Download your optimized resume
Setup Instructions
Clone the repository:
git clone https://github.com/Greavan/SkillSync.git
Create and activate a Python virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
Install dependencies:
pip install -r requirements.txt
Add your Google API key to a .env file:
GOOGLE_API_KEY=your_api_key_here
Run the app:
streamlit run app.py
Project Structure
app.py - Main Streamlit app
utils.py - Utility functions for PDF handling and AI requests
prompts.py - AI prompt templates
requirements.txt - Python dependencies
.env - Environment variables (not tracked in git)
