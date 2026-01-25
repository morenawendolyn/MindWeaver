








































"""
FastAPI routes for interacting with MindWeaver system.
Allows triggering code improvement tasks and querying results.
"""

from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from ..scheduler import TaskScheduler
from ..runner import RefactorRunner

router = APIRouter(prefix="/api", tags=["mindweaver"])

scheduler = TaskScheduler()
runner = RefactorRunner(scheduler=scheduler)

class RefactorRequest(BaseModel):
    file_path: str

@router.post("/refactor")
async def trigger_refactor(req: RefactorRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(runner.run_task, req.file_path)
    return {"status": "queued", "file": req.file_path}

@router.get("/status")
async def get_status():
    return scheduler.get_status()
