from sqlmodel import SQLModel,create_engine,Field

class Faculty(SQLModel,table = True):
    id: int | None = Field(default = None, primary_key = True)
    firstname: str
    lastname: str
    age: int | None = None

engine = create_engine("sqlite:///department.db")

SQLModel.metadata.create_all(engine)

