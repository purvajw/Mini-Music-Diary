import tkinter as tk
from tkinter import ttk
import random
import pygame
import os
import json
from datetime import datetime

# ---------------- INITIALIZE ----------------
pygame.mixer.init()

root = tk.Tk()
root.title("Mini Music Diary")
root.geometry("450x670")
root.config(bg="#e8c7cc")

# ---------------- SONG DATABASE ----------------

happy_songs = [
    ("Kiss It Better - Rihanna", "music/Rihanna_-_Kiss_It_Better_ScaryBeatz.com.mp3"),
    ("Fame is a Gun - Addison Rae", "music/Addison Rae  Fame is a Gun - Copy.mp3"),
    ("Catch Catch - YENA", "music/SpotiDown.App - Catch Catch - YENA.mp3"),
    ("Obsessed - Mariah Carey", "music/SpotiDown.App - Obsessed - Mariah Carey.mp3"),
    ("Stateside + Zara Larsson - PinkPantheress", "music/Stateside + Zara Larsson - PinkPantheress .mp3"),
    ("Swim - Chase Atlantic", "music/Chase Atlantic - Swim.mp3"),
]

sad_songs = [
    ("Call Out My Name - The Weeknd", "music/Call Out My Name - The Weeknd.mp3"),
    
]

love_songs = [
    ("Love For You - LOVELI LORI", "music/loveli lori & ovg! - love for you (Official Audio) - LOVELI LORI (youtube).mp3"),
    ("Seoul City - JENNIE", "music/JENNIE_-_Seoul_City_(mp3.pm).mp3"),
    ("Kiss It Better - Rihanna", "music/Rihanna_-_Kiss_It_Better_ScaryBeatz.com.mp3"),
    ("Love For You - Slowed Down - LOVELI LORI", "music/SpotiDown.App - Love For You - Slowed Down - LOVELI LORI.mp3"),
    ("Handlebars - Jennie", "music/JENNIE (BLACKPINK) - Handlebars (feat. Dua Lipa).mp3"),
]

calm_songs = [
    ("Seoul City - JENNIE", "music/JENNIE_-_Seoul_City_(mp3.pm).mp3"),
    ("MAKE IT TO THE MORNING - PARTYNEXTDOOR", "music/PARTYNEXTDOOR - MAKE IT TO THE MORNING (Official Visualizer).mp3"),
    ("Love For You - Slowed Down - LOVELI LORI", "music/SpotiDown.App - Love For You - Slowed Down - LOVELI LORI.mp3"),
    ("Swim - Chase Atlantic", "music/Chase Atlantic - Swim.mp3"),
    ("Paradise - Chase Atlantic", "music/Chase_Atlantic_-_Paradise_(mp3.pm).mp3"),
    ("Sao Paulo - The Weeknd feat. Anitta", "music/The Weeknd - São Paulo feat. Anitta (Official Audio).mp3"),
    ("One Of The Girls - The Weeknd, JENNIE, and Lily-Rose Depp", "music/One Of The Girls (with JENNIE, Lily Rose Depp) -  The Weeknd, JENNIE, and Lily-Rose Depp.mp3"),
]

kpop_songs = [
    ("WANNABE - ITZY", "music/ITZY WANNABE MV @ITZY.mp3"),
    ("Handlebars - Jennie", "music/JENNIE (BLACKPINK) - Handlebars (feat. Dua Lipa).mp3"),
    ("Super shy - new jeans", "music/NewJeans  - Super Shy.mp3"),
    ("Catch Catch - YENA", "music/SpotiDown.App - Catch Catch - YENA.mp3"),
    ("Seoul City - JENNIE", "music/JENNIE_-_Seoul_City_(mp3.pm).mp3"),
]

