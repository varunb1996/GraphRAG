from pypdf import PdfReader
from pathlib import Path
import json

# -----------------------------
# Storage for all documents
# -----------------------------
DATA = []

# -----------------------------
# PDF INGESTION
# -----------------------------
pdf_dir = Path("data/pdfs")

for pdf_file in pdf_dir.glob("*.pdf"):

    try:
        reader = PdfReader(str(pdf_file))

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        DATA.append({
            "source": str(pdf_file),
            "type": "pdf",
            "content": text
        })

        print(f"[PDF] Processed: {pdf_file}")

    except Exception as e:
        print(f"[PDF ERROR] {pdf_file} -> {e}")

# -----------------------------
# LANGCHAIN CODE INGESTION
# -----------------------------
repo_dir = Path("data/repos/langchain")

# Only useful RAG-related folders
TARGET_FOLDERS = [
    "chains",
    "retrievers",
    "vectorstores"
]

for folder in TARGET_FOLDERS:

    target_path = repo_dir / "libs" / "langchain" / "langchain" / folder

    # Skip if folder doesn't exist
    if not target_path.exists():
        print(f"[WARNING] Missing folder: {target_path}")
        continue

    for file in target_path.rglob("*.py"):

        try:
            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            DATA.append({
                "source": str(file),
                "type": "code",
                "content": content
            })

            print(f"[CODE] Processed: {file}")

        except Exception as e:
            print(f"[CODE ERROR] {file} -> {e}")

# -----------------------------
# CREATE OUTPUT DIRECTORY
# -----------------------------
processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)

# -----------------------------
# SAVE ALL DOCUMENTS
# -----------------------------
output_file = processed_dir / "documents.json"

with open(output_file, "w", encoding="utf-8") as f:

    json.dump(DATA, f, indent=2, ensure_ascii=False)

# -----------------------------
# FINAL SUMMARY
# -----------------------------
print("\n===================================")
print(f"Total documents processed: {len(DATA)}")
print(f"Saved to: {output_file}")
print("===================================")