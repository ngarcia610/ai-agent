import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
a = response.text
pt = response.usage_metadata.prompt_token_count
rt = response.usage_metadata.candidates_token_count

print(f"Response: {a}")
print(f"Prompt tokens: {pt}")
print(f"Response tokens: {rt}")
