import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'no']
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'no']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to        handle invalid inputs
    city = input("\nEnter City Name: \n").lower().strip()
    while city not in cities:
        city = input("\nPlease, Enter Chicago or New York City or Washington:\n").lower().strip()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nChoose a month from January to June to filter for or choose no for no filter: \n").lower().strip()
    while month not in months:
        month = input("\nPlease, Enter a Valid Option:\n").lower().strip()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nChoose a day to filter for or choose no for no filter: \n").lower().strip()
    while day not in days:
        day = input("\nPlease, Enter a Valid Option:\n").lower().strip()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'no':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'no':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    popular_month_name = calendar.month_name[popular_month]
    print('The most common month:', popular_month_name)
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week:', popular_day_of_week)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    frequent_start_station =df.groupby(['Start Station']).size().nlargest(1)
    print('Most frequent start station: ', frequent_start_station)

    # TO DO: display most commonly used end station
    frequent_end_station = df.groupby(['End Station']).size().nlargest(1)
    print('Most frequent end station: ', frequent_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('Most frequent start and end station: ', frequent_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_seconds = df['Trip Duration'].sum()
    travel_time_hours = travel_time_seconds // 3600
    travel_time_minutes = travel_time_seconds // 60
    print('Total Travel Time: ', travel_time_hours, 'Hours' ,travel_time_minutes, 'Minutes' ,travel_time_seconds,'Seconds')
    # TO DO: display mean travel time
    travel_time_seconds = df['Trip Duration'].mean()
    travel_time_hours = travel_time_seconds // 3600
    travel_time_minutes = travel_time_seconds // 60
    print('Mean Travel Time: ', travel_time_hours, 'Hours' ,travel_time_minutes, 'Minutes' ,travel_time_seconds,'Seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        user_types = df['Gender'].value_counts()
        print(user_types)
    except:
        print ('No Gender Data is provided')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        max_birth_year = df['Birth Year'].max()
        min_birth_year = df['Birth Year'].min()
        mode_birth_year = df['Birth Year'].mode()[0]
        print('The Earliest Birth Year: ', max_birth_year)
        print('The Most Recent Birth Year: ', min_birth_year)
        print('The Most Common Birth Year: ', mode_birth_year)
    except:
        print ('No Gender Data is provided')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print('\nDisplaying Data Sample\n')
    start_time = time.time()
    rows_count = 5
    row = df.sample(n = rows_count)
    print(row)
    answer_yes = 'y'
    answer_no = 'n'

    while True:
        another_sample = input("\nWould you like to view another sample of data Y or N:\n").lower().strip()
        if another_sample == answer_yes:
            rows_count = 5
            row = df.sample(n = rows_count)
            print(row)

        elif another_sample == answer_no:
            break
        else:
            print('Enter a valid answer')

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
