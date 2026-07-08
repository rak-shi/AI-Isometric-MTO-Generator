from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

from app.pipeline.gemini_pipeline import extract_mto
from app.utils.pdf_converter import pdf_to_image
from app.utils.image_utils import enhance_image
from app.utils.csv_exporter import create_csv


router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Store latest generated MTO
latest_result = None


# ============================
# Upload + Extract MTO API
# ============================

@router.post("/extract")
async def extract(file: UploadFile = File(...)):

    global latest_result

    # Save uploaded file
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )


    # Convert PDF to Image
    if file.filename.lower().endswith(".pdf"):
        image_path = pdf_to_image(file_path)

    else:
        image_path = file_path


    # Enhance image
    image_path = enhance_image(
        image_path
    )


    # Gemini AI Extraction
    result = extract_mto(
        image_path
    )


    # Save latest result for CSV
    latest_result = result


    return result



# ============================
# CSV Download API
# ============================

@router.get("/mto/csv")
def download_csv():

    if latest_result is None:

        return {
            "error": "Generate MTO first"
        }


    csv_path = create_csv(
        latest_result["items"]
    )


    return FileResponse(
        path=csv_path,
        filename="mto.csv",
        media_type="text/csv"
    )