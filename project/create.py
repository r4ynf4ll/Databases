import pandas as pd

from sqlmodel import SQLModel, create_engine,Field

engine = create_engine("sqlite:///league.db")

df = pd.read_csv("champs.csv")

df.to_sql('champion_desc', con=engine, if_exists='replace', index=False)

SQLModel.metadata.create_all(engine)



