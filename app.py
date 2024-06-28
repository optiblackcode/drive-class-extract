import streamlit as st
import re
import pandas as pd

# Function to extract text inside specific HTML div class
def extract_text_with_class(text, class_name):
    pattern = f'<div class="{class_name}">(.*?)</div>'
    matches = re.findall(pattern, text)
    return matches

# Streamlit app
def main():
    st.title("HTML Class Text Extractor")

    st.write("""
    Upload your code file, and this app will extract text inside the HTML div class:
    `<div class="KL4NAf">cfActivities.json</div>`
    and display it in a table format.
    """)

    uploaded_file = st.file_uploader("Choose a file", type=["html", "txt"])

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        class_name = "KL4NAf"
        extracted_texts = extract_text_with_class(text, class_name)

        if extracted_texts:
            df = pd.DataFrame(extracted_texts, columns=["Extracted Text"])
            st.write("Extracted Texts:")
            st.table(df)
        else:
            st.write("No matching text found.")

if __name__ == "__main__":
    main()
