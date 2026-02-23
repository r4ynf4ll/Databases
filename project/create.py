import pandas as pd

from sqlmodel import SQLModel, create_engine,Field

engine = create_engine("sqlite:///league.db")

df = pd.read_csv("LoL_champions.csv")

df.to_sql('champions', con=engine, if_exists='replace', index=False)

SQLModel.metadata.create_all(engine)

