from fastapi import APIRouter, HTTPException
from sqlmodel import select

from tts.db import SessionDep
from tts.routers.suites import router as suites_router
from tts.models.project import Project

router = APIRouter()
router.include_router(
    router=suites_router, prefix="/{project_id}/suites", tags=["projects, suites"]
)


@router.post("")
async def create_project(project: Project, session: SessionDep) -> Project:
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


@router.get("")
async def get_projects(session: SessionDep) -> list[Project]:
    return session.exec(select(Project).offset(0).limit(100)).all()


@router.get("/{project_id}")
async def get_project(project_id: str, session: SessionDep) -> Project:
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail=f"Project {project_id} not found.")
    return project
