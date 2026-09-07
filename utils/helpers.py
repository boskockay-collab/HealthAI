"""
HealthAI Helper Functions

This module contains small supporting functions used
throughout the HealthAI application.
"""


def clean_text(text):
    """
    Clean unnecessary spaces from user input.
    """

    if not text:
        return ""

    return " ".join(text.strip().split())


def validate_symptom_input(text):
    """
    Check whether the user entered valid symptom information.

    Returns:
        (True, "") if valid
        (False, error message) if invalid
    """

    cleaned_text = clean_text(text)

    if not cleaned_text:
        return False, "Please enter your symptoms first."

    if len(cleaned_text) < 3:
        return False, (
            "Please provide a little more information "
            "about your symptoms."
        )

    return True, ""


def format_symptom_list(symptoms):
    """
    Convert a list of symptoms into readable text.
    """

    if not symptoms:
        return "No specific symptoms matched."

    return ", ".join(symptoms)


def get_match_strength(matched_count):
    """
    Describe the strength of a symptom overlap.

    This is NOT a medical confidence score.
    """

    if matched_count >= 4:
        return "Strong symptom overlap"

    if matched_count >= 2:
        return "Moderate symptom overlap"

    return "Limited symptom overlap"


def get_disclaimer():
    """
    Return the main HealthAI safety disclaimer.
    """

    return (
        "HealthAI provides general health information only. "
        "It does not diagnose diseases or replace a qualified "
        "healthcare professional."
    )


def get_emergency_message():
    """
    Return the standard emergency warning message.
    """

    return (
        "If you are experiencing severe symptoms or a medical "
        "emergency, seek urgent medical attention immediately."
    )
