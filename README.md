# 📝 10k report automation system

This project is a **simplified automation pipeline** that converts Word + Excel source files into a basic **Inline XBRL (iXBRL)** 10-K report.

---

## 🚀 Features

* **Extract narrative text** from a Word document
* **Extract financial facts** (Revenues, Assets, Equity, etc.) from Excel
* Convert Word → **HTML**
* Insert **iXBRL tags** into the HTML:

  * `ix:nonNumeric` for document metadata (DocumentType, EntityRegistrantName)
  * `ix:nonFraction` for numeric values (Revenues, Assets, Liabilities…)
* Auto-generate:

  * **Duration context** (`FY2024`)
  * **Instant context** (`Instant2024`)
  * **USD currency unit** (`iso4217:USD`)
* Output a complete, machine-readable **iXBRL report**

---

## 📁 Project Structure

```
demo/
 ├── main.py               # Main pipeline controller
 ├── converters.py         # Reads Word/Excel inputs
 ├── tagging.py            # iXBRL tagging logic
 ├── metadata.py           # Builds ix:header (context, unit, schemaRef)
 ├── validation.py         # Basic numeric consistency checks
 ├── input/
 │    ├── sample_word.docx
 │    └── sample_excel.xlsx
 └── output/               # Generated ixbrl files
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install python-docx pandas openpyxl
```

### 2. Run the pipeline

```bash
python3 main.py
```

### 3. Find the generated iXBRL file

```
output/10k-report.html
```

Open it in a browser — you will see human-readable text with embedded machine-readable XBRL tags.
