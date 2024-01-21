#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 21:07:37 2024

@author: prasanthnattey
"""

# app.py
import streamlit as st

st.title("Welcome to The Kerala Itinerary")
st.write("Hello, Wallo!")
import streamlit as st
from datetime import time
def main():
    st.title("Kochi Travel Plan")

    st.header("Day 1 Plan")
    hotel_checkin_time = st.time_input("Hotel Checkin Time", value=time(14, 30))
    st.markdown("By {}:{} Hotel Checkin Complete".format(hotel_checkin_time.hour, hotel_checkin_time.minute))

    fresh_time = st.time_input("Freshen up and Hair Wash Time", value=time(15, 0))
    st.markdown("{}-{} get fresh and Wallo’s hair wash at a salon".format(
        fresh_time.strftime("%H:%M"), (fresh_time.replace(minute=fresh_time.minute + 58)).strftime("%H:%M")))

    explore_time = st.time_input("Explore St. Francis Church Time", value=time(16, 0))
    st.markdown("{}-{} explore St. Francis Church, the oldest European church in India.".format(
        explore_time.strftime("%H:%M"), (explore_time.replace(minute=explore_time.minute + 58)).strftime("%H:%M")))

    beach_time = st.time_input("Explore Fort Kochi Beach Time", value=time(17, 0))
    st.markdown("5-8 around fort kochi beach and watch the fishing nets in action. Sunset at 6:20pm on 29th Jan")

    houseboat_option = st.checkbox("Check for Houseboats and Book for a Ride?")
    if houseboat_option:
        st.markdown("Will check for houseboats tomorrow and book for a ride, maybe dinner on the ride?")

        kathakali_option = st.checkbox("Check for 9pm Kathakali Performances?")
        if kathakali_option:
            st.markdown("Will check for 9pm Kathakali Performances somewhere.")

    else:
        kathakali_option = st.checkbox("Alternate: Book Kathakali Performance at 6-7pm?")
        if kathakali_option:
            st.markdown("Kathakali performance 6-7pm [Wallo reserved already]")
            st.markdown("Kerala cuisine dinner with local drinks from 7:30-8:30")

    st.markdown("Come back to hotel so that Wallo can make a video call at 9pm and tell she is sleeping")

    st.header("Day 2 Plan")
    sunrise_option = st.checkbox("Watch Sunrise?")
    if sunrise_option:
        st.markdown("Maybe watch Sunrise?")

    palace_time = st.time_input("Visit Mattancherry Palace Dutch Palace at", value=time(9, 0))
    st.markdown("9am: Mattancherry Palace Dutch Palace")

    jew_town_time = st.time_input("Roam around Jew Town and shop in the market at", value=time(10, 0))
    st.markdown("10am: Roam around Jew Town and shop in the market")

    munnar_time = st.time_input("Start to Munnar by", value=time(11, 0))
    st.markdown("by 11/11:30 start to Munnar")

if __name__ == "__main__":
    main()

