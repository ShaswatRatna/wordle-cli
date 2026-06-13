"""
Wordle CLI
----------
Guess the hidden 5-letter word in 6 tries.
Green = correct letter, correct position.
Yellow = correct letter, wrong position.
Gray = letter not in word.

Learn: string manipulation, loops, sets, file I/O, colorama
"""

import random
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

# ── WORD LIST ─────────────────────────────────────────────────────────────────
# A curated list of common 5-letter words
WORD_LIST = [
    "apple", "brave", "chess", "drain", "ember", "flair", "gloom", "haste",
    "irony", "joust", "knack", "lemon", "mango", "noble", "orbit", "plank",
    "quest", "rider", "shine", "taunt", "ultra", "vivid", "waltz", "xenon",
    "yacht", "zebra", "abbot", "blade", "crane", "depth", "eager", "fancy",
    "ghost", "hedge", "input", "jewel", "karma", "light", "mirth", "nerve",
    "ocean", "prank", "quota", "raven", "sword", "tiger", "usher", "vigor",
    "witch", "pixel", "storm", "flame", "frost", "crisp", "brown", "black",
    "white", "green", "clear", "place", "score", "birth", "blood", "bound",
    "brain", "brick", "bride", "brief", "bring", "broad", "broke", "brook",
    "brush", "build", "built", "burst", "candy", "carry", "catch", "cause",
    "chair", "chalk", "charm", "chart", "chase", "cheap", "check", "cheek",
    "chief", "child", "china", "choir", "civic", "civil", "clamp", "clang",
    "clash", "clasp", "class", "clean", "clerk", "click", "cliff", "cling",
    "cloak", "clock", "clone", "close", "cloud", "coach", "coast", "cobra",
    "comet", "comic", "comma", "coral", "count", "court", "cover", "craft",
    "crash", "crazy", "cream", "creek", "creep", "crest", "crime", "cross",
    "crowd", "crown", "cruel", "crush", "crypt", "cubic", "curve", "cycle",
    "dance", "daisy", "dealt", "debug", "delta", "demon", "dense", "depot",
    "derby", "digit", "ditto", "dizzy", "dodge", "doing", "doubt", "dough",
    "draft", "drama", "drank", "drawl", "drawn", "dream", "dress", "dried",
    "drift", "drink", "drive", "drool", "drove", "drunk", "dryer", "dwarf",
    "dying", "eagle", "earth", "eight", "elite", "elbow", "elder", "emote",
    "empty", "enemy", "enjoy", "enter", "entry", "equal", "error", "essay",
    "event", "every", "exact", "exist", "extra", "fable", "facet", "faith",
    "false", "fatal", "fault", "feast", "fence", "fever", "fiber", "field",
    "fifth", "fifty", "fight", "final", "finer", "first", "fixed", "fjord",
    "flake", "flank", "flash", "flask", "fleet", "flesh", "flock", "flood",
    "floor", "floss", "flour", "flute", "focus", "foray", "force", "forge",
    "forte", "forum", "found", "frame", "frank", "fraud", "fresh", "front",
    "froze", "fruit", "funky", "funny", "gamma", "gauge", "giant", "given",
    "gland", "glass", "glaze", "gleam", "glide", "glint", "gloat", "globe",
    "gloss", "glove", "going", "grace", "grade", "grain", "grand", "grant",
    "graph", "grasp", "grass", "grave", "graze", "great", "greed", "greet",
    "grief", "grind", "groan", "grope", "gross", "grout", "growl", "gruel",
    "guard", "guide", "guild", "guile", "guise", "gulch", "gusto", "gypsy",
    "habit", "happy", "harsh", "hatch", "haunt", "haven", "havoc", "heart",
    "heavy", "heist", "hello", "hence", "herbs", "hinge", "hippo", "hoist",
    "homer", "honey", "honor", "hotel", "hound", "house", "hover", "human",
    "humor", "hurry", "hyper", "ideal", "image", "imply", "inbox", "index",
    "infer", "inner", "inter", "intro", "inure", "issue", "ivory", "japan",
    "joker", "judge", "juice", "juicy", "jumbo", "jumpy", "kayak", "kazoo",
    "kebab", "kneel", "knife", "knock", "known", "koala", "label", "lance",
    "large", "laser", "latch", "later", "laugh", "layer", "leach", "leaky",
    "learn", "lease", "leash", "leave", "legal", "lemon", "level", "lever",
    "limit", "linen", "liner", "liver", "llama", "local", "lodge", "logic",
    "lofty", "loose", "lover", "lower", "loyal", "lucid", "lucky", "lunar",
    "lunch", "lusty", "lying", "magic", "major", "maker", "manga", "manor",
    "maple", "march", "march", "marry", "match", "mayor", "media", "mercy",
    "merge", "merit", "merry", "messy", "metal", "meter", "might", "mimic",
    "minor", "minus", "miser", "mixed", "model", "money", "month", "moral",
    "motel", "motto", "mound", "mourn", "mouth", "movie", "muddy", "mulch",
    "music", "musty", "myrrh", "naive", "nappy", "nasty", "naval", "night",
    "ninja", "noisy", "nomad", "north", "notch", "noted", "novel", "nudge",
    "nurse", "nymph", "obese", "occur", "offer", "often", "olive", "onion",
    "onset", "opera", "optic", "order", "other", "otter", "ought", "outdo",
    "outer", "ovary", "ovoid", "owner", "ozone", "panda", "panic", "paper",
    "party", "pasta", "patch", "pause", "peace", "peach", "pearl", "pedal",
    "penny", "perch", "peril", "perky", "petty", "phase", "phone", "photo",
    "piano", "pilot", "pitch", "pizza", "place", "plain", "plane", "plant",
    "plaza", "plead", "pleat", "pluck", "plumb", "plume", "plump", "plunge",
    "plush", "point", "polar", "polka", "poppy", "porch", "posed", "pouch",
    "poult", "pound", "power", "price", "pride", "prime", "print", "prior",
    "privy", "prize", "probe", "prone", "proof", "prose", "proud", "prove",
    "prowl", "prune", "pubic", "pulse", "punch", "pupil", "purge", "pushy",
    "queen", "query", "queue", "quick", "quiet", "quirk", "quote", "rabbi",
    "racer", "radar", "radio", "rainy", "raise", "rally", "ranch", "range",
    "rapid", "ratio", "reach", "react", "ready", "realm", "rebel", "rebus",
    "recut", "reedy", "regal", "reign", "relax", "repay", "repel", "rerun",
    "reuse", "revel", "rigid", "risky", "rival", "rivet", "robot", "rocky",
    "rouge", "rough", "round", "route", "rowdy", "royal", "rugby", "ruler",
    "runny", "rusty", "sadly", "saint", "salad", "salty", "sandy", "sassy",
    "sauce", "saute", "savor", "scald", "scalp", "scaly", "scamp", "scant",
    "scare", "scarf", "scary", "scene", "scone", "scoop", "scope", "scorn",
    "scout", "scowl", "scram", "scrap", "scrub", "seize", "sense", "serum",
    "setup", "seven", "sever", "shack", "shade", "shady", "shaft", "shake",
    "shaky", "shale", "shall", "shalt", "shame", "shape", "share", "shark",
    "sharp", "shear", "sheep", "sheer", "sheet", "shelf", "shell", "shift",
    "shirt", "shock", "shore", "short", "shout", "shove", "shown", "shrug",
    "shuck", "sight", "sigma", "silly", "since", "sixth", "sixty", "sized",
    "skate", "skimp", "skull", "slain", "slang", "slash", "slate", "slave",
    "sleek", "sleep", "sleet", "slept", "slice", "slide", "slime", "slimy",
    "slosh", "sloth", "slump", "slunk", "slurp", "small", "smash", "smear",
    "smell", "smelt", "smile", "smirk", "smite", "smoke", "smoky", "snack",
    "snail", "snake", "snaky", "snare", "sneak", "sniff", "snore", "snort",
    "snowy", "soggy", "solar", "solid", "solve", "sorry", "sound", "south",
    "space", "spade", "spare", "spark", "spawn", "speak", "spear", "speck",
    "speed", "spend", "spice", "spicy", "spill", "spine", "spite", "splat",
    "split", "spoke", "spook", "spoon", "spore", "sport", "spout", "spray",
    "spree", "sprig", "spunk", "squad", "squat", "squid", "stack", "staff",
    "stage", "stain", "stair", "stake", "stale", "stall", "stamp", "stand",
    "stank", "stare", "stark", "start", "stash", "state", "stays", "steak",
    "steal", "steam", "steel", "steep", "steer", "stern", "stiff", "still",
    "sting", "stink", "stock", "stomp", "stone", "stood", "stool", "stoop",
    "store", "stork", "story", "stout", "stove", "strap", "straw", "stray",
    "strip", "strut", "stuck", "study", "stuff", "stump", "stung", "stunk",
    "stunt", "style", "sugar", "suite", "sulky", "sunny", "super", "surge",
    "swamp", "swarm", "swear", "sweat", "sweep", "sweet", "swept", "swift",
    "swill", "swine", "swipe", "swirl", "swoop", "syrup", "table", "taboo",
    "tacky", "taken", "tally", "tangy", "tapir", "tardy", "tasty", "taxon",
    "teach", "tease", "teeth", "tempo", "tense", "tenth", "tepid", "terms",
    "terse", "theft", "their", "theme", "there", "these", "thick", "thief",
    "thing", "think", "thorn", "those", "three", "threw", "throw", "thumb",
    "thump", "tiara", "tidal", "timid", "tipsy", "tired", "title", "today",
    "token", "tonal", "tonic", "topaz", "topic", "torch", "total", "touch",
    "tough", "towel", "tower", "toxic", "track", "trade", "trail", "train",
    "trait", "tramp", "trash", "trawl", "tread", "treat", "trend", "triad",
    "trial", "tribe", "trick", "tried", "tripe", "troop", "trout", "trove",
    "truce", "truck", "truly", "trump", "trunk", "truss", "trust", "truth",
    "tuber", "tulip", "tuner", "tunic", "turbo", "tutor", "twang", "tweak",
    "twirl", "twist", "tying", "udder", "ulcer", "uncle", "under", "unfit",
    "union", "unite", "unity", "until", "upper", "upset", "urban", "usage",
    "utmost", "utter", "vague", "valid", "valor", "value", "valve", "vapid",
    "vault", "vaunt", "venal", "venom", "venue", "verge", "verse", "vicar",
    "video", "villa", "viral", "virus", "visit", "visor", "vista", "vixen",
    "vocal", "vodka", "voice", "voila", "voter", "vouch", "vowel", "vulva",
    "wacky", "wader", "wafer", "wagon", "waist", "waive", "waken", "waver",
    "weary", "weave", "wedge", "weedy", "weird", "whale", "wheat", "wheel",
    "where", "which", "while", "whiff", "whine", "whirl", "whisk", "whole",
    "whose", "widen", "widow", "windy", "witch", "witty", "woman", "women",
    "world", "worry", "worse", "worst", "worth", "would", "wound", "wrath",
    "wring", "wrist", "wrote", "yearn", "yeast", "yield", "young", "youth",
    "zappy", "zesty", "zilch", "zippy", "zombi", "zonal",
]

