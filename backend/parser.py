import PyPDF2

def extract_text(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

def score_resume(text):
    keywords = ["python", "aws", "docker", "kubernetes"]

    score = 0
    for word in keywords:
        if word in text.lower():
            score += 25

    return score
