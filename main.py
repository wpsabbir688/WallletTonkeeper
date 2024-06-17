import tkinter as tk
from tkinter import scrolledtext
import random
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# List of demo words
demo_words = [
    "brass", "ulture", "goose", "front", "treat", "enforce", "spread", "hood", "shoot", "behave", "aim", "sock", "devote",
    "scorpion", "agree", "shove", "van", "dentist", "educate", "fog", "movie", "wealth", "delay", "scatter", "actual",
    "unaware", "detail", "over", "grant", "donor", "whip", "hen", "coach", "smile", "gentle", "melody", "strategy", "coyote",
    "fee", "measure", "candy", "brave", "cash", "upon", "tragic", "usage", "immune", "rhythm", "mean", "track", "visa",
    "pottery", "barely", "vehicle", "olive", "magnet", "people", "spend", "route", "manual", "drive", "subject", "afford",
    "hybrid", "debris", "hawk", "arm", "parade", "disagree", "cart", "object", "confirm", "coin", "enter", "old", "material",
    "cotton", "quality", "dress", "cable", "huge", "surface", "regular", "again", "resemble", "orchard", "cute", "helmet",
    "online", "crawl", "axis", "bag", "access", "buffalo", "about", "another", "task", "voyage", "magic", "review", "reunion",
    "perfect", "tunnel", "gown", "tackle", "captain", "horror", "law", "lava", "wheel", "talent", "jazz", "fine", "life",
    "draft", "fatigue", "valley", "mimic", "stool", "almost", "rent", "vault", "decade", "penalty", "float", "view", "custom",
    "style", "slim", "dragon", "erupt", "weird", "exile", "gasp", "cinnamon", "urban", "cupboard", "please", "burst", "nurse",
    "upper", "unveil", "erode", "faculty", "antenna", "offer", "wreck", "virtual", "month", "spot", "suit", "property",
    "eternal", "explain", "calm", "oyster", "doll", "crash", "vintage", "endorse", "ethics", "garment", "salmon", "normal",
    "abandon", "symbol", "feature", "example", "odor", "cycle", "scan", "hobby", "biology", "eye", "item", "dust", "gift",
    "bone", "screen", "inquiry", "struggle", "build", "casual", "empty", "peasant", "stock", "act", "cradle", "fade", "upgrade",
    "sniff", "phone", "chair", "arena", "script", "beach", "pink", "dynami", "sunset", "ride", "embrace", "inch", "birth",
    "dose", "stove", "install", "dad", "easy", "produce", "appear", "course", "bullet", "dynamic", "effort", "diamond", "hurry",
    "trigger", "local", "choose", "pilot", "bamboo", "wrong", "husband", "wire", "maze", "attract", "vacuum", "carbon", "leg",
    "noble", "pitch", "season", "trim", "foster", "boss", "merge", "flat", "price", "lizard", "always", "tuna", "spell",
    "slight", "inform", "grid", "gospel", "soap", "identify", "benefit", "wrap", "actor", "lucky", "pear", "equip", "main",
    "chase", "casino", "act", "horn", "bag", "twelve", "useless", "mosquito", "rotate", "present", "critic", "truly", "salt",
    "energy", "term", "common", "picture", "refuse", "buddy", "expand", "shell", "margin", "current", "enact", "toilet",
    "faint", "sugar", "jaguar", "guilt", "neglect", "feel", "gossip", "hurry", "error", "best", "forget", "organ", "maple",
    "system", "danger", "flush", "lazy", "away", "success", "milk", "fashion", "process", "dwarf", "machine", "hundred", "pond",
    "chicken", "skull", "april", "rich", "vapor", "swarm", "input", "sudden", "alter", "paper", "comfort", "under", "utility",
    "vicious", "shed", "toss", "hamster", "fossil", "survey", "also", "trophy", "awesome", "permit", "cannon", "potato", "light",
    "drift", "world", "bronze", "giraffe", "match", "resist", "uphold", "vital", "ankle", "volume", "strong", "wide", "evolve",
    "awake", "arch", "humor", "label", "foil"
]

class RecoveryBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Tonkeeper Recovery Bot")

        self.frame = tk.Frame(root, bg='black')
        self.frame.pack(fill='both', expand=True)

        self.start_button = tk.Button(self.frame, text="Start", bg="green", fg="white", command=self.start)
        self.start_button.pack(side="left", padx=20, pady=20)

        self.stop_button = tk.Button(self.frame, text="Stop", bg="red", fg="white", command=self.stop)
        self.stop_button.pack(side="right", padx=20, pady=20)

        self.random_box = scrolledtext.ScrolledText(self.frame, width=50, height=10, bg='white', fg='black')
        self.random_box.pack(pady=10)

        self.valid_box = scrolledtext.ScrolledText(self.frame, width=50, height=10, bg='white', fg='black')
        self.valid_box.pack(pady=10)

        self.running = False
        self.thread = None

        self.driver = self.setup_driver()

    def setup_driver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.process_words)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()

    def process_words(self):
        while self.running:
            random_words = random.sample(demo_words, 24)
            self.random_box.insert(tk.END, ' '.join(random_words) + '\n')
            self.random_box.yview(tk.END)

            if self.check_words(random_words):
                self.valid_box.insert(tk.END, ' '.join(random_words) + '\n')
                self.valid_box.yview(tk.END)

            self.root.update()
            time.sleep(1)

    def check_words(self, words):
        self.driver.get("chrome-extension://omaabbefbmiijedngplfjmnooppbclkk/index.html#/import/import")
        try:
            textarea = self.driver.find_element(By.TAG_NAME, "textarea")
            textarea.send_keys(' '.join(words))
            textarea.send_keys(Keys.RETURN)

            time.sleep(2)  # Wait for the page to process the input

            # Placeholder: Add your logic to identify if the words are correct, e.g., checking for a specific element or message
            success_indicator = self.driver.find_elements(By.CLASS_NAME, "success-indicator")  # Update this to match the actual success indicator on the page

            return bool(success_indicator)  # Return True if the success indicator is found
        except Exception as e:
            print(f"Error checking words: {e}")
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = RecoveryBot(root)
    root.mainloop()
