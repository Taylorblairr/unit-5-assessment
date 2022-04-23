log_file = open("um-server-01.txt") ##This line denotes the file that will hold the logs for this code


def sales_reports(log_file): ## This line defines The function and passes the parameter "log_file"
    for line in log_file: ##This line starts a loop in the "log_file" parameter
        line = line.rstrip()##This line utlizes rstrip which removes all characters at an end of a string
        day = line[0:3] ##This line creates a new paramater for "day" and makes a list of 0 through 3
        if day == "Tue":##This line creates a boolean and asks if the day is "tues"
            print(line)##This line prints the line paramater to the console


sales_reports(log_file)## This line inserts the sales report functuin unti the logfile parameter
