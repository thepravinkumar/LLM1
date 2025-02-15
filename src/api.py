from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from src.tasks.format_text import format_text
from src.tasks.summarize_text import summarize_text

app = FastAPI()

class TaskRequest(BaseModel):
    text: str

@app.post("/run")
async def run_task(task: str, request: TaskRequest):
    try:
        text = request.text.strip()  # Ensure text is not None before calling strip()
        
        if task.lower() == "format":
            result = format_text(text)
        elif task.lower() == "summarize":
            result = summarize_text(text)
        else:
            raise HTTPException(status_code=400, detail="Unknown task.")
        
        return {"status": "success", "result": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
