import main as m

def title():
    print(m.Title)

def artist():
    print(m.Artist)

def publisher():
    print(m.Publisher)

#boolean return
def myFavoriteSong(SongName):
    if SongName == "A Hard Day's Night":
        return True
    else:
        return False

#call functions
title()
artist()
publisher()

#boolean
myFavorite = myFavoriteSong(m.Title)
if myFavorite==True:
    print("Yes, this is my favorite song.")
else:
    print("No, this is not my favorite song")