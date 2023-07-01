# импортируем библиотеку streamlit
import streamlit as st
from PIL import Image
import pandas as pd
from model import load_model_and_predict

def write_prediction(prediction, prediction_probas):
    st.write("## Предсказание")
    st.write(prediction)

    st.write("## Вероятность предсказания")
    st.write(prediction_probas)


def process_inputs():
    user_input_df = input_features()

    prediction, prediction_probas = load_model_and_predict(user_input_df)
    write_prediction(prediction, prediction_probas)

def input_features():

    translation = {
        "М": 1,
        "Ж": 0,
        "Да": 0,
        "Нет": 1,
        "Рабочая поездка": 0,
        "Поездка по своим делам": 1,
    }

    class_eco =  class_category == "Эко"   
    class_ecop = class_category == "Эко+"

    age_scaled = ((age - 7) /93) * (100 - 7) + 7
    dist_scaled = ((distance - 31) / (8326 - 31)) * (8326 - 31) + 31
    time_scaled = ((time_convenient - 1) / 4) * (5 - 1) + 1
    booking_scaled = ((booking_convenient - 1) / 4)* (5 - 1) + 1
    gate_scaled = ((gate_convenient - 1) / 4)* (5 - 1) + 1
    boarding_scaled = ((boarding_convenient - 1) / 4)* (5 - 1) + 1
    checkin_scaled = ((checkin_convenient - 1) / 4)* (5 - 1) + 1

    data = {'Gender_Male': translation[gender],
       'Age' : age_scaled,
       'Customer Type_disloyal Customer' : translation[client_type], 
       'Type of Travel_Personal Travel' : translation[travel_type], 
       'Class_Eco' : class_eco,
       'Class_Eco Plus' : class_ecop,
       'Flight Distance' : dist_scaled,
       'Departure/Arrival time convenient' : time_scaled, 
       'Ease of Online booking' : booking_scaled,
       'Gate location' : gate_scaled,
       'Online boarding' : boarding_scaled,
       'Checkin service' : checkin_scaled
    }

    df = pd.DataFrame(data, index=[0])

    return df


img = Image.open("plane.png")
st.set_page_config(
    page_title="Облачный оракул",
    page_icon=img)
st.image(img)

st.write("## Облачный оракул")
st.text("подскажет Вам, будете ли Вы довольны полётом - до того, как он случится!")
st.subheader('Ваши пассажирские данные:')
#input_features()
gender = st.selectbox(
'Пол',
('Ж','М'))
age = st.slider('Возраст', 7, 100, 1)
client_type = st.selectbox(
'Вы постоянный клиент авиакомпании?',
('Да', 'Нет'))

st.subheader('Данные о полёте:')
travel_type = st.selectbox(
'Цель путешествия',
('Рабочая поездка', 'Поездка по своим делам'))
class_category = st.selectbox(
'Класс поездки',
('Бизнес','Эко', 'Эко+'))
distance = st.slider('Дистанция перелета, в милях', 31, 9500, 10)

st.subheader('Ваше текущее мнение о деталях полёта:')
time_convenient = st.select_slider(
'Удобство времени вылета\прилёта',
options=[1,2,3,4,5])
booking_convenient = st.select_slider(
'Удобство онлайн бронирования',
options=[1,2,3,4,5])
gate_convenient = st.select_slider(
'Удобство расположения выхода на посадку',
options=[1,2,3,4,5])
boarding_convenient = st.select_slider(
'Удобство онлайн выбора места',
options=[1,2,3,4,5])
checkin_convenient = st.select_slider(
'Удобство онлайн регистрации на рейс',
options=[1,2,3,4,5])
if st.button('Предсказать удовлетворённость полётом'):
    process_inputs()
else:
    st.write('Как же пройдёт полёт?...')
    
if __name__ == "__main__":
    print('')