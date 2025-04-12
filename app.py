import streamlit as st
from utils.parser import extract_text
from utils.llm_chain import summarize_and_flashcards
from utils.export_pdf import save_as_pdf
from utils.mindmap import generate_mindmap

import os

st.set_page_config(page_title="Academic Notes Summarizer", layout="wide")

st.title("📚 Academic Notes Summarizer")
st.markdown("Upload your academic notes in PDF/DOCX format and get a summary, flashcards, a mindmap, and a downloadable PDF.")

# --- File Upload ---
uploaded_file = st.file_uploader("📁 Upload Notes (.pdf or .docx)", type=["pdf", "docx"])

if uploaded_file:
    with st.spinner("📄 Extracting text..."):
        notes_text = extract_text(uploaded_file)

    if notes_text:
        st.success("✅ Notes extracted successfully!")

        with st.spinner("🤖 Generating summary and flashcards using Gemini..."):
            try:
                output = summarize_and_flashcards(notes_text)
                summary, flashcards = output.split("Flashcards:")

                st.subheader("📝 Summary")
                st.markdown(summary.strip())

                st.subheader("🧠 Flashcards")
                flashcard_lines = flashcards.strip().split("\n")
                for i in range(0, len(flashcard_lines), 2):
                    if i + 1 < len(flashcard_lines):
                        st.markdown(f"**{flashcard_lines[i]}**")  # Question
                        st.markdown(f"{flashcard_lines[i + 1]}")  # Answer

                # --- Mind Map ---
                st.subheader("🗺️ Mind Map")
                mindmap_path = generate_mindmap(summary)
                if mindmap_path and os.path.exists(mindmap_path):
                    st.image(mindmap_path, caption="Generated Mind Map", use_column_width=True)

                # --- PDF Export ---
                if st.button("📄 Export Summary & Flashcards as PDF"):
                    file_path = save_as_pdf(summary, flashcards)
                    st.success(f"✅ PDF exported successfully to: `{file_path}`")
                    with open(file_path, "rb") as f:
                        st.download_button("⬇️ Download PDF", f, file_name="summary_flashcards.pdf")

            except Exception as e:
                st.error(f"❌ Error while processing: {e}")
    else:
        st.warning("❗ Could not extract any text from the uploaded file.")
