import os
# 1. Import the new library
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class AIIntegration:
    def __init__(self, api_key=None):
        # 2. Get the GEMINI_API_KEY and configure the library
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if self.api_key:
            genai.configure(api_key=self.api_key)
            # 3. Create a model instance
            # self.model = genai.GenerativeModel('gemini-pro')
            self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
        else:
            self.model = None

    def generate_subject(self, context):
        """Generates an email subject based on the conversation context using Gemini."""
        if not self.model:
            return 'AI Agent Task - [Your Name]'
        
        prompt = f"Generate a professional, concise email subject for the following context: {context}"
        try:
            # 4. Call the Gemini API to generate content
            response = self.model.generate_content(prompt)
            # 5. Get the text from the response
            return response.text.strip()
        except Exception as e:
            print(f"Gemini subject generation error: {e}")
            return 'AI Agent Task - [Your Name]'

    def generate_body(self, context):
        """Generates an email body based on the conversation context using Gemini."""
        if not self.model:
            return 'Dear Manager,\n\nI would like to apply for leave from next Monday to Wednesday.\n\nBest regards,\n[Your Name]'
        
        prompt = f"Write a professional email body for the following context: {context}"
        try:
            # 4. Call the Gemini API to generate content
            response = self.model.generate_content(prompt)
            # 5. Get the text from the response
            return response.text.strip()
        except Exception as e:
            print(f"Gemini body generation error: {e}")
            return 'Dear Manager,\n\nI would like to apply for leave from next Monday to Wednesday.\n\nBest regards,\n[Your Name]'
