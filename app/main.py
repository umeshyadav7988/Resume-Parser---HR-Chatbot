from fastapi import FastAPI, UploadFile, File
from .services import parse_resume, candidate_database, chatbot_query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    content_text = content.decode("utf-8")
    candidate = parse_resume(content_text)
    candidate_database.append(candidate)
    return {"message": "Resume parsed and added!", "candidate": candidate}

@app.post("/ask_chatbot/")
async def ask_chatbot(question: str):
    answer = chatbot_query(question)
    return JSONResponse(content={"answer": answer})
@app.get("/")
def read_root():
    return {"message": "Welcome to Resume Parser API! Use /upload_resume/ and /ask_chatbot/"}
