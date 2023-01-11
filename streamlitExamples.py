import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import engine ,sess

engine=create_engine('sqlite:///project_db.sqlite3')
Session =sessionmaker(bind-engine)
sess-Session()