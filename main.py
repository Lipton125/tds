import os
import shutil
import uuid
import zipfile
import requests
import pandas as pd
from io import BytesIO
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_from_file(file: BytesIO, filename: str):
    """Extracts text from CSV, XLSX, TXT files from memory."""
    file_ext = filename.split(".")[-1].lower()
    
    if file_ext == "csv":
        df = pd.read_csv(file)
        return df.to_string()
    
    elif file_ext in ["xls", "xlsx"]:
        df = pd.read_excel(file)
        return df.to_string()
    
    elif file_ext == "txt":
        return file.read().decode("utf-8")
    
    return ""

@app.post("/api/")
async def ask_deepseek(question: str = Form(...), file: UploadFile = File(None)):
    extracted_text = ""

    if file:
        file_ext = file.filename.split(".")[-1].lower()
        file_content = await file.read()
        file_stream = BytesIO(file_content)

        # If ZIP file, extract contents
        if file_ext == "zip":
            with zipfile.ZipFile(file_stream, "r") as zip_ref:
                for extracted_file_name in zip_ref.namelist():
                    with zip_ref.open(extracted_file_name) as extracted_file:
                        extracted_text += extract_text_from_file(BytesIO(extracted_file.read()), extracted_file_name) + "\n"
        else:
            extracted_text = extract_text_from_file(file_stream, file.filename)
    
    # Construct the prompt
    prompt = f"Answer the question concisely and directly without explanations. Just provide the final answer.\n\nQuestion: {question}"
    if extracted_text:
        prompt += f"\n\nHere is the relevant data:\n{extracted_text[:5000]}"  # Limit text to 5000 chars

    try:
        # Make API call to OpenRouter DeepSeek V3
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 1000
            }
        )
        response_data = response.json()
        
        if "choices" in response_data and response_data["choices"]:
            answer = response_data["choices"][0]["message"]["content"].strip()
            return JSONResponse(content={"answer": answer})
        else:
            return JSONResponse(content={"error": "No response from model"}, status_code=500)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
