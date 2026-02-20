from sqlmodel import SQLModel, create_engine,Field

class Champion(SQLModel, table=True):
    id: int | None = Field(default = None, primary_key = True)
    name: str
    tag1: str
    tag2: str | None = None
    roles: str
    resource: str

engine = create_engine("sqlite:///league.db")

SQLModel.metadata.create_all(engine)

