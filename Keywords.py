import re

series = ["what", "how", "many", "when", "season", "episodes", "1", "one", "2", "two", "3", "three", "4", "four",
          "current", "final", "air", "manga", "published", "aot", "on", "plot", "synopsis"]
characters = ["who", "eren", "mikasa", "armin", "levi", "erwin", "hange", "jean", "conny", "sasha", "historia", "ymir",
              "reiner", "bertholdt", "annie", "zeke"]
titans = ["who", "what", "nine", "titan", "titans", "founding", "attack", "colossal", "armored", "female", "beast",
          "jaw", "cart", "war", "hammer", "shifter"]
organizations = ["who", "what", "military", "branches", "factions", "regiments", "regiment", "scout", "survey", "corps",
                 "police", "garrison"]
locations = ["what", "where", "wall", "walls", "maria", "rose", "sina", "paradis", "island", "marley"]
objects = ["what", "odm", "omni", "directional", "mobility", "gear", "maneuver", "signal", "flare"]
bot = ["who", "what", "hi", "hello", "how", "are", "you", "doing", "your", "name", "tell", "me", "joke", "show", "art",
       "artwork", "human"]


def tokenize(input):
    tokens = [];
    tokens += [t.lower() for t in re.findall("[a-zA-Z0-9]+", input)]
    return tokens


def find_keywords(tokens):
    keywords = []
    categories = {'series': 0, 'character': 0, 'titan': 0, 'organization': 0, 'location': 0, 'object': 0, 'bot': 0}
    for t in tokens:
        if t in series:
            categories['series'] += 1
        if t in characters:
            categories['character'] += 1
        if t in titans:
            categories['titan'] += 1
        if t in organizations:
            categories['organization'] += 1
        if t in locations:
            categories['location'] += 1
        if t in objects:
            categories['object'] += 1
        if t in bot:
            categories['bot'] += 1

    if "attack" in tokens and "on" in tokens and "titan" in tokens:
        categories['titan'] -= 2
        if categories['character'] > 1 or categories['titan'] > 1 or categories['organization'] > 1 or \
                categories['location'] > 1 or categories['object'] > 1 or categories['bot'] > 1:
            categories['series'] -= 1
        keywords += ["attack", "titan"]

    # print(categories)

    category = sorted(categories.items(), key=lambda item: item[1], reverse=True)[0][0]

    if category == "series":
        keywords += [t for t in tokens if t in series]
    elif category == "character":
        keywords += [t for t in tokens if t in characters]
    elif category == "titan":
        keywords = [t for t in tokens if t in titans]
    elif category == "organization":
        keywords += [t for t in tokens if t in organizations]
    elif category == "location":
        keywords += [t for t in tokens if t in locations]
    elif category == "object":
        keywords += [t for t in tokens if t in objects]
    elif category == "bot":
        keywords += [t for t in tokens if t in bot]

    return category, keywords


if __name__ == "__main__":
    while True:
        user_input = input()
        if user_input == "quit":
            break
        else:
            tokens = tokenize(user_input)
            key = find_keywords(tokens)
            print(key)

