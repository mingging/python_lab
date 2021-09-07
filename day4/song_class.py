class Song(object):
    def __init__(self, lyrics):
        self.lyrice = lyrics
    
    def sing_a_song(self):
        for line in self.lyrice:
            print(line)