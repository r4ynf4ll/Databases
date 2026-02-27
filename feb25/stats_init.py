import csv
from pathlib import Path

from models import Stats


def generate_stats_list(csv_path: str | Path | None = None) -> list[Stats]:
	if csv_path is None:
		csv_path = Path(__file__).with_name("stats.csv")
	else:
		csv_path = Path(csv_path)

	players_csv_path = Path(__file__).with_name("players.csv")
	roster_by_number: dict[int, tuple[str, str]] = {}
	with players_csv_path.open(newline="", encoding="utf-8") as players_csv_file:
		players_reader = csv.DictReader(players_csv_file)
		for row in players_reader:
			number_raw = row["Number"].strip()
			if number_raw.isdigit():
				roster_by_number[int(number_raw)] = (row["First Name"], row["Last Name"])

	stats_by_number: dict[int, Stats] = {}
	with csv_path.open(newline="", encoding="utf-8") as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			number_raw = row["Number"].strip()
			if not number_raw.isdigit():
				continue
			number = int(number_raw)

			last_name = row["Last_Name"].strip()
			first_name = row["First_Name"]
			if number in roster_by_number:
				first_name, last_name = roster_by_number[number]

			stats_by_number[number] = Stats(
					Number=number,
					First_Name=first_name,
					Last_Name=last_name if last_name else None,
					GP=int(row["GP"]),
					G=int(row["G"]),
					A=int(row["A"]),
					PTS=int(row["PTS"]),
					SH=int(row["SH"]),
					SH_PCT=float(row["SH_PCT"]),
					Plus_Minus=int(row["Plus_Minus"]),
					PPG=int(row["PPG"]),
					SHG=int(row["SHG"]),
					FG=int(row["FG"]),
					GWG=int(row["GWG"]),
					GTG=int(row["GTG"]),
					OTG=int(row["OTG"]),
					HTG=int(row["HTG"]),
					UAG=int(row["UAG"]),
					PN_PIM=row["PN-PIM"],
					MIN=int(row["MIN"]),
					MAJ=int(row["MAJ"]),
					OTH=int(row["OTH"]),
					BLK=int(row["BLK"]),
				)

	for number, (first_name, last_name) in roster_by_number.items():
		if number not in stats_by_number:
			stats_by_number[number] = Stats(
				Number=number,
				First_Name=first_name,
				Last_Name=last_name,
				GP=0,
				G=0,
				A=0,
				PTS=0,
				SH=0,
				SH_PCT=0.0,
				Plus_Minus=0,
				PPG=0,
				SHG=0,
				FG=0,
				GWG=0,
				GTG=0,
				OTG=0,
				HTG=0,
				UAG=0,
				PN_PIM="0-0",
				MIN=0,
				MAJ=0,
				OTH=0,
				BLK=0,
			)

	return [stats_by_number[number] for number in sorted(stats_by_number)]
