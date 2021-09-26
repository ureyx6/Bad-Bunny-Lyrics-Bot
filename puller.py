import lyricsgenius
import random
from lyricsgenius.types.song import Song
import tweepy
keys = {
    'CONSUMER_API_KEY': 'YOUR KEY HERE',
    'CONSUMER_API_SECRET_KEY': 'YOUR KEY HERE',
    'ACCESS_TOKEN': 'YOUR KEY HERE',
    'ACCESS_TOKEN_SECRET': 'YOUR KEY HERE'
}
all_songs = ["Amorfoda", "Tú No Metes Cabra", "MÍA", "Yonaguni", "Chambea", "Soy Peor", "Si Veo a Tu Mamá", "Tú No Metes Cabra (Remix)", "Vete", "Estamos Bien", "Yo Perreo Sola", "Dime Si Te Acuerdas", "25/8", "La Difícil", "Otra Noche en Miami", "BOOKER T", "HACIENDO QUE ME AMAS", "La Romana", "Soy Peor (Remix)", "A Tu Merced", "﹤3", "Si Estuviésemos Juntos", "TE MUDASTE", "NI BIEN NI MAL", "Solo de Mí", "BYE ME FUI", "De Museo", "Pero Ya No", "Diles", "YO VISTO ASÍ", "Soliá", "EN CASITA", "RLNDT", "Caro", "ANTES QUE SE ACABE", "RONCA FREESTYLE", "TE DESEO LO MEJOR", "TRELLAS", "HOY COBRÉ", "200 MPH", "120", "LA DROGA", "MALDITA POBREZA", "La Zona", "EL MUNDO ES MÍO", "BENDICIONES", "Como Antes", "¿Quién Tú Eres?", "SI ELLA SALE", "Dime Si Vas A Volver", "Ser Bichote", "COMPOSITOR DEL AÑO", "6 Rings", "Cuando Perriabas", "Pa’ Que Le De (Remix)", "Tenemos Que Hablar", "Contigo", "Me Llueven 3.0", "Desde el Corazón", "Me Importa Un Carajo", "La T-Shirt De Biggie", "Solo Avísame", "Vamos Pa’ La Calle (Remix)", "La Vida", "CYNH2", "Soy Peor (Mambo Remix)", "Me Rolie (Mami No Sé)", "Mood (Freestyle)", "Pa’ Que Le De", "El Freestyle", "Es Tiempo", "Mi Puerto Rico", "Soy Culpable", "El Chapo (Freestyle)", "Get","Bad Bunny: Problemas de un niño normal", "Tentación", "No Perdamos Tiempo", "Estamos Cabrón", "Lo De Nosotros", "Calentando (Freestyle)", "Explícame", "Another (Freestyle)", "Freestyle por Grupo (21/05/2019)", "Vamos a Llegar", "En Lo Que (Freestyle)", "Flow Exagerao", "Perdonen", "Como Yo No Hay 2",
 "Sigan Tirando"]

def get_raw_lyrics():
    genius_client_access_token = "YOUR KEY HERE"
    genius = lyricsgenius.Genius(genius_client_access_token)
    random_song_title = random.choice(all_songs)
    lyrics = genius.search_song(random_song_title, "Bad Bunny").lyrics
    return lyrics, Song

def get_tweet_from(lyrics):
    lines = lyrics.split('\n')
    for index in range(len(lines)):
        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i != "XXX"]

    random_num = random.randrange(0, len(lines)-1)
    tweet = lines[random_num] + "\n" + lines[random_num+1]
    tweet = tweet.replace("\\", "")
    return tweet

def handler(event, context):
    auth = tweepy.OAuthHandler(
        keys['CONSUMER_API_KEY'],
        keys['CONSUMER_API_SECRET_KEY']
    )
    auth.set_access_token(
        keys['ACCESS_TOKEN'],
        keys['ACCESS_TOKEN_SECRET']
    )
    api = tweepy.API(auth)
    lyrics, Song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics)
    status = api.update_status(tweet)

    return tweet
    raise SystemExit