from sqlmodel import SQLModel, create_engine,Field

class Champion(SQLModel, table=True)
    name: str
    tag1: str
    tag2: str | None = None
    roles: str
    resource: str



