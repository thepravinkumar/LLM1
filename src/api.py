from fastapi import FastAPI, HTTPException
import os
from src.tasks.format_text import format_text
from src.tasks.summarize_text import summarize_text

app = FastAPI()

@app.post("/run")
async def run_task(task: str, text: str = None):
    try:
        if task.lower() == "format":
            result = format_text(text)
        elif task.lower() == "summarize":
            result = summarize_text(text)
        else:
            raise ValueError("Unknown task.")
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
