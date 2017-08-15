import time,webbrowser

def take_a_break(url_to_open,num_of_breaks = 3,sleep_duration = 60*60*3):
    """
    Function to open webpage at specified time interval.

    url_to_open = string. Web page to open at break time.
    num_of_breaks = int. Number of breaks.
    sleep_duration = int. Time interval between breaks in seconds.
    """
    print('This function started at: {}'.format(time.ctime()))
    for i in range(num_of_breaks):
        time.sleep(sleep_duration)
        webbrowser.open(url_to_open, new=1, autoraise=True)

take_a_break('https://www.youtube.com/user/allindiabakchod')            


    