VALID_GUESSES = set(w.lower() for w in WORD_LIST)

MAX_TRIES = 6
WORD_LEN  = 5

# ── COLOR HELPERS ─────────────────────────────────────────────────────────────
GREEN  = Back.GREEN  + Fore.WHITE + Style.BRIGHT
YELLOW = Back.YELLOW + Fore.BLACK + Style.BRIGHT
GRAY   = Back.WHITE  + Fore.BLACK
RESET  = Style.RESET_ALL


def color_tile(letter, state):
    if state == "G": return f"{GREEN} {letter.upper()} {RESET}"
    if state == "Y": return f"{YELLOW} {letter.upper()} {RESET}"
    return f"{GRAY} {letter.upper()} {RESET}"


# ── GAME LOGIC ────────────────────────────────────────────────────────────────
def evaluate_guess(guess, target):
    """
    Returns a list of states for each letter:
    G = correct position, Y = wrong position, X = not in word
    """
    result  = ["X"] * WORD_LEN
    target_remaining = list(target)

    # First pass: find greens
    for i in range(WORD_LEN):
        if guess[i] == target[i]:
            result[i] = "G"
            target_remaining[i] = None

    # Second pass: find yellows
    for i in range(WORD_LEN):
        if result[i] == "G":
            continue
        if guess[i] in target_remaining:
            result[i] = "Y"
            target_remaining[target_remaining.index(guess[i])] = None

    return result


