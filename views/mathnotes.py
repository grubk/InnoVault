import streamlit as st
import toml
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

with open(".streamlit/secrets.toml", "r") as f:
    config = toml.load(f)

token = config.get("auth", {}).get("GITHUB_TOKEN")
if not token or not isinstance(token, str):
    raise ValueError("GITHUB_TOKEN not found in secrets.toml")

# Set up client
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def english_to_latex(math_description: str) -> str:
    """
    Converts a string describing math in English to a raw LaTeX string using the GPT model.
    """
    system_prompt = (
        "You are a LaTeX generator. Given a math expression described in plain English, "
        "you return only the equivalent LaTeX code without explanation, and without surrounding it with \\(...\\) or \\[...\\]."
    )

    response = client.complete(
        messages=[
            SystemMessage(content=system_prompt),
            UserMessage(content=math_description),
        ],
        temperature=0,
        top_p=1,
        model=model
    )

    return response.choices[0].message.content.strip()



#Main section
st.title("English to LaTex Converter ")
st.write("Date Created: 2025-06-01")
st.markdown("""
- In the text box below, write some mathematical statement in English, eg. 'Integral from 0 to 4 of 4x'
- You can be fairly free with your language. For example, 'int sqrt(x^2 + 3x)' would also work
- After pressing the 'Submit' button, your query will be converted into LaTex and can be copied using the 'Copy' button
""")
st.write("\n\n")


col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")

with col1:

    content = st.text_area("Write the statement you want converted to LaTex here:")
    if st.button("Convert to LaTex"):
        if content.strip():
            st.session_state["latex_output"] = english_to_latex(content)
        else:
            st.session_state["latex_output"] = "Converted LaTeX will display here."

with col2:

    st.write("Preview:")
    if "latex_output" in st.session_state:
        st.latex(st.session_state["latex_output"])  # no need to clean it anymore

        st.write("LaTeX Code (click to copy):")
        st.text_input(
            label="",
            value=st.session_state["latex_output"],
            key="copy_latex",
            label_visibility="collapsed"
        )


