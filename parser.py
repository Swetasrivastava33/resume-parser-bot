import spacy

nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text):
    skills = ['python', 'sql', 'excel', 'tableau', 'power bi', 'javascript', 'html', 'css', 'aws', 'react']
    return [skill for skill in skills if skill.lower() in text.lower()]

def extract_education(text):
    keywords = ['b.tech', 'm.tech', 'bachelor', 'master', 'phd', 'mba']
    return [kw for kw in keywords if kw in text.lower()]