weeknd_songs = [
    ("Call Out My Name - The Weeknd", "music/Call Out My Name - The Weeknd.mp3"),
    ("Sao Paulo - The Weeknd feat. Anitta", "music/The Weeknd - São Paulo feat. Anitta (Official Audio).mp3"),
    ("One Of The Girls - The Weeknd, JENNIE, and Lily-Rose Depp", "music/One Of The Girls (with JENNIE, Lily Rose Depp) -  The Weeknd, JENNIE, and Lily-Rose Depp.mp3"),
]

bollywood_songs = [
   
]


music_db = {
    "happy": happy_songs,
    "bored": happy_songs,
    "dance": happy_songs,
    "baddie": happy_songs,
    "excited": happy_songs,
    "joyful": happy_songs,

    "sad": sad_songs,
    "lonely": sad_songs,
    "heartbroken": sad_songs,

    "love": love_songs,
    "romantic": love_songs,

    "relaxed": calm_songs,
    "calm": calm_songs,
    "chill": calm_songs,

    "kpop": kpop_songs,
    "confident": kpop_songs,

    "weeknd": weeknd_songs,
    "sexy": weeknd_songs,

    "hindi": bollywood_songs,
    "bollywood": bollywood_songs,
}

current_playlist = []
current_index = 0
current_song_path = None
is_paused = False
autoplay_job = None  # holds the root.after() id so we can cancel it cleanly

# ---------------- DIARY STORAGE ----------------
DIARY_FILE = "diary_entries.json"


def load_diary():
    """Read saved diary entries from disk. Returns [] if the file
    doesn't exist yet or is empty/corrupted."""
    if not os.path.exists(DIARY_FILE):
        return []
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_diary(entries):
    with open(DIARY_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)


diary_entries = load_diary()

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="୨ৎ My Mini Music Diary ୨ৎ",
    font=("Georgia", 18, "bold"),
    bg="#e8c7cc",
    fg="#6e1f34"
)
title.pack(pady=12)

subtitle = tk.Label(
    root,
    text="⋆｡‧˚ʚ Welcome love ɞ˚‧｡⋆",
    font=("Helvetica", 10, "italic"),
    bg="#e8c7cc",
    fg="#555555"
)
subtitle.pack()

# ---------------- TABS ----------------

style = ttk.Style()
style.theme_use("default")
style.configure(
    "Pink.TNotebook",
    background="#e8c7cc",
    borderwidth=0,
)
style.configure(
    "Pink.TNotebook.Tab",
    background="#f2d8dc",
    foreground="#6e1f34",
    font=("Helvetica", 11, "bold"),
    padding=[16, 8],
)
style.map(
    "Pink.TNotebook.Tab",
    background=[("selected", "#b56576")],
    foreground=[("selected", "white")],
)

notebook = ttk.Notebook(root, style="Pink.TNotebook")
notebook.pack(padx=15, pady=(0, 10), fill="both", expand=True)

# ---------------- CARD (mood / playlist tab) ----------------
card = tk.Frame(notebook, bg="#f9ecee")
notebook.add(card, text="♡ playlist")

# ---------------- DIARY TAB ----------------
diary_tab = tk.Frame(notebook, bg="#f9ecee")
notebook.add(diary_tab, text="✎ diary")

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

# ---------------- PLAYLIST ----------------
playlist_label = tk.Label(
    card,
    text="♡ Recommended Songs ♡",
    font=("Helvetica", 11, "bold"),
    bg="#f9ecee",
    fg="#6e1f34"
)
playlist_label.pack(pady=10)

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
    text="୨ৎ choose a song ୨ৎ",
    font=("Helvetica", 11, "bold"),
    bg="#f9ecee",
    fg="#6e1f34",
    justify="center"
)
player_display.pack(pady=20)

