from typing import Annotated
from uuid import uuid4

from pydantic import UUID4
from sqlmodel import Field

ProjectId = Annotated[str, Field(max_length=64, primary_key=True)]
UUID = Annotated[UUID4, Field(default_factory=uuid4, primary_key=True)]
Name = Annotated[str, Field(min_length=1, max_length=128)]
Description = Annotated[str, Field(min_length=1, max_length=2048)]
