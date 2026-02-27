from sqlmodel import Session
from models import engine
from stats_init import generate_stats_list

with Session(engine) as session:
    stats = generate_stats_list()
    session.add_all(stats)
    session.commit()
