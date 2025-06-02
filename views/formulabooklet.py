import streamlit as st

def downloadPDF(filepath):
    with open(filepath, "rb") as f:
        pdf_bytes = f.read()
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name=filepath.split("/")[-1],
        mime="application/pdf"
    )

# Main
options = ['MATH 101', 'PHYS 158', 'CHEM 154']
selected_subject = st.selectbox("Choose a subject:", options)

st.write(f"You selected: {selected_subject}")

if selected_subject == 'MATH 101':
    st.write("Note: This booklet provided by the faculty shows very few of the formulas ACTUALLY used in the course, and this formula booklet was only usable during the 2025 examination. Formula booklets are not permitted during any of the two midterms.")
    pdf_path = "assets/math101formulasheet.pdf"
    downloadPDF(pdf_path)

elif selected_subject == 'PHYS 158':
    pdf_path = "assets/phys158formulasheet.pdf"
    downloadPDF(pdf_path)

elif selected_subject == 'CHEM 154':
    pdf_path = "assets/chem154formulasheet.pdf"
    downloadPDF(pdf_path)
