import streamlit as st

from ai.emergency_detector import detect_emergency
from ai.symptom_analyzer import analyze_symptoms
from utils.helpers import (
    validate_symptom_input,
    format_symptom_list,
    get_match_strength,
    get_disclaimer,
    get_emergency_message
)


st.set_page_config(
    page_title="HealthAI – Intelligent Health Assistant",
    page_icon="🩺",
    layout="centered"
)


st.title("🩺 HealthAI")
st.subheader("Intelligent Health Assistant")

st.write(
    "HealthAI helps users understand common symptom patterns "
    "and provides general health information and guidance."
)

st.info(
    "⚠️ HealthAI is an educational support tool. "
    "It does not provide a medical diagnosis."
)


st.markdown("### 📝 Describe Your Symptoms")

symptoms = st.text_area(
    "Enter the symptoms you are experiencing:",
    placeholder=(
        "Example: headache, fever, sore throat and weakness..."
    ),
    height=150
)


if st.button("🔍 Analyze Symptoms", use_container_width=True):

    valid, error_message = validate_symptom_input(symptoms)

    if not valid:
        st.error(error_message)

    else:

        emergency_result = detect_emergency(symptoms)

        if emergency_result["emergency"]:

            st.error("🚨 POTENTIAL MEDICAL EMERGENCY")

            st.warning(
                emergency_result["message"]
            )

            st.markdown("### Warning Signs Detected")

            for sign in emergency_result["matched_signs"]:

                st.write(
                    f"• {sign['sign'].capitalize()}"
                )

            st.error(
                get_emergency_message()
            )

        else:

            st.success(
                "✅ No obvious emergency warning signs were detected."
            )

        st.markdown("---")
        st.markdown("### 🤖 HealthAI Analysis")

        with st.spinner("Analyzing your symptoms..."):

            results = analyze_symptoms(
                symptoms,
                max_results=3
            )

        if results:

            st.write(
                "HealthAI found the following possible symptom patterns:"
            )

            for number, result in enumerate(results, start=1):

                st.markdown(
                    f"### {number}. {result['name']}"
                )

                st.write(
                    result["description"]
                )

                match_strength = get_match_strength(
                    len(result["matched_symptoms"])
                )

                st.write(
                    f"**Match strength:** {match_strength}"
                )

                st.write(
                    "**Matching symptoms:** "
                    + format_symptom_list(
                        result["matched_symptoms"]
                    )
                )

                st.markdown("**General guidance:**")

                for advice in result["guidance"]:

                    st.write(
                        f"• {advice}"
                    )

                st.warning(
                    "When to seek medical care: "
                    + result["seek_care"]
                )

                st.markdown("---")

        else:

            st.warning(
                "HealthAI could not find a clear symptom pattern "
                "from the information provided."
            )

            st.write(
                "Consider providing more details about your symptoms "
                "and how long you have experienced them."
            )


st.markdown("---")

st.markdown("### ⚕️ Important Health Notice")

st.write(
    get_disclaimer()
)

st.write(
    "If your symptoms are severe, rapidly worsening, or you "
    "are concerned about your condition, seek help from a "
    "qualified healthcare professional."
)

st.markdown("---")

st.caption(
    "HealthAI – Intelligent Health Assistant | "
    "Educational AI Project"
)
