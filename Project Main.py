import pandas as pd
import time
import matplotlib.pyplot as plt
import keyboard
import os


data = pd.read_csv('spotify_top_charts_22.csv')
df = pd.DataFrame(data)
df = df.drop('uri', axis=1)


def intro():
    msg = ('''
    *=============================================================*
    |               Informatics Practices Practical               |
    |                        Session 2023-24                      |
    *-------------------------------------------------------------*
    |  Topic   :     Spotify top songs of 2022                    |     
    |  By      :     Ashutosh Pandey                              |
    |  Roll No :     10                                           | 
    |  Class   :     XII                                          |
    |  Section :     Alpha                                        | 
    *=============================================================*
    ''')

    for i in msg:
        # time.sleep(0.002)
        print(i, end="")

    inp = input("Press ENTER key to continue : ")

    if keyboard.KEY_DOWN:
        main_menu()


def main_menu():
    msg = ('''
    *=========================================*
    |                Main Menu                |
    *=========================================*
    | 1 | Go to data analysis menu            |
    | 2 | Go to graphical data analysis menu  |
    | 3 | Go to developer information         |
    | 0 | Exit application                    |
    *=========================================*
    ''')

    for i in msg:
        # time.sleep(0.001)
        print(i, end="")

    inp = input('Enter the number corresponding to your choice : ')

    if inp == '1':
        msg = ('''
        Loading Data Analysis Menu...
        ''')

        for i in msg:
            # time.sleep(0.02)
            print(i, end='')

        data_analysis_menu()

    elif inp == '2':
        msg = '''
        Loading Graphical Data Analysis Menu.....
        '''

        for i in msg:
            #time.sleep(0.02)
            print(i,end = "")

        graphical_menu()

    elif inp == '0':
        msg = '''
        Thank You For Using My Application

                                      -Dev
        '''

        for i in msg:
            time.sleep(0.1)
            print(i, end='')

    else:
        print('''
        Invalid Choice
        ''')
        # time.sleep(2)
        main_menu()


def data_analysis_menu():
    msg = ('''
    *======================================*
    |          Data Analysis Menu          |
    *======================================*
    | 1 | Search by artist name            |
    | 2 | Search by track name             |
    | 3 | Sort by weeks on chart           |
    | 4 | Sort by length                   |
    | 0 | Go back                          |
    *======================================*
    ''')

    for i in msg:
        # time.sleep(0.01)
        print(i, end='')

    inp = input("Enter the number corresponding to your choice : ")

    if inp == '1':
        msg = ('''
            Loading sort by artist name.....
            ''')

        for i in msg:
            # time.sleep(0.02)
            print(i, end="")

        print('Enter 0 to go back')
        dam_code1()

    elif inp == '2':
        msg = ('''
            Loading sort by track name....
            ''')

        for i in msg:
            # time.sleep(0.01)
            print(i, end="")

        print('Enter 0 to go back')
        dam_code2()

    elif inp == '3':
        msg = ('''
                Loading sort by weeks on chart....
                ''')

        for i in msg:
            # time.sleep(0.01)
            print(i, end="")

        print('Enter 0 to go back')

        dam_code3()

    elif inp == '4':
        msg = ('''
                Loading sort by length....
                ''')

        for i in msg:
            # time.sleep(0.01)
            print(i, end="")

        print('Enter 0 to go back')

        dam_code4()

    elif inp == '0':
        main_menu()

    else:
        print('''
        Invalid Choice
        ''')
        time.sleep(2)
        data_analysis_menu()


