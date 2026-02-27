from sqlmodel import SQLModel, Field, create_engine

class Champion(SQLModel, table=True):
    champion_name: str = Field(default=None, primary_key=True)
    tier_number: int = Field(default=None)
    role: str = Field(default=None)
    winrate: float = Field(default=None)
    pickrate: float = Field(default=None)

engine = create_engine('sqlite:///league.db')
SQLModel.metadata.create_all(engine)