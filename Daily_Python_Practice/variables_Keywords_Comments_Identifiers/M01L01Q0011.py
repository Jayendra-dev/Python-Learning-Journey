#Objective: Create variables using all five basic Python 
# data types and calculate the average listening time per song.

# Spotify Wrapped

# Creating variables
user_name = "Rahul"
songs_played = 250       # int
hours_listened = 125.5   # float
top_artist = "Arijit Singh"  # str
is_premium = True        # bool

# Printing 4-line summary
print("Spotify Wrapped Summary")
print("User:", user_name, "| Songs Played:", songs_played)
print("Hours Listened:", hours_listened, "| Top Artist:", top_artist)
print("Premium User:", is_premium)

# Calculating average minutes per song
average_minutes = (hours_listened * 60) / songs_played

print("Average minutes per song:", average_minutes)


"""Spotify Wrapped Summary
User: Rahul | Songs Played: 250
Hours Listened: 125.5 | Top Artist: Arijit Singh
Premium User: True
Average minutes per song: 30.12"""