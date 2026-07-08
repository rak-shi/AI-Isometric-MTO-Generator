# AI Isometric MTO Generator

A full-stack AI-powered web application that extracts a Material Take-Off (MTO) from piping isometric drawings.

Users can upload an isometric drawing (PDF/Image), and the backend AI pipeline analyzes the drawing and generates structured MTO data with CSV export support.

---

## Features

- Upload piping isometric drawings (PDF/Image)
- Convert PDF drawings into images
- Image preprocessing before AI extraction
- AI-powered MTO generation using Gemini Vision
- Structured JSON output
- Material Take-Off table view
- CSV export functionality
- Mock mode support when API key is unavailable
- Full-stack implementation

---

## Tech Stack

### Frontend

- Next.js
- TypeScript
- React
- Axios
- Tailwind CSS

### Backend

- FastAPI
- Python
- Google Gemini API
- Pydantic
- Pandas
- pdf2image
- Pillow

---

## System Architecture

```text
                 User
                  |
                  |
          Next.js Frontend
                  |
                  |
        Upload PDF / Image
                  |
                  |
            FastAPI Backend
                  |
        ---------------------
        |                   |
 PDF to Image        Image Processing
        |                   |
        ---------------------
                  |
                  |
           Gemini Vision AI
                  |
                  |
          MTO JSON Extraction
                  |
        ---------------------
        |                   |
     MTO Table          CSV Export
```

---

## Project Structure

```text
AI-Isometric-MTO-Generator

│
├── backend
│   │
│   ├── app
│   │   │
│   │   ├── api
│   │   │   └── routes.py
│   │   │
│   │   ├── models
│   │   │   └── mto.py
│   │   │
│   │   ├── pipeline
│   │   │   └── gemini_pipeline.py
│   │   │
│   │   ├── utils
│   │   │   ├── pdf_converter.py
│   │   │   ├── image_utils.py
│   │   │   └── csv_exporter.py
│   │   │
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env.example
│
│
├── frontend
│   │
│   ├── app
│   │   └── page.tsx
│   │
│   ├── components
│   │   ├── UploadBox.tsx
│   │   └── MTOTable.tsx
│   │
│   ├── lib
│   │   └── api.ts
│   │
│   └── package.json
│
└── README.md
```

---

# Setup Instructions

## Backend Setup

Go to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment file:

```text
.env
```

Add:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

Backend starts:

```text
http://127.0.0.1:8000
```

Swagger API:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Go to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend runs:

```text
http://localhost:3000
```

---

# API Endpoints

## Extract MTO

```http
POST /api/extract
```

Input:

```text
PDF/Image file
```

Output:

```json
{
  "drawing_meta": {},
  "items": [],
  "summary": {}
}
```

---

## Download CSV

```http
GET /api/mto/csv
```

Downloads:

```text
mto.csv
```

---

# AI Pipeline

1. User uploads piping isometric drawing
2. Backend receives file
3. PDF is converted into image
4. Image enhancement is applied
5. Gemini Vision analyzes drawing
6. Structured MTO JSON is generated
7. Data displayed as table
8. CSV file generated for download

---

# Example MTO Fields

- Item Number
- Category
- Description
- Size
- Material Specification
- Quantity
- Unit
- Length
- Confidence Score
- Remarks

---

# Mock Mode

The application supports fallback mock MTO generation when:

- Gemini API key is unavailable
- API quota is exceeded
- AI service is temporarily unavailable

This ensures the application can always run end-to-end.

---

# Author

Rakshitha Valipireddy

GitHub:
https://github.com/rak-shi

---

# Status

Completed:
- Backend
- Frontend
- AI Extraction Pipeline
- CSV Export
- Full-stack Integration
