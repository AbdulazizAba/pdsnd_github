import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['all','january','february', 'march', 'april', 'may', 'june']
days = ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
      city=str(input("\n Please specify a city to start from the following list (Chicago, New York City, Washington) \n"))
      if city.lower() in cities:
        break
      else:
        print("Wrong Entry!. Please Try Again")
        continue
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month=str(input("\n Please specify a month during January - June ,or type all for the whole period\n"))
      if month.lower() in months:
        break
      else:
        print("Wrong Entry!. Please Try Again")
        continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day=str(input(" \n Please specify a day of the week or type all for all days \n"))
      if day.lower() in days:
        break
      else:
        print("Wrong Entry!. Please Try Again!")
        continue

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
# loading data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

# converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

# filter by month if applicable
    if month != 'all':
        # useing the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_travel_month = df['month'].mode()
    print('Most Common Month:', popular_travel_month)

    # TO DO: display the most common day of week
    popular_travel_day = df['day_of_week'].mode()
    print('Most Common Day of week:', popular_travel_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_travel_hour = df['hour'].mode()
    print('Most Common Start Hour:', popular_travel_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Popular_Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Popular start station:', Popular_Start_Station)

    # TO DO: display most commonly used end station
    Popular_End_Station = df['End Station'].value_counts().idxmax()
    print('Most Popular end station:', Popular_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip']=df['Start Station']+'-'+df['End Station']
    Trip = df['Trip'].value_counts().idxmax()
    print('Most Popular trip:', Trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total Travel Time (Seconds):', Total_Travel_Time)

    # TO DO: display mean travel time
    Average_Travel_Time = df['Trip Duration'].mean()
    print('Average Travel Time (Seconds):', Average_Travel_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Types = df['User Type'].value_counts()
    print('User Type Count:', User_Types)

    # TO DO: Display counts of gender
    try:
        Gender = df['Gender'].value_counts()
        print('Gender Count:', Gender)
    except KeyError:
        print("\nNo data available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Birthdate = int(df['Birth Year'].min())
        print('Earliest Birtdate:', Earliest_Birthdate)
    except KeyError:
        print("\nNo data available for this city.")
                
    try:
        Recent_Birthdate = int(df['Birth Year'].max())
        print('Most Recent Birtdate:', Recent_Birthdate)                              
    except KeyError:
        print("\nNo data available for this city.")
                
    try:
        Common_Birthdate = int(df['Birth Year'].mode())
        print('Most Common Birtdate:', Common_Birthdate)               
    except KeyError:
        print("\nNo data available for this city.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x=5
    while True:
        raw_data=input('\n Would you like to view individual trip data (5 rows a time)? Type yes or no \n')
        if raw_data.lower() == 'yes':
            print(df.head(x))
            x=x+5
        else:
            break
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
