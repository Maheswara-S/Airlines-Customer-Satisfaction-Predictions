import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('pipe.pkl','rb'))

st.header('Airlines User Satisfaction Prediction')

inflight_entertainment = st.selectbox('Inflight Entertinement',['0','1','2','3','4','5'])
if inflight_entertainment == '0':
    inflight_entertainment =0
elif inflight_entertainment == '1':
    inflight_entertainment =1
elif inflight_entertainment == '2':
    inflight_entertainment =2
elif inflight_entertainment == '3':
    inflight_entertainment =3
elif inflight_entertainment == '4':
    inflight_entertainment =4
elif inflight_entertainment == '5':
    inflight_entertainment =5

online_support = st.selectbox('Online Support',['0','1','2','3','4','5'])
if online_support == '0':
    online_support =0
elif online_support == '1':
    online_support =1
elif online_support == '2':
    online_support =2
elif online_support == '3':
    online_support =3
elif online_support == '4':
    online_support =4
elif online_support == '5':
    online_support =5

ease_of_online_booking = st.selectbox('Ease of Online Booking',['0','1','2','3','4','5'])
if ease_of_online_booking == '0':
    ease_of_online_booking =0
elif ease_of_online_booking == '1':
    ease_of_online_booking =1
elif ease_of_online_booking == '2':
    ease_of_online_booking =2
elif ease_of_online_booking == '3':
    ease_of_online_booking =3
elif ease_of_online_booking == '4':
    ease_of_online_booking =4
elif ease_of_online_booking == '5':
    ease_of_online_booking =5

onboard_service = st.selectbox('Onboard Service',['0','1','2','3','4','5'])
if onboard_service == '0':
    onboard_service =0
elif onboard_service == '1':
    onboard_service =1
elif onboard_service == '2':
    onboard_service =2
elif onboard_service == '3':
    onboard_service =3
elif onboard_service == '4':
    onboard_service =4
elif onboard_service == '5':
    onboard_service =5

leg_room_service = st.selectbox('Leg Room Service',['0','1','2','3','4','5'])
if leg_room_service == '0':
    leg_room_service =0
elif leg_room_service == '1':
    leg_room_service =1
elif leg_room_service == '2':
    leg_room_service =2
elif leg_room_service == '3':
    leg_room_service =3
elif leg_room_service == '4':
    leg_room_service =4
elif leg_room_service == '5':
    leg_room_service =5

online_boarding = st.selectbox('Online Boarding',['0','1','2','3','4','5'])
if online_boarding == '0':
    online_boarding =0
elif online_boarding == '1':
    online_boarding =1
elif online_boarding == '2':
    online_boarding =2
elif online_boarding == '3':
    online_boarding =3
elif online_boarding == '4':
    online_boarding =4
elif online_boarding == '5':
    online_boarding =5


if st.button('Submit'):

    X = pd.DataFrame([[inflight_entertainment,online_support,ease_of_online_booking,onboard_service,leg_room_service,online_boarding]],
                       columns=['Inflight Entertainment','Online Support','Ease of Online Booking','On Board Service','Leg Room Service','Online Booking'])
                       
    pred = model.predict(X)

    if pred[0] == 0:
        sat = 'Dissatisfied'
    else:
        sat = 'Satisfied'

    st.text(f'User are {sat}')