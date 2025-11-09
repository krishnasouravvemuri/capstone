MOVIE_URLS = {
    "happy": "https://www.themoviedb.org/genre/35-movie",
    "sad": "https://www.themoviedb.org/genre/10751-family/movie",
    "angry": "https://www.themoviedb.org/genre/28-movie",
    "fear": "https://www.themoviedb.org/genre/27-movie",
    "surprise": "https://www.themoviedb.org/genre/878-movie",
    "neutral": "https://www.themoviedb.org/genre/99-movie",
    "disgust": "https://www.themoviedb.org/genre/16-movie",
}

SPOTIFY_PLAYLISTS = {
    "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
    "angry": "https://open.spotify.com/playlist/37i9dQZF1DWXe9gFZP0gtP",
    "fear": "https://open.spotify.com/playlist/37i9dQZF1DWYWddJiPzbvb",
    "surprise": "https://open.spotify.com/playlist/37i9dQZF1DX1kCIzMYtzum",
    "neutral": "https://open.spotify.com/playlist/37i9dQZF1DX2sUQwD7tbmL",
    "disgust": "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6",
}

def recommend_links(emotion, mode):
    """Return a URL instead of opening it."""
    emotion = emotion.lower().strip()
    if mode == "spotify":
        return SPOTIFY_PLAYLISTS.get(emotion, SPOTIFY_PLAYLISTS["happy"])
    elif mode == "movies":
        return MOVIE_URLS.get(emotion, MOVIE_URLS["sad"])
    else:
        return None