def graphical_menu():
    msg = ('''
    *========================================================*
    |               Graphical Data Analysis Menu             |
    *========================================================*
    | 1 | Graph of weeks on chart by an artist               |
    | 2 | Graph of Energy on a track by an artist            |
    | 3 | Graph of an artist's Acousticness                  |
    | 4 | Graph of Danceability on a track by an artist      |
    | 0 | Go back                                            |
    *========================================================*
    ''')

    for i in msg:
        #time.sleep(0.01)
        print(i, end="")

    inp = input('''
    Enter the number corresponding to your choice : ''')

    if inp == '1':
        msg = '''
            Preparing to plot graph...
            '''
        for i in msg:
            #time.sleep(0.02)
            print(i, end="")

        print('Enter 0 to go back')

        gm_code1()

    if inp == '2':

        msg = '''
            Preparing to plot graph...
            '''

        for i in msg:

            #time.sleep(0.02)
            print(i, end="")

        print('Enter to go back')

        gm_code2()

    if inp == '3':

        msg = '''
                Preparing to plot graph...
                '''
        for i in msg:

            # time.sleep(0.02)
            print(i, end="")

        print('Enter to go back')

        gm_code3()

    if inp == '4':

        msg = '''
                        Preparing to plot graph...
                        '''
        for i in msg:
            # time.sleep(0.02)
            print(i, end="")

        print('Enter to go back')

        gm_code4()

    if inp == '0':
        main_menu()


def dam_code1():
    df_drop = ['danceability', 'energy', 'key', 'loudness', 'mode',
               'speechiness', 'acousticness', 'tempo', 'time_signature',
               'instrumentalness', 'liveness', 'duration_ms']

    df1 = df.drop(columns=df_drop)

    inp1 = input('''
    Enter artist name to sort by(case sensitive) - ''')

    if inp1 == '0':
        data_analysis_menu()

    else:
        op = df1['artist_names'] == inp1
        df2 = df1[op]

        if df2.empty:
            print('''
            Sorry No data available
            ''')

        else:
            print(df2)

        dam_code1()


def dam_code2():
    df_drop = ['danceability', 'energy', 'key', 'loudness', 'mode',
               'speechiness', 'acousticness', 'tempo', 'time_signature',
               'instrumentalness', 'liveness', 'duration_ms']

    df1 = df.drop(columns=df_drop)

    inp1 = input('''
    Enter track name to sort by - ''')

    if inp1 == '0':
        data_analysis_menu()

    else:
        op = df1['track_name'] == inp1
        df2 = df1[op]

        if df2.empty:
            print('''
            Sorry No data available
            ''')
            time.sleep(2)

        else:
            print(df2)

        dam_code2()


def dam_code3():
    df_drop = ['danceability', 'energy', 'key', 'loudness', 'mode',
               'speechiness', 'acousticness', 'tempo', 'time_signature',
               'instrumentalness', 'liveness', 'duration_ms', 'peak_rank']

    df1 = df.drop(columns=df_drop)

    inp = input('''
    Enter number of weeks to sort by - ''')

    inp1 = int(inp)

    if inp1 == '0':
        data_analysis_menu()

    else:
        op = df1['weeks_on_chart'] == inp1
        df2 = df1[op]

        if df2.empty:
            print('''
            Sorry No data available
            ''')
            time.sleep(2)

        else:
            print(df2)

        dam_code3()


def dam_code4():
    df_drop = ['danceability', 'energy', 'key', 'loudness', 'mode',
               'speechiness', 'acousticness', 'tempo', 'time_signature',
               'instrumentalness', 'liveness', 'peak_rank']

    df1 = df.drop(columns=df_drop)
    df1['length'] = df1['duration_ms'] / 60000
    df1 = df1.drop(columns='duration_ms')
    df1 = round(df1, 1)

    print('''Enter 0 to go back''')

    inp = input('''
        Enter length in minutes(e.g- 3.5) - ''')
    inp1 = float(inp)

    if inp1 == 0:
        data_analysis_menu()

    else:
        op = df1['length'] == inp1
        df2 = df1[op]

        if df2.empty:
            print('''
            Sorry No data available
            ''')

        else:
            print(df2)

        dam_code4()


