class Time:
    """ The Time class defines the time with
    attributes: hour, minutes, seconds
    """
    hour = 12
    minutes = 00
    seconds = 00
    def get_hour(Time):
        return Time.hour

    def get_minute(Time):
        return Time.minutes

    def get_second(Time):
        return Time.seconds

    def print_time(Time):
        print(Time.hour, ":", Time.minutes, ":", Time.seconds)

    def set_hour(Time, new_hour):
        Time.hour = new_hour

    def set_minute(Time, new_minute):
        Time.minutes = new_minute

    def set_second(Time, new_second):
        Time.seconds = new_second

    def increment_second(Time, seconds):
        if Time.seconds <= 60:
            Time.seconds += 1

        elif Time.seconds >= 61:
            Time.minutes += 1

    def increment_minute(Time, seconds):
        if Time.minutes <= 60:
            Time.seconds += 1

        elif Time.minutes >= 61:
            Time.hour += 1

    def increment_hour(Time, hour):
        if Time.hour <= 12:
            Time.hour += 1

        elif Time.hour >= 13:
            Time.hour = 1

Time.print_time(Time)
    
time1 = Time()

time1.set_hour(int(input("Enter the hour")))

time1.set_minute(int(input("Input the minutes")))

time1.set_second(int(input("Input the seconds")))
