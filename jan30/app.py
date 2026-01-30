import sqlite3
import gradio as gr

def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
    SELECT playerID
    FROM batting
    WHERE teamID = 'PHI' and yearID = 1976
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    players = []
    for record in records:
        id = players.append(record[0])
    return players

def f(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query="""
    SELECT HR
    FROM batting
    WHERE playerID=? and yearID=1976 and teamID='PHI'
    """
    cursor.execute(query,[player])
    records = cursor.fetchall()
    conn.close()
    return records[0][0]

iface = gr.Interface(fn=f,inputs=gr.Dropdown(choices=fetch_phillies()),outputs="number")
iface.launch()