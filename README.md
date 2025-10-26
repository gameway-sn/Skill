# SkillSync

SkillSync is an AI-powered resume optimization tool designed to help job seekers enhance their resumes for better ATS (Applicant Tracking System) compatibility and job matching.

## Features
- Upload your resume in PDF format
- Analyze your resume against a job description
- Get AI-driven feedback, skills gap analysis, and personalized recommendations
- Generate an optimized, ATS-friendly PDF resume
- Built with Python and Streamlit
- Integrates Google Generative AI (Gemini 1.5 Flash)

## Model Used
SkillSync uses the Google Generative AI model: **Gemini 1.5 Flash** for resume analysis, feedback, and optimization.

## How It Works
1. Upload your resume (PDF)
2. Paste the job description
3. Receive actionable insights and suggestions from the AI
4. Download your optimized resume

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/Greavan/SkillSync.git
   ```
2. Create and activate a Python virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Add your Google API key to a `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
5. Run the app:
   ```
   streamlit run app.py
   ```

## Project Structure
- `app.py` - Main Streamlit app
- `utils.py` - Utility functions for PDF handling and AI requests
- `prompts.py` - AI prompt templates
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (not tracked in git)

