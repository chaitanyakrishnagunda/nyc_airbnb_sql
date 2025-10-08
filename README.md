# 🧾 AI Expense Splitter (Work in Progress 🚧)

An **AI-powered Expense Splitting App** that extracts and understands information from receipt images using OCR and NLP.  
The system reads scanned or photographed receipts, parses text details (items, amounts, totals), and prepares structured data for fair bill splitting.

---

## 🧠 Overview

This project uses **Optical Character Recognition (OCR)** and **Natural Language Processing (NLP)** techniques to automate the process of splitting bills among users.

It begins by:
1. **Extracting text** from raw receipt images using EasyOCR.
2. **Preprocessing** receipts (cropping, thresholding, resizing).
3. **Parsing** the extracted text to identify key fields like:
   - Item names  
   - Individual prices  
   - Total amounts  
   - Taxes / Discounts  

Future versions will include NLP-driven understanding via **ChatGPT API** to handle natural language inputs like:
> “Alice paid for dinner and Bob owes half.”

---

## 🧰 Tech Stack

- **Python 3.x**
- **EasyOCR** – text extraction from images  
- **OpenCV** – image preprocessing  
- **Pandas / JSON** – structured data output  
- **ChatGPT API (Planned)** – NLP-based bill understanding  
- **Streamlit (Planned)** – user interface  
- **AWS RDS (Planned)** – data storage and retrieval  

---

## 📂 Project Structure
ai-bill-splitter/
├── data/
│ ├── raw_receipts/
│ └── cleaned_receipts/
├── notebooks/
│ └── easyocr_experiments.ipynb
├── src/
│ ├── ocr_extraction.py
│ ├── preprocess_receipts.py
│ └── parse_extracted_data.py
├── outputs/
│ └── extracted_text.txt
└── README.md


---

## 🚀 Current Progress

- [x] OCR working with EasyOCR  
- [x] Image preprocessing (cropping, resizing, thresholding)  
- [x] JSON-based structured text output  
- [ ] NLP-based parsing with ChatGPT  
- [ ] Streamlit front-end for user interaction  
- [ ] Cloud deployment and database storage  

---

## 🧩 Next Steps

1. Integrate **ChatGPT API** for text-to-structure parsing.  
2. Build **Streamlit UI** for user uploads and results.  
3. Add **bill-splitting logic** using GPT and rule-based automation.  
4. Store processed receipts and metadata in **AWS RDS**.  

---

> ⚠️ Full dataset excluded due to size limitations.  
> To access the complete dataset, please contact the author or use your own receipts for testing.

## 🧑‍💻 Author

**Chaitanya Krishna Gunda**  
M.S. in Data Science, Stevens Institute of Technology  
Passionate about AI, NLP, and intelligent data systems.

---

## 🏗️ Status

This project is actively under development.  
Updates and improvements will be added progressively as modules evolve. Stay tuned! 🚧