# ---------------- FUNCTIONS ----------------
def get_music():
    global current_playlist, current_song_path, current_index
    mood = entry.get().lower().strip()
    playlist_box.delete(0, tk.END)

    if mood in music_db and music_db[mood]:
        mood_key = mood
    else:
       
        non_empty_moods = [m for m, songs in music_db.items() if songs]
        mood_key = random.choice(non_empty_moods)

    current_playlist = random.sample(music_db[mood_key], len(music_db[mood_key]))
    current_index = 0

    for song_name, song_path in current_playlist:
        playlist_box.insert(tk.END, f"♡ {song_name}")

    if current_playlist:
        current_song_path = current_playlist[0][1]
        player_display.config(text=f"୨ৎ {current_playlist[0][0]} ୨ৎ")
        playlist_box.selection_clear(0, tk.END)
        playlist_box.selection_set(0)


def play_index(index):
    """Play the song at `index` in current_playlist and start the watcher
    that auto-advances to the next song when this one finishes."""
    global current_song_path, current_index, is_paused

    if not current_playlist:
        return

    index = index % len(current_playlist)  # wrap around to start after the last song
    current_index = index
    song_name, song_path = current_playlist[index]
    current_song_path = song_path
    is_paused = False

    player_display.config(text=f"୨ৎ {song_name} ୨ৎ")
    playlist_box.selection_clear(0, tk.END)
    playlist_box.selection_set(index)
    playlist_box.see(index)

    if os.path.exists(song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        check_for_song_end()
    else:
        player_display.config(text=f"୨ৎ missing file: {song_name} ୨ৎ")


def check_for_song_end():
    """Poll pygame every 500ms. pygame doesn't have a built-in 'song
    finished' event for this kind of setup, so we just check get_busy()
    repeatedly. If the song stopped AND we're not paused, advance."""
    global autoplay_job
    autoplay_job = root.after(500, _check_for_song_end_tick)


def _check_for_song_end_tick():
    global autoplay_job
    if is_paused:
        
        autoplay_job = root.after(500, _check_for_song_end_tick)
        return

    if pygame.mixer.music.get_busy():
        
        autoplay_job = root.after(500, _check_for_song_end_tick)
    else:
        
        if current_playlist:
            play_index(current_index + 1)


def play_song():
    global is_paused
    if not current_playlist:
        return
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
        check_for_song_end()
    else:
        play_index(current_index)


def pause_song():
    global is_paused
    pygame.mixer.music.pause()
    is_paused = True


def stop_song():
    global is_paused, autoplay_job
    pygame.mixer.music.stop()
    is_paused = False
    if autoplay_job is not None:
        root.after_cancel(autoplay_job)
        autoplay_job = None


def select_song(event):
    selected = playlist_box.curselection()
    if selected:
        play_index(selected[0])


playlist_box.bind("<<ListboxSelect>>", select_song)

# ---------------- BUTTON ----------------
button = tk.Button(
    card,
    text="♡ get playlist ♡",
    command=get_music,
    font=("Helvetica", 11, "bold"),
    bg="#b56576",
    fg="white",
    activebackground="#8f3d56",
    activeforeground="white",
    bd=0,
    padx=20,
    pady=10
)
button.pack(pady=15)

# ---------------- CUTE CONTROLS ----------------
controls = tk.Frame(card, bg="#f9ecee")
controls.pack(pady=15)

play_btn = tk.Button(
    controls,
    text="▶ play",
    command=play_song,
    font=("Helvetica", 10, "bold"),
    bg="#d98ca1",
    fg="white",
    activebackground="#b56576",
    bd=0,
    padx=15,
    pady=8
)
play_btn.pack(side="left", padx=5)

pause_btn = tk.Button(
    controls,
    text="❚❚ pause",
    command=pause_song,
    font=("Helvetica", 10, "bold"),
    bg="#d98ca1",
    fg="white",
    activebackground="#b56576",
    bd=0,
    padx=15,
    pady=8
)
pause_btn.pack(side="left", padx=5)

stop_btn = tk.Button(
    controls,
    text="■ stop",
    command=stop_song,
    font=("Helvetica", 10, "bold"),
    bg="#d98ca1",
    fg="white",
    activebackground="#b56576",
    bd=0,
    padx=15,
    pady=8
)
stop_btn.pack(side="left", padx=5)

# ================== DIARY TAB CONTENTS ==================

diary_title = tk.Label(
    diary_tab,
    text="♡ Today's Note ♡",
    font=("Helvetica", 12, "bold"),
    bg="#f9ecee",
    fg="#6e1f34"
)
diary_title.pack(pady=(20, 10))

diary_text = tk.Text(
    diary_tab,
    width=40,
    height=5,
    font=("Helvetica", 11),
    bg="#f2d8dc",
    fg="#555555",
    bd=0,
    wrap="word",
    padx=10,
    pady=10
)
diary_text.pack(padx=20)


def save_entry():
    """Grab whatever's typed in the note box, pair it with today's date
    and whatever mood/playlist is currently loaded, and append it to the
    JSON file on disk so it's still there next time the app opens."""
    note = diary_text.get("1.0", "end").strip()
    if not note:
        return  # nothing typed, nothing to save

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        "mood": entry_box_value(),
        "note": note,
    }
    diary_entries.insert(0, entry)  # newest first
    save_diary(diary_entries)

    diary_text.delete("1.0", "end")
    refresh_entry_list()


