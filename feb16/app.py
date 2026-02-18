import sqlite3
import pandas as pd
import gradio as gr

def playernames():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
    WITH top_hitters AS (SELECT nameFirst, nameLast, batting.playerID as playerID
    FROM batting inner join people
    ON batting.playerID = people.playerID
    WHERE teamID = 'PHI'
    GROUP BY batting.playerID
    ORDER BY sum(HR) desc
    LIMIT 10)

    SELECT CONCAT(nameFirst,' ', nameLast) as player, playerID
    FROM top_hitters
    ORDER BY nameLast asc
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return records

def f(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
    SELECT CAST(yearID AS text),HR
    FROM batting
    WHERE playerID = ?
    """
    cursor.execute(query,[player])
    records = cursor.fetchall()
    df = pd.DataFrame(records,columns=['yearID','HR'])
    conn.close()
    return df


with gr.Blocks() as iface:
    choices = gr.Dropdown(choices=playernames(),interactive=True)
    hrs = gr.LinePlot(
        x="yearID",
        y="HR",
        tooltip=['yearID', 'HR'],)
    choices.change(fn=f,inputs=[choices],outputs=hrs)

iface.launch()