from sqlmodel import SQLModel

from tts.common_types import Description, Name, ProjectId


class Project(SQLModel, table=True):
    id: ProjectId
    name: Name
    description: Description