def entry_box_value():
    """Whatever mood word is currently in the mood entry box on the
    playlist tab, so each diary note remembers what mood it was written
    under. Falls back to 'unspecified' if nothing was typed there."""
    typed = entry.get().strip()
    return typed if typed else "unspecified"


save_note_btn = tk.Button(
    diary_tab,
    text="♡ save note ♡",
    command=save_entry,
    font=("Helvetica", 11, "bold"),
    bg="#b56576",
    fg="white",
    activebackground="#8f3d56",
    activeforeground="white",
    bd=0,
    padx=20,
    pady=8
)
save_note_btn.pack(pady=12)

past_label = tk.Label(
    diary_tab,
    text="♡ Past Entries ♡",
    font=("Helvetica", 11, "bold"),
    bg="#f9ecee",
    fg="#6e1f34"
)
past_label.pack(pady=(10, 5))

diary_list_frame = tk.Frame(diary_tab, bg="#f9ecee")
diary_list_frame.pack(padx=20, pady=(0, 10), fill="both", expand=True)

diary_scrollbar = tk.Scrollbar(diary_list_frame)
diary_scrollbar.pack(side="right", fill="y")

# A Text widget (read-only) is used instead of a Listbox here so each
# entry can wrap across multiple lines (date + mood + note) cleanly.
diary_list = tk.Text(
    diary_list_frame,
    width=44,
    height=10,
    yscrollcommand=diary_scrollbar.set,
    font=("Helvetica", 9),
    bg="#f2d8dc",
    fg="#555555",
    bd=0,
    wrap="word",
    padx=8,
    pady=8,
    state="disabled"  # read-only, user shouldn't type directly into the list
)
diary_list.pack(fill="both", expand=True)
diary_scrollbar.config(command=diary_list.yview)


def refresh_entry_list():
    """Redraw the past-entries box from diary_entries. Called on startup
    and right after saving a new note."""
    diary_list.config(state="normal")
    diary_list.delete("1.0", "end")

    if not diary_entries:
        diary_list.insert("end", "no entries yet — write your first note above ♡")
    else:
        for e in diary_entries:
            diary_list.insert(
                "end",
                f"♡ {e['date']}  ·  mood: {e['mood']}\n{e['note']}\n\n"
            )

    diary_list.config(state="disabled")


refresh_entry_list()

# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    text="By Purva ♡",
    font=("Helvetica", 9, "italic"),
    bg="#e8c7cc",
    fg="#555555"
)
footer.pack(pady=10)

# ---------------- CLEAN SHUTDOWN ----------------
def on_close():
    """Make sure music + pygame fully stop when the window is closed,
    instead of leaving an orphaned process playing audio in the background."""
    global autoplay_job
    if autoplay_job is not None:
        root.after_cancel(autoplay_job)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
