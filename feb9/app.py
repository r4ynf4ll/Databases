import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT name, batting.yearID, batting.HR
    FROM batting inner join teams
    ON batting.teamID = teams.teamID AND batting.yearID = teams.yearID
    WHERE playerID = 'ruthba01'
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()
records_df = pd.DataFrame(records,columns = ['teamname','year','HR'])
print(records_df)