def display_board(guesses, results):
    print()
    for i, (guess, result) in enumerate(zip(guesses, results)):
        row = "  " + "".join(color_tile(guess[j], result[j]) for j in range(WORD_LEN))
        print(row)
    # Empty rows
    for _ in range(MAX_TRIES - len(guesses)):
        print("  " + "".join(f"{GRAY}   {RESET}" for _ in range(WORD_LEN)))
    print()


def display_keyboard(guesses, results):
    """Show which letters have been used and their states."""
    letter_states = {}
    priority = {"G": 3, "Y": 2, "X": 1}

    for guess, result in zip(guesses, results):
        for letter, state in zip(guess, result):
            current = letter_states.get(letter)
            if current is None or priority[state] > priority[current]:
                letter_states[letter] = state

    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    print()
    for row in rows:
        print("  ", end="")
        for ch in row:
            state = letter_states.get(ch)
            if state == "G":   print(f"{GREEN} {ch.upper()} {RESET}", end=" ")
            elif state == "Y": print(f"{YELLOW} {ch.upper()} {RESET}", end=" ")
            elif state == "X": print(f"{GRAY} {ch.upper()} {RESET}", end=" ")
            else:              print(f" {ch.upper()} ", end=" ")
        print()
    print()


def save_score(won, tries, word):
    """Append result to a local scores file."""
    with open("wordle_scores.txt", "a") as f:
        result = f"WIN in {tries}" if won else f"LOST (word: {word})"
        f.write(f"{result}\n")


