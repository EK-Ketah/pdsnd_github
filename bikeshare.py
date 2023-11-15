import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        selected_city = input('Enter city name (chicago, new york city, washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please enter a valid city name.')

    while True:
        selected_month = input('Enter month (all, january, february, ..., june): ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid input. Please enter a valid month.')

    while True:
        selected_day = input('Enter day of the week (all, monday, tuesday, ..., sunday): ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid input. Please enter a valid day of the week.')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
 """
    Load bikeshare data for the specified city, month, and day.

    Args:
        city (str): Name of the city (e.g., 'chicago', 'new york city', 'washington')
        month (str): Name of the month (e.g., 'all', 'january', 'february')
        day (str): Name of the day (e.g., 'all', 'monday', 'tuesday')

    Returns:
        df (pd.DataFrame): Pandas DataFrame containing bikeshare data
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.day_name()

    month_mapping = {'all': 0, 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    month_num = month_mapping.get(month, 0)
    df = df[df['Month'] == month_num]

    if day != 'all':
        df = df[df['Day_of_Week'] == day.title()]

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['Month'].mode()[0]
    print(f'The most common month is: {common_month}')

    common_day = df['Day_of_Week'].mode()[0]
    print(f'The most common day of week is: {common_day}')

    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print(f'The most common start hour is: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is: {common_start_station}')

    common_end_station = df['End Station'].mode()[0]
    print(f'The most commonly used end station is: {common_end_station}')

    df['Start_End_Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Start_End_Combination'].mode()[0]
    print(f'The most frequent combination of start station and end station trip is: {common_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print(f'The total travel time is: {total_travel_time} seconds')

    mean_travel_time = df['Trip Duration'].mean()
    print(f'The mean travel time is: {mean_travel_time} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('Counts of each user type:')
    print(user_types)

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of each gender:')
        print(gender_counts)
    else:
        print('\nGender information not available for this dataset.')

    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
