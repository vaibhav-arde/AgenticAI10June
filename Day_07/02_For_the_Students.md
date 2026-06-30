# 🎓 Student Reference Guide: Advanced Prompt Engineering

## Welcome to Day 7! 🚀

Today we shifted our mindset from writing creative prompts to building **programmatic interfaces** with AI. This guide contains key cheat sheets, setup guides, and code templates from today's lecture. Keep it open while writing your assignment!

---

## 📌 Core Concepts Cheat Sheet

### 1. System Prompts (Permanent Rules)
System instructions are the foundation rules the model must *always* follow. Unlike user input, system instructions are set during model initialization.
```python
import google.generativeai as genai

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a strict data clerk. Answer only in JSON."
)
```

### 2. Structured Outputs (JSON Schema)
To integrate an LLM with databases, we need a predictable JSON output. We define the schema using **Pydantic** and configure Gemini's `GenerationConfig`.
```python
from pydantic import BaseModel, Field

class StudentResumeSchema(BaseModel):
    candidate_name: str = Field(description="Full name of applicant")
    skills: list[str] = Field(description="Technical skills like Python, Java, SQL")
    total_experience_months: int = Field(description="Total work experience in months")
    has_projects: bool = Field(description="True if projects are mentioned, else False")

# Set schema configuration in the generation config
config = genai.GenerationConfig(
    response_mime_type="application/json",
    response_schema=StudentResumeSchema
)

response = model.generate_content("Analyze: Amit Kumar has 2 years of Java experience...", generation_config=config)
print(response.text) # Guaranteed to be a valid JSON string matching StudentResumeSchema
```

### 3. Function Calling (Tool Use)
Function calling allows Gemini to interface with your Python functions (e.g. databases, local APIs).
```python
# 1. Define your Python function with clear docstrings and type hints
def get_placement_drives(branch: str) -> str:
    """Fetch active placement drives for a specific engineering branch.
    
    Args:
        branch: The engineering branch (e.g., 'CSE', 'ECE', 'ME')
    """
    # In a real app, this queries a database
    if branch.upper() == "CSE":
        return "TCS on 12th June, Infosys on 15th June"
    return "TCS on 12th June"

# 2. Register the tool during model creation
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=[get_placement_drives] # Pass functions directly
)

# 3. Start a chat session with automatic execution enabled
chat = model.start_chat(enable_automatic_function_calling=True)
response = chat.send_message("What companies are visiting for CSE students?")
print(response.text)
```

---

## 🛠️ Local Environment Setup Guide

Make sure your workspace is running with `uv`. Follow these steps to install and set up:

### Step 1: Install packages
```bash
uv add google-generativeai pydantic python-dotenv
```

### Step 2: Configure Environment Keys
Create a `.env` file in the root of your project:
```env
GEMINI_API_KEY=AIzaSyYourKeyHere...
```

### Step 3: Load Keys in Python
```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

---

## 🐢 Troubleshooting & Common Errors

### 1. `ValidationError` in Pydantic
- **Why it happens:** The model outputted a format that does not match your schema (e.g., returned a string instead of a list, or returned `None` for a field that wasn't marked optional).
- **How to fix:** 
  1. Add detailed descriptions in `Field(description="...")` to guide the model.
  2. Make fields optional using `field: str | None = None` so that missing values don't crash your parser.

### 2. LLM ignores Function Calling
- **Why it happens:** You forgot to write a docstring or arguments type hints in your Python function. The API cannot convert a Python function into an OpenAPI schema without comments.
- **How to fix:** Always write clear, descriptive docstrings and type annotations:
  ```python
  def calculate_tax(salary: float) -> float: # <-- Type hint
      """Calculate income tax based on Indian tax rules. # <-- Docstring
      
      Args:
          salary: The annual salary in INR.
      """
  ```

---

## 📚 Resources & Official Links
- [Pydantic Official Documentation](https://docs.pydantic.dev/latest/)
- [Gemini SDK Structured Outputs Guide](https://ai.google.dev/gemini-api/docs/structured-outputs?lang=python)
- [Gemini SDK Function Calling Guide](https://ai.google.dev/gemini-api/docs/function-calling?lang=python)
