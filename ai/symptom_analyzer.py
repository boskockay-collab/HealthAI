"""
HealthAI Symptom Analyzer

This module performs simple NLP-style symptom matching.
It compares symptoms entered by the user with the HealthAI
health knowledge base.

IMPORTANT:
The results are possible matches for educational purposes.
They are NOT medical diagnoses.
"""

import re

from data.health_knowledge import get_health_knowledge


def normalize_text(text):
    """
    Clean and normalize user input.
    """
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"[^\w\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def symptom_is_present(symptom, user_text):
    """
    Check whether a symptom or related phrase appears
    in the user's description.
    """

    symptom = normalize_text(symptom)
    user_text = normalize_text(user_text)

    if symptom in user_text:
        return True

    return False


def analyze_symptoms(user_input, max_results=3):
    """
    Compare the user's symptoms with the HealthAI knowledge base.

    Returns the most relevant possible matches.
    """

    user_text = normalize_text(user_input)

    if not user_text:
        return []

    knowledge = get_health_knowledge()

    results = []

    for condition_id, condition in knowledge.items():

        matched_symptoms = []

        for symptom in condition["symptoms"]:

            if symptom_is_present(symptom, user_text):
                matched_symptoms.append(symptom)

        if matched_symptoms:

            total_symptoms = len(condition["symptoms"])

            match_score = (
                len(matched_symptoms) / total_symptoms
            ) * 100

            results.append({
                "id": condition_id,
                "name": condition["name"],
                "description": condition["description"],
                "matched_symptoms": matched_symptoms,
                "match_score": round(match_score, 1),
                "guidance": condition["guidance"],
                "seek_care": condition["seek_care"]
            })

    results.sort(
        key=lambda result: (
            len(result["matched_symptoms"]),
            result["match_score"]
        ),
        reverse=True
    )

    return results[:max_results]


def get_primary_result(user_input):
    """
    Return the strongest possible match.

    Returns None if no match is found.
    """

    results = analyze_symptoms(user_input, max_results=1)

    if results:
        return results[0]

    return None