def gm_code1():
    df_drop = ['peak_rank', 'danceability', 'energy',
               'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
               'liveness', 'tempo', 'time_signature', 'duration_ms']
    df1 = df.drop(columns=df_drop)

    inp = input('''
    Enter name of artist(case sensitive) : ''')

    if inp == '0':
        graphical_menu()
    else:
        op = df1['artist_names'] == inp
        df2 = df1[op]

        if df2.empty:
            print('''
            Sorry no data available...''')
        else:
            plt.figure(figsize=(12, 6))
            #plt.set_facecolor('lightgray')
            plt.plot(df2['track_name'], df2['weeks_on_chart'],
                     color='red', lw=2, marker='*',
                     markerfacecolor='black', markeredgecolor = 'black')
            plt.title('Weeks On Chart per Song')
            plt.ylabel('Weeks on chart')
            plt.xlabel('Track name')
            plt.xticks(rotation=45)
            plt.show()
        gm_code1()


def gm_code2():
    df_drop = ['peak_rank', 'danceability', 'key', 'loudness',
               'mode', 'speechiness', 'acousticness', 'instrumentalness',
               'liveness', 'tempo', 'time_signature', 'duration_ms', 'weeks_on_chart']
    df1 = df.drop(columns=df_drop)

    inp = input('''
        Enter name of artist(case sensitive) : ''')

    if inp == '0':
        graphical_menu()
    else:
        op = df1['artist_names'] == inp
        df2 = df1[op]

        if df2.empty:
            print('''
                Sorry no data available...''')
        else:
            plt.figure(figsize=(12, 6))
            # plt.set_facecolor('lightgray')
            plt.plot(df2['track_name'], df2['energy'],
                     color='red', lw=2, marker='*',
                     markerfacecolor='black', markeredgecolor='black')
            plt.title('Energy in a track by an artist')
            plt.ylabel('Energy Level')
            plt.xlabel('Track name')
            plt.xticks(rotation=45)
            plt.show()
        gm_code2()


def gm_code3():
    df_drop = ['peak_rank', 'danceability', 'key', 'loudness', 'energy',
               'mode', 'speechiness', 'instrumentalness',
               'liveness', 'tempo', 'time_signature', 'duration_ms', 'weeks_on_chart']
    df1 = df.drop(columns=df_drop)

    inp = input('''
            Enter name of artist(case sensitive) : ''')

    if inp == '0':
        graphical_menu()
    else:
        op = df1['artist_names'] == inp
        df2 = df1[op]

        if df2.empty:
            print('''
                    Sorry no data available...''')
        else:
            plt.figure(figsize=(12, 6))
            # plt.set_facecolor('lightgray')
            plt.plot(df2['track_name'], df2['acousticness'],
                     color='red', lw=2, marker='*',
                     markerfacecolor='black', markeredgecolor='black')
            plt.title('Energy of a track by an artist')
            plt.ylabel('Acousticness')
            plt.xlabel('Track name')
            plt.xticks(rotation=45)
            plt.show()
        gm_code3()


def gm_code4():

    df_drop = ['peak_rank', 'acousticness', 'key', 'loudness', 'energy',
               'mode', 'speechiness', 'instrumentalness',
               'liveness', 'tempo', 'time_signature', 'duration_ms', 'weeks_on_chart']
    df1 = df.drop(columns=df_drop)

    inp = input('''
                Enter name of artist(case sensitive) : ''')

    if inp == '0':
        graphical_menu()
    else:
        op = df1['artist_names'] == inp
        df2 = df1[op]

        if df2.empty:
            print('''
                        Sorry no data available...''')
        else:
            plt.figure(figsize=(12, 6))
            plt.bar(df2['track_name'], df2['danceability'],
                     color='black', lw=2)
            plt.title('Energy of a track by an artist')
            plt.ylabel('Dancaebility')
            plt.xlabel('Track name')
            plt.xticks(rotation=45)
            plt.show()
        gm_code4()


intro()