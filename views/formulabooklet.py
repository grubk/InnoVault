import streamlit as st
import base64

def viewPDF(filename):
    with open(filename, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1400" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Main
options = ['MATH 101', 'PHYS 158', 'CHEM 154']
selected_subject = st.selectbox("Choose a subject:", options)

st.write(f"You selected: {selected_subject}")

if selected_subject == 'MATH 101':
    st.write("Note: This booklet provided by the faculty shows very few of the formulas ACTUALLY used in the course, and this formula booklet was only usable during the 2025 examination. Formula booklets are not permitted during any of the two midterms.")
    viewPDF("assets/math101formulasheet.pdf")
elif selected_subject == 'PHYS 158':
    viewPDF("assets/phys158formulasheet.pdf")
elif selected_subject == 'CHEM 154':
    viewPDF("assets/chem154formulasheet.pdf")
