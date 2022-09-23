from pytube import YouTube

link = input("The video Link: ")
yt = YouTube(link) # searches the link in youtube

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/dattakiranrao/Downloads')