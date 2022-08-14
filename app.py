import streamlit as st
from lyrics_visualizer import *

# disable warning when calling st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("""
# Lyrics Frequency Visualizer
""")

st.markdown("""
This app takes a Spotify playlist containing Japanese songs and displays the frequencies of the top words in all of the lyrics.

Requirements to use this app:
* A Spotify account (does not need to be a Premium account)
* Your Spotify client ID and client secret ([how to obtain these](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/))
* Python libraries: `requests`, `re`, `time`, `os`, `base64`, `datetime`, `pandas`, `collections`, `spacy`, `advertools`, `csv`, `matplotlib.pyplot`, `japanize_matplotlib`
    * If you don't have one of the following modules, then type `pip install <module>` in the terminal to install it.
    * In addition to the `spacy` library, you will also need to download the Japanese pipeline (type the following below into the terminal to download both `spacy` and the Japanese pipeline)
""")

st.code("""
$ pip install -U pip setuptools wheel
$ pip install -U spacy
$ python -m spacy download ja_core_news_sm
""")

st.markdown("""
Notes:
* The lyrics may not be accurate, so you can check the lyrics for each song in the folder `songs`.
* The top words are in Japanese and are not translated into English - you can use Google Translate's camera on the mobile app if you would like to see the translations.
* There is an interval of 10 seconds set between each scrape as to not overload any servers (since each song requires scraping the sites [DuckDuckGo](https://duckduckgo.com/) and [Lyrical Nonsense](https://www.lyrical-nonsense.com/)). As a result, the process of downloading the lyrics will be slow if there are many songs in the playlist. If you would like to change this, go to the `get_first_duckduckgo_link()` method in the `LyricsExtract` class and change the paramter of `time.sleep()`.
""")

client_id = st.text_input("Spotify Client ID")
client_secret = st.text_input("Spotify Client Secret")
playlist_id = st.text_input("Playlist ID (Private Playlists Allowed)", "37i9dQZF1EIYEv8LTId1b8")


try:
    spotify = SpotifyAPI(client_id, client_secret)
    df = spotify.create_tracks_df(playlist_id)
    st.write(df)

    # spotify.get_lyrics_for_all_songs(playlist_id, "test")

    n = st.slider("Number of top words", 1, 40, 20)

    fig = WordCounter().visualize_word_freqs("test", "results", n)
    st.pyplot(fig)

except:
    st.write("**At least one of the fields entered above is invalid.**")