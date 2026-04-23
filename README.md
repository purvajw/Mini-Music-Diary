import tkinter as tk
import random

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Mini Music Diary")
root.geometry("500x670")
root.config(bg="#e8c7cc")

# ---------------- SONG DATABASE ----------------
music_db = {
    "happy": [
        "Kiss It Better - Rihanna",
        "Obsessed - Mariah Carey",
        "Confident - Justin Bieber",
        "Genie in a bottle - Christina Aguilera",
        "Heartbeat - Childish Gambino",
        "Fame is a Gun - Addison Rae",
        "Kiss and MakeUp - Dua Lipa, Blackpink",
        "Last Friday Night - Katy Perry",
        "Copines - Aya Nakamura",
        "Confidence - Kim",
        "What Do You Mean - Justin Bieber",
        "Every Summertime - NIKI",
        "Die For You - The Weeknd, Ariana Grande",
        "What is Love? - Twice"
    ],

    "sad": [
        "Someone Like You - Adele",
        "Let Her Go - Passenger",
        "Fix You - Coldplay",
        "Call Out My Name - Weeknd",
        "back to friends - sombr",
        "Say Yes To Heaven - Lana del Rey",
        "WILDFLOWER - Billie Eilish",
        "Heather - Conan Gray",
        "the grudge - Olivia Rodrigo",
        "Bad At Love - Halsey",
        "Dancing With Your Ghost - Sasha Alex Sloan",
        "twin - Jennie",
        "ONLY - LEEHI"
    ],

    "relaxed": [
        "Sunset Lover - Petit Biscuit",
        "Sunsetz - Cigarettes After Sex",
        "Unforgettable - French Montana",
        "american wedding - dopuu",
        "Still with you - Jungkook",
        "the perfect pair - beabadoobee",
        "Show Me Love (with Tyla) - WizTheMc",
        "Seoul City - Jennie",
        "Is There Someone Else? - The Weeknd",
        "Apocalypse - Cigarettes After Sex",
        "Melting - Kali Uchis",
        "Pink + White - Frank Ocean",
        "bad - wave to earth",
        "Make It To The Morning - PARTYNEXTDOOR"
    ],

    "energetic": [
        "Wannabe - ITZY",
        "GLAMOUR - Uniqe",
        "Levitating - Dua Lipa",
        "Swim - Chase Atlantic",
        "Dracula - Tame Impala, Jennie",
        "Stateside + Zara Larsson - PinkPantheress",
        "(When You Gonna) Give It Up To Me - Sean Paul, Keyshia Cole",
        "Mantra - Jennie",
        "Moulaga - Heuss L'enfoiré, Jul",
        "Mala - 6ix9ine, Anuel AA",
        "b2b - Charli XCX",
        "Hotel Lobby - Tobi",
        "NO BATIDÃO - ZXKAI"
    ],

    "love": [
        "Lover girl - Laufey",
        "from the start - Laufey",
        "Reflections - The Neighbourhood",
        "Love Story - Taylor Swift",
        "My Love Mine All Mine - Mitski",
        "her - JVKE",
        "Young and Beautiful - Lana Del Rey",
        "There Is a Light That Never Goes Out - The Smiths",
        "About You - The 1975",
        "we can't be friends - Ariana Grande",
        "Daydreaming - Ariana Grande",
        "Ye Ishq Hai - Pritam",
        "Jeene Laga Hoon - Sachin-Jigar",
        "I Wanna Be Yours - Arctic Monkeys",
        "Love Grows (Where My Rosemary Goes) - Edison Lighthouse",
        "Fall in Love Alone - Stacey Ryan"
    ]
}

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="୨ৎ Mini Music Diary ୨ৎ",
    font=("Georgia", 18, "bold"),
    bg="#e8c7cc",
    fg="#6e1f34"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="⋆｡‧˚ʚ How are you feeling? ɞ˚‧｡⋆",
    font=("Helvetica", 10, "italic"),
    bg="#e8c7cc",
    fg="#555555"
)
subtitle.pack()

# ---------------- CARD ----------------
card = tk.Frame(root, bg="#f9ecee")
card.pack(padx=25, pady=20, fill="both", expand=True)

label = tk.Label(
    card,
    text="Enter your current mood",
    font=("Helvetica", 12, "bold"),
    bg="#f9ecee",
    fg="#6e1f34"
)
label.pack(pady=(20, 10))

entry = tk.Entry(
    card,
    width=28,
    font=("Helvetica", 12),
    justify="center",
    bg="#f2d8dc",
    fg="#555555",
    bd=0
)
entry.pack(ipady=8)

# ---------------- PLAYLIST SECTION ----------------
playlist_label = tk.Label(
    card,
    text="♡ Recommended Songs ♡",
    font=("Helvetica", 11, "bold"),
    bg="#f9ecee",
    fg="#6e1f34"
)
playlist_label.pack(pady=15)

frame = tk.Frame(card, bg="#f9ecee")
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

playlist_box = tk.Listbox(
    frame,
    width=44,
    height=10,
    yscrollcommand=scrollbar.set,
    font=("Helvetica", 10),
    bg="#f2d8dc",
    fg="#555555",
    bd=0,
    highlightthickness=0,
    selectbackground="#b56576",
    selectforeground="white"
)
playlist_box.pack()

scrollbar.config(command=playlist_box.yview)

# ---------------- PLAYER DISPLAY ----------------
player_display = tk.Label(
    card,
    text="» choose a song «\n0:00 ─〇───── 0:00\n⇄   ◃◃   ⅠⅠ   ▹▹   ↻",
    font=("Helvetica", 11),
    bg="#f9ecee",
    fg="#6e1f34",
    justify="center"
)
player_display.pack(pady=20)

# ---------------- FUNCTIONS ----------------
def get_music():
    mood = entry.get().lower().strip()
    playlist_box.delete(0, tk.END)

    if any(word in mood for word in ["happy", "excited", "joyful"]):
        mood_key = "happy"
    elif any(word in mood for word in ["sad", "lonely", "heartbroken"]):
        mood_key = "sad"
    elif any(word in mood for word in ["relaxed", "calm", "stressed"]):
        mood_key = "relaxed"
    elif any(word in mood for word in ["energetic", "motivated"]):
        mood_key = "energetic"
    elif any(word in mood for word in ["love", "romantic"]):
        mood_key = "love"
    else:
        mood_key = random.choice(list(music_db.keys()))

    songs = random.sample(music_db[mood_key], len(music_db[mood_key]))

    for song in songs:
        playlist_box.insert(tk.END, f"♡ {song}")

    player_display.config(
        text=f"» ♡ {songs[0]} «\n0:00 ─〇───── 0:00\n⇄   ◃◃   ⅠⅠ   ▹▹   ↻"
    )

def select_song(event):
    selected = playlist_box.get(tk.ACTIVE)
    player_display.config(
        text=f"» {selected} «\n0:00 ─〇───── 0:00\n⇄   ◃◃   ⅠⅠ   ▹▹   ↻"
    )

playlist_box.bind("<<ListboxSelect>>", select_song)

# ---------------- BUTTON ----------------
button = tk.Button(
    card,
    text="♡ get playlist ♡",
    command=get_music,
    font=("Helvetica", 11, "bold"),
    bg="#a9445b",
    fg="white",
    activebackground="#6e1f34",
    activeforeground="white",
    bd=0,
    padx=18,
    pady=8
)
button.pack(pady=20)

# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    text="By Purva ♡",
    font=("Helvetica", 9, "italic"),
    bg="#e8c7cc",
    fg="#555555"
)
footer.pack(pady=10)

root.mainloop()
