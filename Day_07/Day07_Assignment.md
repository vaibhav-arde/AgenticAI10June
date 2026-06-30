dgiag

# 📝 Day 7 Assignment: Resume Analyzer CLI

## 💼 Business Scenario

You have joined the college placement cell of an engineering institute in Coimbatore. The placement season is starting, and major IT firms (like TCS, Wipro, and local startups) are visiting. The placement director wants you to build a Python CLI utility called **Resume Analyzer** that helps students audit their resumes against actual job postings.

The tool must extract structured metadata, calculate similarity scores, and generate interview questions for the student to practice before the real company exams.

---

## 🎯 Objectives

Build a Python script that accepts:

1. **Raw Resume Text** (representing candidate profile).
2. **Job Description Text** (representing employer expectations).

The program must:

1. Parse the resume into a structured schema using **Pydantic** validation and **Gemini API**.
2. Run a comparison prompt to analyze skill gaps, calculate matching scores, and generate custom interview questions.
3. Programmatically evaluate the output to ensure it matches the requested schema and does not contain hallucinations.

---

## 📋 Detailed Requirements

### 1. The Structured Resume Schema (Pydantic)

Create a Pydantic model named `ResumeAnalysis` to capture:

- `candidate_name`: Name of applicant (String)
- `email`: Valid email address (String)
- `skills_present`: List of technical skills found in resume (List of strings)
- `skills_missing`: List of important skills listed in the Job Description but *missing* from the resume (List of strings)
- `match_score_percentage`: A float score from 0.0 to 100.0 indicating overall alignment between candidate skills and the job description.
- `experience_level`: A string classifying candidate seniority: `BEGINNER`, `INTERMEDIATE`, or `ADVANCED`.
- `interview_questions`: A list of exactly **3 customized interview questions** based on the candidate's gaps or project details.

### 2. System Instructions

Define a system prompt for the model ensuring:

- Strictly objective evaluations.
- No hallucinated skills; only extract skills explicitly mentioned in the text.
- Formats final output exclusively as valid JSON matching the schema.

### 3. Programmatic Evaluation Suite

Write a testing function `run_evaluation_suite(output_json: str, job_desc: str) -> dict` in your script. The function must programmatically verify:

- **Rule 1 (Schema Check):** Attempts to parse the JSON string back into the Pydantic class. Returns a boolean success flag.
- **Rule 2 (Name Presence):** Asserts the candidate name is not `"Unknown"` and has at least two words.
- **Rule 3 (Validation Boundaries):** Confirms that `match_score_percentage` is between 0.0 and 100.0.
- **Rule 4 (List Length):** Ensures the `interview_questions` array has exactly 3 elements.

---

## 🌟 Bonus Tasks (For Extra Credit)

1. **GitHub Link Extractor:** Add a schema field `github_link` (String or None). Parse the resume text to extract the candidate's GitHub profile URL. If no GitHub URL is found, return `None`.
2. **Batch Processing:** Enable the script to accept a folder path containing multiple raw text files (`resume1.txt`, `resume2.txt`), process them in a loop, and export a consolidated Excel/CSV file containing name, email, match score, and experience level for all candidates.

---

## 📊 Evaluation Rubric (100 Marks Total)

| Criteria                                   | Max Marks | Description                                                                                                                              |
| :----------------------------------------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Pydantic Schema Design**           | 25 Marks  | Schema contains all requested fields, appropriate type hints, and descriptive metadata fields.                                           |
| **JSON Extraction Integrity**        | 25 Marks  | API successfully converts raw resume text and job description into valid, compliant JSON using constrained generation. No syntax bugs.   |
| **Logic & Match Score Calculations** | 20 Marks  | The generated gap analysis is logical. The model extracts valid missing skills and maps them correct to the job description constraints. |
| **Programmatic Evaluation Suite**    | 20 Marks  | Evaluation checks execute and validate output boundaries without runtime crashes.                                                        |
| **Bonus Features**                   | 10 Marks  | Batch processing from folders and extracting GitHub links successfully.                                                                  |

---

## 📂 Submission Format

Your submission folder must be initialized with `uv`:

```bash
uv init day7_assignment
cd day7_assignment
uv add google-generativeai pydantic python-dotenv
```

Implement your code in `main.py` (or a notebook `solution.ipynb`).

Your directory must have this structure:

```
day7_assignment/
├── pyproject.toml
├── .env                  <-- Include your dummy/real keys here
└── main.py
```

Submit your completed `main.py` script.