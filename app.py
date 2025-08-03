import streamlit as st
import os

# Ordner für Uploads
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="📤 Quick Share", layout="centered")

st.title("📤 Quick Share – Dateiaustausch online")

# Datei-Upload
uploaded_file = st.file_uploader("Wähle eine Datei zum Hochladen", type=None)

if uploaded_file:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Datei '{uploaded_file.name}' wurde erfolgreich hochgeladen.")

st.markdown("---")
st.subheader("📁 Verfügbare Dateien zum Herunterladen")

files = os.listdir(UPLOAD_FOLDER)

if files:
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file)
        with open(file_path, "rb") as f:
            st.download_button(
                label=f"⬇️ {file}",
                data=f,
                file_name=file,
                mime="application/octet-stream"
            )
else:
    st.info("Noch keine Dateien hochgeladen.")
