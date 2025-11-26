from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
from typing import Optional, List
import requests
from utils.pdf import generate_pdf
from markdown import markdown
import re
from fpdf import FPDF
from io import BytesIO
# Hugging Face Setup
HUGGINGFACE_API_KEY = "enter the key"
HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"
app = FastAPI()

# Middleware
app.add_middleware(SessionMiddleware, secret_key="a8b2c9d9e3f4g5h6i7j8k9l0m1n2o3p4")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Mount static and templates
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic Model
class RecipeRequest(BaseModel):
    query: str
    diet_preference: Optional[str] = None
    cuisine_type: Optional[str] = None

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.get("/shopping", response_class=HTMLResponse)
async def shopping(request: Request):
    items = request.session.get("shopping_list", [])
    return templates.TemplateResponse("shopping.html", {"request": request, "items": items})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/accessories", response_class=HTMLResponse)
async def accessories(request: Request):
    return templates.TemplateResponse("accessories.html", {"request": request})

@app.get("/seasonal", response_class=HTMLResponse)
async def seasonal(request: Request):
    return templates.TemplateResponse("seasonal.html", {"request": request})
@app.get("/api/check-hf-key")
def check_hf_key():
    return {"key_set": HUGGINGFACE_API_KEY != "enter the key"}


# Hugging Face Recipe Generator
@app.post("/api/recipe")
async def generate_recipe(req: RecipeRequest):
    if HUGGINGFACE_API_KEY == "enter the key" or not HUGGINGFACE_API_KEY:
        return {"error": "❌ API Key missing. Please set HUGGINGFACE_API_KEY in main.py"}
    prompt = f"""
You are a master chef AI. Generate a detailed recipe for "{req.query}".
Include:
- Title
- Ingredients
- Instructions
- Tips
Format it in clean markdown style.
"""

    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{HF_MODEL}",
        headers=headers,
        json=payload
    )
    result = response.json()

    if isinstance(result, list) and "generated_text" in result[0]:
        markdown_text = result[0]["generated_text"]

        def extract_section(header, text):
            match = re.search(rf"(?i){header}[\s]*[:\-]*\n(.*?)(?=\n[A-Z]|$)", text, re.DOTALL)
            return match.group(1).strip() if match else ""

        title = req.query.title() + " Recipe"
        ingredients_raw = extract_section("Ingredients", markdown_text)
        instructions = extract_section("Instructions", markdown_text)
        tips = extract_section("Tips", markdown_text)

        ingredients = [re.sub(r"^[\-\•\*\s]*", "", line.strip()) for line in ingredients_raw.split("\n") if line.strip()]



        return {
            "title": title,
            "ingredients": ingredients,
            "instructions": instructions,
            "tips": tips
        }

    return {"error": "❌ Error generating recipe. Try again later."}

# Save shopping list to session
@app.post("/api/save-shopping")
async def save_shopping(request: Request, items: List[str] = Form(...)):
    request.session["shopping_list"] = items
    return JSONResponse(content={"message": "Shopping list saved."})


# PDF Generation
@app.post("/api/download-pdf")
def download_pdf_endpoint(title: str = Form(...), ingredients: str = Form(...), instructions: str = Form(...)):
    # Convert ingredients string back to list if needed, or handle as string
    # Assuming ingredients comes as a comma-separated string or similar from form
    # But looking at the frontend, it might be sending individual fields.
    # Let's check how the frontend sends it. 
    # Wait, the previous code expected `ingredients: list` but `Form(...)` usually sends strings unless repeated.
    # Let's assume for now we receive them as is.
    
    # Actually, looking at the previous code: `def generate_pdf(title: str, ingredients: list, instructions: str):`
    # The endpoint was defined as: `def generate_pdf(title: str, ingredients: list, instructions: str):`
    # This implies FastAPI was handling the list conversion if sent as `ingredients` multiple times.
    
    # Let's stick to the signature but use the imported function.
    
    # We need to parse ingredients if they come as a single string, or handle list.
    # For safety, let's accept list.
    
    ingredients_list = ingredients.split(",") if isinstance(ingredients, str) else ingredients
    
    pdf_buffer = generate_pdf(title, ingredients_list, instructions)
    
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={title.replace(' ', '_')}.pdf"}
    )
