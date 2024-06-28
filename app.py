import streamlit as st
import re

# Function to extract lines with the specified pattern
def extract_lines_with_pattern(text, pattern):
    lines = text.split('\n')
    matched_lines = [line for line in lines if re.search(pattern, line)]
    return matched_lines

# Streamlit app
def main():
    st.title("Code Line Extractor")

    st.write("""
    Upload your code file, and this app will extract lines containing the pattern:
    `<div class="KL4NAf">cfActivities.json</div>`
    """)

    uploaded_file = st.file_uploader("Choose a file", type=["txt", "py", "html", "css", "js"])

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        pattern = r'<div class="KL4NAf">cfActivities\.json<\/div>'
        extracted_lines = extract_lines_with_pattern(text, pattern)

        if extracted_lines:
            st.write("Extracted Lines:")
            for line in extracted_lines:
                st.code(line, language="html")
        else:
            st.write("No matching lines found.")

if __name__ == "__main__":
    main()
