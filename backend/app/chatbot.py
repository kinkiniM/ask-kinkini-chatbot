# from faqs import FAQS


# CONTACT_DETAILS = """
# You can contact Kinkini through:

# Email: kinkinimajumder@gmail.com    
# LinkedIn: Add your LinkedIn profile link here  

# """


# DEFAULT_RESPONSE = f"""
# I may not have the exact answer for that yet.

# You can ask me about:

# - Kinkini's work experience
# - Sampurna Financial Services work
# - Capgemini work
# - AI skills
# - Data science skills
# - Projects
# - Services
# - Pricing
# - Contact details

# For anything specific, please contact Kinkini directly.

# {CONTACT_DETAILS}
# """


# def get_bot_response(user_input: str) -> str:
#     """
#     Simple keyword-based FAQ matching.
#     No LLM API is used in Phase 1.
#     """

#     if not user_input or not user_input.strip():
#         return "Please ask me something about Kinkini, her skills, projects, services, or pricing."

#     cleaned_input = user_input.lower().strip()

#     all_matches = []

#     for category, data in FAQS.items():
#         for question in data["questions"]:
#             keyword = question.lower().strip()

#             if keyword == cleaned_input:
#                 all_matches.append((len(keyword), data["answer"]))

#             elif keyword in cleaned_input:
#                 all_matches.append((len(keyword), data["answer"]))

#     if all_matches:
#         # Return the longest matching keyword answer.
#         # Example: "capgemini experience" wins over only "experience".
#         all_matches.sort(reverse=True, key=lambda x: x[0])
#         return all_matches[0][1]

#     return DEFAULT_RESPONSE

import os

from openai import OpenAI
from dotenv import load_dotenv
from profile import PROFILE

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY"),
)

SYSTEM_PROMPT = f"""
You are Ask Kinkini.

Answer ONLY using the following information.

{PROFILE}
"""

def get_bot_response(user_input: str) -> str:
    """
    Uses NVIDIA NIM (Mistral) instead of keyword matching.
    """

    if not user_input or not user_input.strip():
        return (
            "Please ask me something about Kinkini, her experience, "
            "projects, skills, or services."
        )

    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-medium-3.5-128b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
            temperature=0.3,
            max_tokens=512,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error connecting to NVIDIA API: {str(e)}"