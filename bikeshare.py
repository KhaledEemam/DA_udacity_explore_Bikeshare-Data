import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New york city': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city =check_input('Would you like to see data for Chicago, New york city or Washington', 1)
    while True :
        filter = input("Do you want to filter data by 'month','day', 'both' or 'No filter' at all ? ").lower()
        if filter == 'month' :
            month = check_input('Which month? January, February , March , April , May or June?', 2)
            day = 'all'
            break
        elif filter == 'day' :
            day = check_input('Which day? (Sunday,Monday, ...).', 3)
            month = 'all'
            break
        elif filter == 'both' :
            month = check_input('Which month? January, February , March , April , May or June?', 2)
            day = check_input('Which day? Please type response as an integer (e.g., Sunday,Monday...,all).', 3)
            break
        elif filter == 'no filter':
            month = 'all'
            day = 'all'
            break
        else :
            print("You entered an invalid filter, please provide a right one.")
            continue


    print('-' * 40)
    return city, month, day

def check_input(input_question,input_index) :

    while True :
        user_input = input(input_question).lower()
        try :
            if input_index == 1 and user_input not in ['chicago','new york city','washington'] :
                 print("Invalid city input , Please try again")
            elif input_index == 2 and  user_input not in ["january", "february", "march", "april", "may", "june"] :
                print("Invalid day input , Please try again")
            elif input_index == 3 and user_input not in [ 'monday','tuesday','wednesday','thursday','friday','saturday','sunday' ] :
                print("Invalid day input , Please try again")
            else :
                 break
        except ValueError :
            print("Invalid input , Please try again later")
    return user_input.title()



def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['month'] = df['Start Time'].dt.month
    df['day'] =  df["Start Time"].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all' :
        months = ["January", "February", "March", "April", "May", "June"]
        month_index = (months.index(month)) + 1
        df = df[df['month'] == month_index]
    if day != 'all' :
        df = df[df['day'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    most_commmon_month =df['month'].mode()[0]
    most_commmon_day = df['day'].mode()[0]
    most_commmon_hour = df['hour'].mode()[0]
    # display the most common month
    print('The most common month is {}'.format(most_commmon_month) )
    # display the most common day of week
    print('The most common day is {}'.format(most_commmon_day))
    # display the most common start hour
    print('The most common hour is {}'.format(most_commmon_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    most_commonly_start_station = df['Start Station'].mode()[0]
    most_commonly_end_station = df['End Station'].mode()[0]
    # display most commonly used start station
    print('The  most commonly used start station is {}'.format(most_commonly_start_station))
    # display most commonly used end station
    print('The  most commonly used end station is {}'.format(most_commonly_end_station))
    # display most frequent combination of start station and end station trip
    df['Trips'] = df['Start Station']+' to '+df['End Station']
    most_common_trip = df['Trips'].mode()[0]
    print('The most common trip is from {}'.format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time = {}'.format(total_travel_time))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time = {}'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Stats : ')
    print(df['User Type'].value_counts())
    if city == 'Washington' :
        print("Gender & birth year data aren't available in washington city")
    else :
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth, most_recent_year_of_birth, most_common_year_of_birth = \
            df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0]
        print('earliest, most recent, and most common year of birth are {},{} and {}'.format(
            earliest_year_of_birth, most_recent_year_of_birth, most_common_year_of_birth


    ))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def show_rows_data(df):
     i = 0
     while True :
         user_response = input("Would you like to show some users data ? 'Yes' or 'No' ").lower()
         if user_response == 'no' :
            break
         elif user_response == 'yes' :
             print(df[i:i+5])
             i += 5
         else :
             print("Please reply only with 'Yes' or 'No'")
             continue





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_rows_data(df)

        restart = input('Would you like to restart? Enter yes or no.')
        if restart.lower() != 'yes':
         break

if __name__ == "__main__":
        main()