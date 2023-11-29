import SiteScraper as ss
import pandas as pd 
video_object = ss.yt_vedio()
new_data = video_object.yt_vedios_data("https://www.youtube.com/@bbcearth/videos")


df = pd.read_csv('bbc.csv')
df['title'] = new_data['title']
df['views']=new_data['views']
df['when']=new_data['when']
df.to_csv('bbc.csv')
