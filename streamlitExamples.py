import streamlit as st
from sqlalchemy.orm import sessionmaker
from project_orm import UserInput,Prediction
from sqlalchemy import create_engine
# from sqlalchemy import bind,sess

engine=create_engine('sqlite:///project_db.sqlite3')
Session =sessionmaker(bind=engine)
sess=Session()

st.title('I am Using Database with SqlAlchemy Here')
area =st.number_input('Enter house area in sqft',
max_value=10000,
min_value=100,
value=500
)

rooms =st.number_input('enter no of rooms',max_value=500,
min_value=0,
value=1)

age=st.number_input('age of house',
max_value=500,
min_value=0,
value=1)

location=st.text_area('Enter location address')
submit =st.button('make prediction')

if submit and location:
    try:
        entry =UserInput(house_area=area,
                    no_of_rooms=rooms,
                    age=age,
                     location=location)
        sess.add(entry)
        sess.commit()
        st.success("data added to Database")
    except Exception as e:
        st.error(f"some error occur  : {e} ")
    
