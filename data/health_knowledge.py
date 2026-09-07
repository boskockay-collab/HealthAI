"""
HealthAI Health Knowledge Base

This module contains general health information used by the
HealthAI symptom analysis system.

IMPORTANT:
This information is for educational purposes only.
It does not provide a medical diagnosis.
"""


HEALTH_KNOWLEDGE = {

    "common_cold": {
        "name": "Common Cold",
        "description": (
            "A common viral infection that can affect the nose and throat."
        ),
        "symptoms": [
            "runny nose",
            "stuffy nose",
            "sneezing",
            "sore throat",
            "cough",
            "mild headache",
            "mild fever",
            "fatigue"
        ],
        "guidance": [
            "Get enough rest.",
            "Drink plenty of fluids.",
            "Monitor your symptoms.",
            "Avoid close contact with others if you are unwell."
        ],
        "seek_care": (
            "Seek medical advice if symptoms become severe, persist, "
            "or continue to get worse."
        )
    },


    "flu": {
        "name": "Flu-like Illness",
        "description": (
            "A viral illness that can cause fever, tiredness, "
            "body aches and respiratory symptoms."
        ),
        "symptoms": [
            "fever",
            "headache",
            "body aches",
            "muscle pain",
            "fatigue",
            "weakness",
            "cough",
            "sore throat",
            "chills"
        ],
        "guidance": [
            "Rest and allow your body time to recover.",
            "Drink enough fluids.",
            "Monitor your temperature and symptoms.",
            "Avoid spreading illness to other people."
        ],
        "seek_care": (
            "Seek medical attention if symptoms are severe, rapidly worsen, "
            "or you have difficulty breathing."
        )
    },


    "malaria_like_illness": {
        "name": "Malaria-like Symptoms",
        "description": (
            "Fever, chills, headache, weakness and body aches can occur "
            "with malaria and several other illnesses."
        ),
        "symptoms": [
            "fever",
            "high fever",
            "chills",
            "headache",
            "weakness",
            "fatigue",
            "body aches",
            "muscle pain",
            "sweating",
            "nausea",
            "vomiting"
        ],
        "guidance": [
            "If you have a fever in a malaria-risk area, consider getting "
            "tested at a health facility.",
            "Drink fluids to reduce the risk of dehydration.",
            "Monitor your symptoms carefully."
        ],
        "seek_care": (
            "Fever with severe weakness, confusion, repeated vomiting, "
            "difficulty breathing, seizures or loss of consciousness "
            "requires urgent medical attention."
        )
    },


    "tension_headache": {
        "name": "Tension Headache",
        "description": (
            "A common type of headache that may be associated with stress, "
            "fatigue or muscle tension."
        ),
        "symptoms": [
            "headache",
            "pressure in head",
            "head pressure",
            "neck pain",
            "shoulder pain",
            "fatigue",
            "stress"
        ],
        "guidance": [
            "Rest in a quiet environment.",
            "Try to maintain regular sleep.",
            "Drink enough water.",
            "Take breaks if you have been using a screen for a long time."
        ],
        "seek_care": (
            "Seek medical attention for a sudden extremely severe headache "
            "or a headache accompanied by serious neurological symptoms."
        )
    },


    "migraine": {
        "name": "Migraine-like Symptoms",
        "description": (
            "Migraine can cause moderate to severe headache and may be "
            "associated with nausea or sensitivity to light and sound."
        ),
        "symptoms": [
            "severe headache",
            "headache",
            "throbbing headache",
            "nausea",
            "vomiting",
            "sensitivity to light",
            "sensitivity to sound",
            "dizziness"
        ],
        "guidance": [
            "Rest in a quiet, dark environment.",
            "Stay hydrated.",
            "Try to identify and avoid personal triggers."
        ],
        "seek_care": (
            "Seek medical care if headaches are unusually severe, sudden, "
            "recurrent, or different from your usual headaches."
        )
    },


    "sore_throat": {
        "name": "Sore Throat / Throat Infection",
        "description": (
            "A sore throat can occur because of viral infections, "
            "irritation or other causes."
        ),
        "symptoms": [
            "sore throat",
            "throat pain",
            "difficulty swallowing",
            "swollen throat",
            "fever",
            "cough"
        ],
        "guidance": [
            "Drink plenty of fluids.",
            "Rest adequately.",
            "Monitor your symptoms.",
            "Avoid irritants such as smoke."
        ],
        "seek_care": (
            "Seek medical attention if you have severe difficulty swallowing, "
            "difficulty breathing, severe swelling or persistent symptoms."
        )
    },


    "gastroenteritis": {
        "name": "Gastrointestinal Infection",
        "description": (
            "An infection or irritation affecting the digestive system "
            "that may cause vomiting, diarrhea and abdominal discomfort."
        ),
        "symptoms": [
            "diarrhea",
            "vomiting",
            "nausea",
            "stomach pain",
            "abdominal pain",
            "stomach cramps",
            "fever",
            "weakness"
        ],
        "guidance": [
            "Drink fluids regularly.",
            "Pay attention to signs of dehydration.",
            "Rest adequately.",
            "Choose light foods if you are able to eat."
        ],
        "seek_care": (
            "Seek medical attention if there is severe dehydration, "
            "blood in stool or vomit, severe abdominal pain, "
            "or persistent vomiting."
        )
    },


    "dehydration": {
        "name": "Dehydration",
        "description": (
            "Dehydration occurs when the body loses more fluid than it takes in."
        ),
        "symptoms": [
            "thirst",
            "dry mouth",
            "weakness",
            "dizziness",
            "fatigue",
            "dark urine",
            "headache"
        ],
        "guidance": [
            "Drink fluids regularly.",
            "Increase fluid intake after heavy sweating, vomiting or diarrhea.",
            "Rest and monitor how you feel."
        ],
        "seek_care": (
            "Severe dizziness, confusion, fainting or inability to keep "
            "fluids down requires medical attention."
        )
    },


    "allergies": {
        "name": "Allergic Symptoms",
        "description": (
            "Allergies can cause symptoms when the immune system reacts "
            "to substances such as pollen, dust or other triggers."
        ),
        "symptoms": [
            "sneezing",
            "runny nose",
            "itchy eyes",
            "watery eyes",
            "nasal congestion",
            "itchy nose",
            "rash"
        ],
        "guidance": [
            "Try to identify and avoid known triggers.",
            "Keep your environment clean where possible.",
            "Monitor whether symptoms improve after avoiding the trigger."
        ],
        "seek_care": (
            "Seek emergency medical attention for severe difficulty breathing "
            "or swelling of the face, lips, tongue or throat."
        )
    },


    "urinary_tract_infection": {
        "name": "Urinary Tract Infection-like Symptoms",
        "description": (
            "Urinary symptoms such as burning during urination or frequent "
            "urination can occur with a urinary tract infection."
        ),
        "symptoms": [
            "burning urination",
            "painful urination",
            "frequent urination",
            "urgency to urinate",
            "lower abdominal pain",
            "cloudy urine"
        ],
        "guidance": [
            "Drink fluids regularly.",
            "Consider seeking medical evaluation if symptoms persist.",
            "A healthcare professional can determine whether testing is needed."
        ],
        "seek_care": (
            "Seek medical attention if urinary symptoms are accompanied by "
            "fever, severe pain, vomiting or pain in the back or side."
        )
    }
}


def get_health_knowledge():
    """
    Return the complete HealthAI knowledge base.
    """
    return HEALTH_KNOWLEDGE
