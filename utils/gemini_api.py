import requests

class GeminiAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"

    def analyze_resume(self, raw_text):
        """Use Gemini API to convert resume text to structured JSON"""
        headers = {
            "Content-Type": "application/json"
        }

        prompt = (
    "You are a resume parser. Extract the following structured information from the resume text "
    "and return it as well-formatted JSON.\n\n"
    "Include the following fields:\n"
    "- Name\n"
    "- Contact Information\n"
    "- Skills (categorized):\n"
    "  - Programming Languages\n"
    "  - Frameworks\n"
    "  - Libraries/Tools\n"
    "  - Databases\n"
    "  - Cloud/DevOps\n"
    "  - Other Relevant Skills\n"
    "- Work Experience (with company, role, duration, description)\n"
    "- Education (degree, institution, year, CGPA/percentage)\n"
    "- Projects (name, technologies used, description)\n"
    "- Extracurricular Activities\n\n"
    f"Resume Text:\n{raw_text}\n\n"
    "Make sure the 'skills' section is structured like this:\n\n"
    "{\n"
    "  \"skills\": {\n"
    "    \"Programming Languages\": [\"Python\", \"C++\"],\n"
    "    \"Frameworks\": [\"Streamlit\", \"Django\"],\n"
    "    \"Libraries/Tools\": [\"NumPy\", \"Pandas\"],\n"
    "    \"Databases\": [\"MySQL\", \"MongoDB\"],\n"
    "    \"Cloud/DevOps\": [\"AWS\", \"Docker\"],\n"
    "    \"Other Relevant Skills\": [\"Agile\", \"Git\"]\n"
    "  }\n"
    "}\n\n"
    "Only return a valid JSON object. Do not include explanations or commentary."
)


        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        response = requests.post(self.endpoint, json=payload, headers=headers)
        print(f"Gemini API Response: {response.status_code} - {response.text}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Gemini API Error: {response.status_code} - {response.text}")
