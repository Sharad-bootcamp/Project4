import streamlit as st
import pandas as pd
import pickle

# Declaring the teams and venues
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
         'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi', 'Chandigarh', 'Jaipur', 'Chennai',
          'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur',
          'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali', 'Bengaluru']

# Load the pre-trained model
pipe = pickle.load(open('pipe.pkl', 'rb'))




# Streamlit app title
st.title('IPL Win Predictor')

# User inputs for team, venue, target, score, overs, and wickets
col1, col2 = st.columns(2)

with col1:
    battingteam = st.selectbox('BATTING TEAM', sorted(teams))

with col2:
    bowlingteam = st.selectbox('BOWLING TEAM', sorted(teams))

city = st.selectbox('VENUE', sorted(cities))

target = int(st.number_input('Target', step=1))

col3, col4, col5 = st.columns(3)

with col3:
    score = int(st.number_input('Score', step=1))

with col4:
    overs = int(st.number_input('Overs Completed', step=1))

with col5:
    wickets = int(st.number_input('Wickets Fallen', step=1))

# Predictions and output display
if score > target:
    st.write(battingteam, "won the match")
elif score == target - 1 and overs == 20:
    st.write("Match Drawn")
elif wickets == 10 and score < target - 1:
    st.write(bowlingteam, 'Won the match')
elif battingteam == bowlingteam:
    st.write('To proceed, please select different teams as no match can be played between the same teams')
else:
    if 0 <= target <= 300 and 0 <= overs <= 20 and 0 <= wickets <= 10 and 0 <= score:
        try:
            if st.button('Predict Probability'):
                runs_left = target - score
                balls_left = 120 - (overs * 6)
                wickets_left = 10 - wickets
                currentrunrate = score / overs
                requiredrunrate = (runs_left * 6) / balls_left

                # Create the input DataFrame with the required columns
                input_df = pd.DataFrame({
                    'batting_team': [battingteam],
                    'bowling_team': [bowlingteam],
                    'city': [city],
                    'runs_left': [runs_left],
                    'balls_left': [balls_left],
                    'wickets_left': [wickets_left],  # Include 'wickets_left' in the input DataFrame
                    'total_runs_x': [target],
                    'cur_run_rate': [currentrunrate],
                    'req_run_rate': [requiredrunrate]
                })

                # Make predictions using the pre-trained pipeline
                result = pipe.predict_proba(input_df)
                lossprob = result[0][0]
                winprob = result[0][1]

                # Display predictions
                st.header(battingteam + " - " + str(round(winprob * 100)) + "%")
                st.header(bowlingteam + " - " + str(round(lossprob * 100)) + "%")

        except ZeroDivisionError:
            st.error("Please fill in all the required details")
    else:
        st.error('There is something wrong with the input, please fill in the correct details as of IPL T-20 format')
