"""
HealthAI Emergency Detection System

This module checks a user's symptom description for potentially
serious warning signs.

IMPORTANT:
This is a safety-support feature, not a medical diagnosis system.
"""

import re


EMERGENCY_PATTERNS = {
    "breathing": [
        "difficulty breathing",
        "can't breathe",
        "cannot breathe",
        "shortness of breath",
        "severe breathing",
        "breathing difficulty",
    ],

    "chest": [
        "severe chest pain",
        "chest pressure",
        "chest pain",
        "tightness in chest",
    ],

    "consciousness": [
        "unconscious",
        "loss of consciousness",
        "passed out",
        "fainted",
        "not responding",
    ],

    "seizure": [
        "seizure",
        "convulsion",
        "convulsions",
    ],

    "stroke_warning": [
        "face drooping",
        "one sided weakness",
        "one-sided weakness",
        "slurred speech",
        "sudden weakness",
        "sudden numbness",
        "can't speak",
        "cannot speak",
    ],

    "severe_bleeding": [
        "severe bleeding",
        "heavy bleeding",
        "bleeding heavily",
        "blood loss",
    ],

    "severe_allergic_reaction": [
        "swollen tongue",
        "swelling of tongue",
        "swollen throat",
        "swelling of throat",
        "swollen lips",
        "swelling of lips",
        "severe allergic reaction",
        "anaphylaxis",
    ],

    "severe_confusion": [
        "severe confusion",
        "suddenly confused",
        "not making sense",
    ],

    "suicidal_crisis": [
        "want to kill myself",
        "want to die",
        "kill myself",
        "suicide",
        "suicidal",
    ],
}


def normalize_text(text):
    """
    Convert text to lowercase and remove unnecessary spaces.
    """
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def detect_emergency(symptoms):
    """
    Check whether the symptom description contains emergency
    warning signs.

    Returns a dictionary containing:
    - emergency: True or False
    - matched_signs: warning signs found
    - message: appropriate safety message
    """

    text = normalize_text(symptoms)

    matched_signs = []

    for category, patterns in EMERGENCY_PATTERNS.items():

        for pattern in patterns:

            if pattern in text:
                matched_signs.append({
                    "category": category,
                    "sign": pattern
                })

    if matched_signs:

        return {
            "emergency": True,
            "matched_signs": matched_signs,
            "message": (
                "Some of the symptoms you entered may indicate a "
                "medical emergency. Please seek urgent medical attention "
                "from a qualified healthcare professional or emergency "
                "medical service."
            )
        }

    return {
        "emergency": False,
        "matched_signs": [],
        "message": (
            "No obvious emergency warning signs were detected from "
            "the information provided. This does not rule out a "
            "serious medical condition."
        )
    }


def get_emergency_signs():
    """
    Return the emergency warning-sign database.
    """
    return EMERGENCY_PATTERNS
