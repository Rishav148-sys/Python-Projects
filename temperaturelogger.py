import math

# Global variable - accessible anywhere in the program
station_name = "Kathmandu Weather Station"

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]


def get_average(temps):
    """Returns the mean temperature."""
    return sum(temps) / len(temps)


def get_deviation(temps):
    """Returns standard deviation using math.sqrt."""
    
    # Local variable - only accessible inside this function
    local_mean = get_average(temps)
    
    variance = sum((t - local_mean) ** 2 for t in temps) / len(temps)
    return math.sqrt(variance)


def get_summary(temps):
    """Prints min, max, average, and deviation."""
    
    print("Station:", station_name)
    print("-----------------------------------")
    print("Minimum Temperature :", min(temps), "°C")
    print("Maximum Temperature :", max(temps), "°C")
    print("Average Temperature :", round(get_average(temps), 2), "°C")
    print("Standard Deviation  :", round(get_deviation(temps), 2), "°C")
    print("-----------------------------------")


# Call the summary function
get_summary(temperatures)
