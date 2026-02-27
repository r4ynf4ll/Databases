from sqlmodel import Session
from models import engine
from players_init import generate_players_list

with Session(engine) as session:
    players = generate_players_list()
    session.add_all(players)
    session.commit()