def show_stats():
    """Show win/loss stats from saved scores."""
    if not os.path.exists("wordle_scores.txt"):
        return
    with open("wordle_scores.txt") as f:
        lines = f.readlines()
    wins  = sum(1 for l in lines if l.startswith("WIN"))
    total = len(lines)
    print(f"\n  📊 Your stats: {wins} wins / {total} games played")


# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Style.BRIGHT}  🎯 WORDLE CLI{RESET}")
    print(f"  Guess the 5-letter word in {MAX_TRIES} tries.\n")
    print(f"  {GREEN} G {RESET} = Right letter, right spot")
    print(f"  {YELLOW} Y {RESET} = Right letter, wrong spot")
    print(f"  {GRAY} X {RESET} = Letter not in word\n")

    show_stats()

    target  = random.choice(WORD_LIST).lower()
    guesses = []
    results = []
    won     = False

    while len(guesses) < MAX_TRIES:
        display_board(guesses, results)
        display_keyboard(guesses, results)

        tries_left = MAX_TRIES - len(guesses)
        print(f"  Attempt {len(guesses)+1}/{MAX_TRIES} — {tries_left} left")

        guess = input("  Your guess: ").strip().lower()

        if len(guess) != WORD_LEN:
            print(f"  ⚠️  Please enter a {WORD_LEN}-letter word.\n")
            continue

        if not guess.isalpha():
            print("  ⚠️  Letters only, no numbers or symbols.\n")
            continue

        if guess not in VALID_GUESSES:
            print("  ⚠️  Not in word list. Try another word.\n")
            continue

        result = evaluate_guess(guess, target)
        guesses.append(guess)
        results.append(result)

        if all(r == "G" for r in result):
            won = True
            break

    # Final board
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Style.BRIGHT}  🎯 WORDLE CLI{RESET}\n")
    display_board(guesses, results)

    if won:
        msgs = ["🧠 Genius!", "🔥 Magnificent!", "✨ Impressive!", "👏 Splendid!", "😊 Great!", "😅 Phew!"]
        print(f"  {msgs[len(guesses)-1]} You got it in {len(guesses)}!\n")
    else:
        print(f"  😔 The word was: {Style.BRIGHT}{target.upper()}{RESET}\n")

    save_score(won, len(guesses), target)

    again = input("  Play again? (y/n): ").strip().lower()
    if again == "y":
        main()
    else:
        show_stats()
        print(f"\n  Thanks for playing! 🎉\n")


if __name__ == "__main__":
    main()
