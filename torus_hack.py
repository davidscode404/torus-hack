import os
import google.generativeai as genai

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

API_KEY = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash-8b')

system_prompt = read_markdown_file('systemprompt_2.md')

response = model.generate_content(system_prompt)
print(response.text)