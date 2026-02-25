from sqlmodel import Field, SQLModel

class Player(SQLModel, table=True):
	Position: str
	Weight: int
	Height: str
	Hometown: str
	Class: str
	High_School: str
	Number: int = Field(primary_key=True)
	First_Name: str
	Last_Name: str

class Stats(SQLModel, table=True):
	Number: int = Field(primary_key=True, foreign_key="player.Number")
	First_Name: str
	Last_Name: str | None = None
	GP: int
	G: int
	A: int
	PTS: int
	SH: int
	SH_PCT: float
	Plus_Minus: int
	PPG: int
	SHG: int
	FG: int
	GWG: int
	GTG: int
	OTG: int
	HTG: int
	UAG: int
	PN_PIM: str
	MIN: int
	MAJ: int
	OTH: int
	BLK: int
