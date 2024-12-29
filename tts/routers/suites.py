from fastapi import APIRouter

from tts.common_types import ProjectId
from tts.db import SessionDep
from tts.models.suite import Suite, SuiteCreate

router = APIRouter()


@router.post("")
async def create_suite(
    project_id: ProjectId, suite: SuiteCreate, session: SessionDep
) -> Suite:
    db_suite = Suite.model_validate(suite)
    session.add(db_suite)
    session.commit()
    session.refresh(db_suite)
    return db_suite


@router.get("")
async def get_suites() -> list[Suite]:
    pass
