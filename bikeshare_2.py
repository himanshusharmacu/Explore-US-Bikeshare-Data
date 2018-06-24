import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city to analyze.
    Returns:
        (str) city - name of the city to analyze
    """
    
    print('For which city would you like to analyze the data?\n Chicago, New York City, or Washington?')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #valid_cities = ['chicago','new york','washington']
    #while input_city not in valid_cities:
    
    input_city = input('\nEnter_City: ')
    #city is inputted here !
    
    if input_city.lower() == 'chicago':
        city = 'chicago'  #setting city to chicago
    elif input_city.lower() == 'new york city':
        city = 'new york city'   #setting city to new york city
    elif input_city.lower() == 'washington':
        city = 'washington'    #setting city to washington
    else:
        print('\nPlease Enter A Valid Input\n')
        return get_city()

    print('\nYou have chosen {}.\n'.format(city.title()))
    print('-'*40)
    
    return city

def get_month():
    """
    Asks user to specify a month to analyze.
    Returns:
    (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    
    # get user input for month (all, january, february, ... , june)
    
    print('Type the month you want to filter your data or just Type \'skip\' or \'00\' to skip month filtration !.')
    print(' \'Note:\' You can input using numeric values or abbreviations like months range from 01-12 or jan,feb,....!')
    
    input_month = input('Month: ')
    #month is inputted here !.
    
        # setting month variable to skip filtration
    if input_month.lower() in ['skip', '00']:
        month = 'all'
        # Setting  month to January
    elif input_month.lower() in ['january', 'jan', '01']:
        month = 'january'
        # Setting  month to February
    elif input_month.lower() in ['february', 'feb', '02']:
        month = 'february'
        # Setting  month to March
    elif input_month.lower() in ['march', 'mar', '03']:
        month = 'march'
        # Setting  month to April
    elif input_month.lower() in ['april', 'apr', '04']:
        month = 'april'
        # Setting  month to May
    elif input_month.lower() in ['may',  '05']:
        month = 'may'
        # Setting  month to June
    elif input_month.lower() in ['june', 'jun', '06']:
        month = 'june'
    else:
        print('\nPlease Enter A Valid Input\n')
        return get_month()

    # Printing message on screen
    if month == 'all':
        print('\nYou have chosen to show data for all months.\n')
    else:
        print('\nYou have chosen to show statistics for {}.\n'.format(month.title()))

    return month

def get_day():
    """
    Asks user to specify a  day to analyze.
    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # get user input for day of week_day
    
    print('Type the day you want to filter your data or just Type \'skip\' or \'00\' to skip week_day filtration !.')
    print(' \'Note:\' You can input using numeric values or abbreviations like week_days range from 01-07 or mon,tue,wed,....!')
    
    input_day = input('Week Day: ')
        
        # Setting day to skip filtration
    if input_day.lower() in ['skip','00']:
        day = 'all'
        # Setting day to Monday
    elif input_day.lower() in ['monday', 'mon', '01']:
        day = 'monday'
        # Setting day to Tuesday
    elif input_day.lower() in ['tuesday', 'tue', '02']:
        day = 'tuesday'
        # Setting day to Wednesday
    elif input_day.lower() in ['wednesday', 'wed', '03']:
        day = 'wednesday'
        # Setting day to Thursday
    elif input_day.lower() in ['thursday', 'thu', '04']:
        day = 'thursday'
        # Setting day to Friday
    elif input_day.lower() in ['friday', 'fri','05']:
        day = 'friday'
        # Setting day to Saturday
    elif input_day.lower() in ['saturday', 'sat', '06']:
        day = 'saturday'
        # Setting day to Sunday
    elif input_day.lower() in ['sunday', 'sun', '07']:
        day = 'sunday'
    else:
        print('\nPlease Enter A Valid Input\n')
        return get_day()

    if day == 'all':
        print('\nYou have skipped the week_day filtration !\n')
    else:
        print('\nHere\'s your data for {}!\n\n'.format(day))

    print('-'*40)
    return day


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
    
    # loading the csv file and creating a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # making new columns from start_time column and creating the hour,month and day columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    # checking for month filtration
    if month != 'all':
        # making the value of month to integer as the csv contains value of month as an integer
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # checking for week_day filtration and creating new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    #dataframe is being returned
    return df


def time_stats(df):
    """calculates and displays statistics related to the time_started and time_ended"""

    print('\nThe Most Frequent Times of Travelling : \n')
    
    #time.time() returns the current time as a floating point number expressed in seconds since the epoch, in UTC.
    start_time = time.time()

    # calculating the most common month, i have used mode function
    
    #a list is being created to index and show the output of popular_month alphabetically.!
    months1 = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('Most popular month: {}'.format(months1[popular_month-1]).title())

    # calculating the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day of week: {}'.format(popular_day))

    # display the most common start hour
    popular_start_hour = df['start_hour'].mode()[0]
    #converting the time format to 12-hour format
    if 0 <= popular_start_hour < 12:
        print('Most popular start hour: {} AM'.format(popular_start_hour))
    else:
        print('Most popular start hour: {} PM'.format(popular_start_hour-12))
        

    print("\nTime taken to calculate:-  %s second(s) !" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """calculates and displays statistics related to popular stations and trip."""

    print('\nThe Most Popular Stations and Trip :\n')
    
    #time.time() returns the current time as a floating point number expressed in seconds since the epoch, in UTC.
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most popular start station: {}'.format(start_station))

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most popular end station: {}'.format(end_station))

    # display most frequent combination of start station and end station trip
    df['popular_trip'] = df['Start Station'] + " " + "to" + " " +  df['End Station']
    
    #calculating the trip with maximum frequency using mode function
    popular_trip_value = df['popular_trip'].mode()[0]
    #calculating the count of that trip
    count = df['popular_trip'].value_counts().max()

    #print('Most popular trip: {} --> {} ({} times)'.format(most_frequent_start, most_frequent_stop, most_frequent_count))
    print('Most popular trip: {}  ({} times)'.format(popular_trip_value,count))

    print("\nTime taken to calculate:-  %s second(s) !" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTotal and average trip duration :\n')
    start_time = time.time()

    #calculating the sum of total trip durations
    total_duration = df['Trip Duration'].sum()
    
    #The divmod() method takes two numbers and returns a pair of their quotient and remainder
    #converting to minutes and seconds
    minute, second = divmod(total_duration, 60)
    #converting to hours and minutes
    hour, minute = divmod(minute, 60)
    #converting to days and hours
    day,hour=divmod(hour,24)
    print('Total trip duration: {} day(s), {} hour(s), {} minute(s) and {}'
          ' second(s).'.format(day,hour, minute, second))
    
    #calculating the average time 
    avg_duration = round(df['Trip Duration'].mean())
    #converting to minutes and seconds
    m, s = divmod(avg_duration, 60)
    #converting to hours and minutes
    h, m = divmod(m, 60)
    print('Average trip duration: {} hour(s), {} minute(s) and {}'
              ' second(s).'.format(h, m, s))
        
    print("\nTime taken to calculate:-  %s second(s) !" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nShowing statistics on bikeshare users:\n')
    start_time = time.time()

    # Display counts of user types
    print('Total User Types : {}'.format(df['User Type'].nunique()))
    for user_type, count in df['User Type'].value_counts().iteritems():
        print('{}: {}'.format(user_type, count))

    # Display counts of gender
    #we have to filter files as some files dont contain the gender column !.
    if 'Gender' in df.columns:
        print('\nTotal Gender Types : {}'.format(df['Gender'].nunique()))
        #calculating total types of gender
        male_count = df.query('Gender == "Male"').Gender.count()
        female_count = df.query('Gender == "Male"').Gender.count()
        print('Male users : {}\nFemale users : {}\n'.format(male_count, female_count))
    else:
        print('No gender data available.\n')


    # Display earliest, most recent, and most common year of birth
    #we have to filter files as some files dont contain the gender column !.
    if 'Birth Year' in df.columns:
        #calculating most common birth year
        birth_year_common = df['Birth Year'].mode()[0]
        #calculating youngest customer's age
        birth_year_earliest = df['Birth Year'].min()
        #calculating most aged customer's age
        birth_year_most_recent = df['Birth Year'].max()
        print('Most common birth year: {}'.format(int(birth_year_common)))
        print('Earliest birth year: {}'.format(int(birth_year_earliest)))
        print('Most recent birth year: {}'.format(int(birth_year_most_recent)))
    else:
        print('No birth data available.')


    print("\nTime taken to calculate:-  %s second(s) !" % (time.time() - start_time))
    print('-'*40)
    
def extra_questions(df):
    """I have answered some questions which were in my mindset as a data analyst """

    print('\nData Analysed By Me :\n')
    
    start_time = time.time()

    if 'Gender' in df.columns:
        most_gender = df.groupby(['Start Station', 'Gender']).size().sort_values(ascending=False).to_frame(name='Count').reset_index().iloc[0]
        most_start = most_gender['Start Station']
        gender_type = most_gender['Gender']
        count_gender_type = most_gender['Count']
        print('Maximum active station: {} {} travel from  {} \n'.format(count_gender_type ,gender_type,most_start))
    
        min_gender = df.groupby(['Start Station', 'Gender']).size().sort_values(ascending=True).to_frame(name='Count').reset_index().iloc[0]
        min_start = min_gender['Start Station']
        gender_type2 = min_gender['Gender']
        count_gender_type2 = min_gender['Count']
        print('Minimun active station: {} {} travel from  {} \n '.format(count_gender_type2 ,gender_type2,min_start))
    
        print("So i think ,we should focus on those stations which have minimun no. of customers and attract them.")
    else:
        print("No data analysed for this city!")

    print("\nTime taken to calculate:-  %s second(s) !" % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        print('Hello! Let\'s explore some US bikeshare data!')
        #calling city function to input city name
        city = get_city()
        #calling month function to input month name
        month = get_month()
        #calling day function to input week_day
        day = get_day()
        
        #calling load_data function to read csv file 
        #dataframe is created in this function and modified according to the user inputs
        df = load_data(city, month, day)

        #calling functions to display data
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        extra_questions(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
