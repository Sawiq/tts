from sqlmodel import Field, SQLModel

from tts.common_types import UUID, Description, Name


class SuiteBase(SQLModel):
    parentId: UUID | None = Field(default=None, foreign_key="suite.id")
    name: Name
    description: Description


class SuiteCreate(SuiteBase):
    pass


class Suite(SuiteBase, table=True):
    id: UUID
