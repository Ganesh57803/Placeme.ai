# Placeme.ai

Placeme.ai is an intelligent tool designed to help job seekers optimize their resumes for better job opportunities. It provides insights, recommendations, and tools to create ATS-friendly resumes tailored to specific roles.

## Features

### Resume Analysis
- **ATS Compatibility Check**: Ensures your resume meets Applicant Tracking System (ATS) standards.
- **Keyword Optimization**: Identifies and suggests role-specific keywords.
- **Skills Gap Analysis**: Highlights missing skills for targeted job roles.
- **Role-Specific Feedback**: Provides actionable insights based on job descriptions.

### Resume Builder
- **Customizable Templates**: Choose from modern, minimal, professional, and creative designs.
- **AI-Powered Suggestions**: Get content recommendations for sections like skills, achievements, and experience.
- **PDF Export**: Download your resume in a professional format.

### Job Search Integration
- **LinkedIn Scraper**: Fetch real-time job listings based on your preferences.
- **Role Matching**: Align your resume with job descriptions for better chances of success.

## How It Works
1. **Upload or Create**: Import your resume in PDF/Word format or start from scratch.
2. **Analyze**: Get detailed feedback on ATS compatibility, keyword gaps, and skills alignment.
3. **Optimize**: Use AI-driven suggestions to improve your resume.
4. **Download & Apply**: Export your optimized resume and start applying for jobs.

## Tech Stack
- **Frontend**: Streamlit, HTML, CSS, JavaScript
- **Backend**: Python, Streamlit
- **Database**: SQLite3
- **Modules**: spaCy, PyPDF2, scikit-learn, Plotly, NLTK

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone 
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For MacOS/Linux
   venv\Scripts\activate     # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Contribution
Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request.



#