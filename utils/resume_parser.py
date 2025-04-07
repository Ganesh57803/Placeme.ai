import PyPDF2
import docx
import re
from io import BytesIO
class ResumeParser:
    def extract_text(self, file):
        """Extract text from PDF or DOCX file"""
        if file.name.endswith('.pdf'):
            return self._extract_text_from_pdf(file)
        elif file.name.endswith('.docx'):
            return self._extract_text_from_docx(file)
        else:
            raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

    def _extract_text_from_pdf(self, pdf_file):
        """Extract text from PDF file"""
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()

    def _extract_text_from_docx(self, docx_file):
        """Extract text from DOCX file"""
        doc = docx.Document(BytesIO(docx_file.read()))
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
            
    def parse(self, file):
        text = self.extract_text(file)
        
        # Simple keyword-based parsing
        skills = []
        experience = []
        education = []
        
        # Common programming languages and tools
        skill_keywords = ['python', 'java', 'javascript', 'html', 'css', 'sql', 'react', 'angular', 'vue', 
                         'node', 'express', 'django', 'flask', 'spring', 'docker', 'kubernetes', 'aws', 
                         'azure', 'git', 'jenkins', 'jira']
                         
        # Look for skills
        text_lower = text.lower()
        for skill in skill_keywords:
            if skill in text_lower:
                skills.append(skill)
                
        return {
            "skills": skills,
            "experience": experience,
            "education": education,
            "raw_text": text
        }
