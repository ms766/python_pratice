#!/usr/bin/env python3
import sqlite3
import json
from pathlib import Path


movies = json.loads(
    Path("/Users/ms/Desktop/pythonPrac/sql/movies.json").read_text())

print(movies)
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO MOVIES VALUES(?,?,?)"
#     for movie in movies:
#         conn.execute(command, tuple(move.values()))
#     conn.commit()
