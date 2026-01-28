import sqlite3
import pandas as pd

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

query = """
    SELECT playerID,yearID,teamID,HR
    From batting
    WHERE yearID=1976 and teamID = 'PHI' and HR > 0
    ORDER BY HR desc
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records,columns=['playerID','yearID','teamID','HR'])
print(records_df)