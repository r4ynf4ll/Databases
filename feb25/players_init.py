import csv
from pathlib import Path

from models import Player


def generate_players_list(csv_path: str | Path | None = None) -> list[Player]:
	if csv_path is None:
		csv_path = Path(__file__).with_name("players.csv")
	else:
		csv_path = Path(csv_path)

	players: list[Player] = []
	with csv_path.open(newline="", encoding="utf-8") as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			players.append(
				Player(
					Position=row["Position"],
					Weight=int(row["Weight"]),
					Height=row["Height"],
					Hometown=row["Hometown"],
					Class=row["Class"],
					High_School=row["High School"],
					Number=int(row["Number"]),
					First_Name=row["First Name"],
					Last_Name=row["Last Name"],
				)
			)

	return players