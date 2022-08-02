import AOTdb as aot


def get_series(keywords):
    if "what" in keywords and ("plot" in keywords or "synopsis" in keywords):
        return aot.Series["Plot"]
    if ("what" in keywords and "manga" in keywords) or ("when" in keywords and "published" in keywords):
        return aot.Series["Manga"]
    if ("what" in keywords and (("attack" in keywords and "on" in keywords and "titan" in keywords)
                                or "aot" in keywords)) or ("when" in keywords and "air" in keywords):
        return aot.Series["AOT"]
    if ("episodes" in keywords and "season" in keywords and "1" in keywords) or \
            ("episodes" in keywords and "season" in keywords and "one" in keywords):
        return aot.Series["Season 1"]
    elif ("episodes" in keywords and "season" in keywords and "2" in keywords) or \
            ("episodes" in keywords and "season" in keywords and "two" in keywords):
        return aot.Series["Season 2"]
    elif ("episodes" in keywords and "season" in keywords and "3" in keywords) or \
            ("episodes" in keywords and "season" in keywords and "three" in keywords):
        return aot.Series["Season 3"]
    elif ("episodes" in keywords and "season" in keywords and "4" in keywords) or \
            ("episodes" in keywords and "season" in keywords and "four" in keywords):
        return aot.Series["Season 4"]
    elif "who" in keywords and (("hajime" in keywords) or ("isayama" in keywords)):
        return aot.Series["Isayama"]

    return "Sorry, I didn't understand what you meant. Either your inquiry is not related the anime or is not\n" \
           "yet in my database! Try asking me something else about the series!\n" \
           "E.g. What is Attack on Titan?"


def get_character(keywords):
    if "who" in keywords:
        if "eren" in keywords:
            return aot.Characters["Eren"]
        elif "mikasa" in keywords:
            return aot.Characters["Mikasa"]
        elif "armin" in keywords:
            return aot.Characters["Armin"]
        elif "levi" in keywords:
            return aot.Characters["Levi"]
        elif "erwin" in keywords:
            return aot.Characters["Erwin"]
        elif "hange" in keywords:
            return aot.Characters["Hange"]
        elif "jean" in keywords:
            return aot.Characters["Jean"]
        elif "conny" in keywords:
            return aot.Characters["Conny"]
        elif "sasha" in keywords:
            return aot.Characters["Sasha"]
        elif "historia" in keywords:
            return aot.Characters["Historia"]
        elif "ymir" in keywords:
            return aot.Characters["Ymir"]
        elif "reiner" in keywords:
            return aot.Characters["Reiner"]
        elif "bertholdt" in keywords:
            return aot.Characters["Bertholdt"]
        elif "annie" in keywords:
            return aot.Characters["Annie"]
        elif "zeke" in keywords:
            return aot.Characters["Zeke"]

    return "Sorry, I didn't understand what you meant. Either your inquiry is not related the anime or is not\n" \
           "yet in my database! Try asking me something else about the series!\n" \
           "E.g. Who is Eren Jaeger?"


def get_titan(keywords):
    if "what" in keywords or "who" in keywords:
        if "nine" in keywords and ("titan" in keywords or "titans" in keywords):
            return aot.Titans["Nine Titans"]
        elif "founding" in keywords and "titan" in keywords:
            return aot.Titans["Founding"]
        elif "attack" in keywords and "titan" in keywords:
            return aot.Titans["Attack"]
        elif "colossal" in keywords and "titan" in keywords:
            return aot.Titans["Colossal"]
        elif "armored" in keywords and "titan" in keywords:
            return aot.Titans["Armored"]
        elif "female" in keywords and "titan" in keywords:
            return aot.Titans["Female"]
        elif "beast" in keywords and "titan" in keywords:
            return aot.Titans["Beast"]
        elif "jaw" in keywords and "titan" in keywords:
            return aot.Titans["Jaw"]
        elif "cart" in keywords and "titan" in keywords:
            return aot.Titans["Cart"]
        elif "war" in keywords and "hammer" in keywords and "titan" in keywords:
            return aot.Titans["War Hammer"]
        elif "titan" in keywords or "titans" in keywords:
            return aot.Titans["Titan"]

    return "Sorry, I didn't understand what you meant. Either your inquiry is not related the anime or is not\n" \
           "yet in my database! Try asking me something else about the series!\n" \
           "E.g. What is a Titan?"


def get_organization(keywords):
    if ("survey" in keywords and "corps" in keywords) or "scout" in keywords:
        return aot.Organizations["Survey Corps"]
    elif ("military" and "police") in keywords:
        return aot.Organizations["Military Police"]
    elif "garrison" in keywords:
        return aot.Organizations["Garrison"]
    elif "military" in keywords or ("three" in keywords and "branches" in keywords and "military"in keywords):
        return aot.Organizations["Military"]

    return "Sorry, I didn't understand what you meant. Either your inquiry is not related the anime or is not\n" \
           "yet in my database! Try asking me something else about the series!\n" \
           "E.g. What is the Survey Corps?"


def get_location(keywords):
    if "what" in keywords or "where" in keywords:
        if "wall" in keywords and "maria" in keywords:
            return aot.Locations["Wall Maria"]
        elif "wall" in keywords and "rose" in keywords:
            return aot.Locations["Wall Rose"]
        elif "wall" in keywords and "sina" in keywords:
            return aot.Locations["Wall Sina"]
        elif "walls" in keywords:
            return aot.Locations["Walls"]
        elif "paradis" and "island" in keywords:
            return aot.Locations["Paradis"]
        elif "marley" in keywords:
            return aot.Locations["Marley"]

    return "Sorry, I didn't understand what you meant. Either your inquiry is not related the anime or is not\n" \
           "yet in my database! Try asking me something else about the series!\n" \
           "E.g. Where is Wall Maria?"


def get_object(keywords):
    if "what" in keywords:
        if ("odm" in keywords and "gear" in keywords) or ("omni" in keywords and "directional" in keywords and
                                                          "mobility" in keywords and "gear" in keywords):
            return aot.Objects["ODM gear"]
        if "signal" in keywords and "flare" in keywords:
            return aot.Objects["Signal Flare"]

    return "Sorry, I didn't understand what you meant. Either your inquiry is not related the anime or is not\n" \
           "yet in my database! Try asking me something else about the series!\n" \
           "E.g. What is the omni-directional mobility gear?"


def get_bot(keywords):
    if "hi" in keywords or "hello" in keywords:
        return aot.Bot["Greeting"]
    elif "how" in keywords and "are" in keywords and "you" in keywords:
        return aot.Bot["Greeting2"]
    elif (("who" in keywords or "what" in keywords) and "are" in keywords and "you" in keywords) or ("what" in keywords                                                                                 and "your" in keywords
                                                                                                     and "name" in keywords):
        return aot.Bot["Intro"]
    elif "tell" in keywords and "me" in keywords and "joke" in keywords:
        return aot.Bot["Joke"]
    elif "are" in keywords and "you" in keywords and "human" in keywords:
        return aot.Bot["Robot"]
    elif "show" in keywords and "me" in keywords and ("art" in keywords or "artwork" in keywords):
        return aot.Bot["Art"]

    return "Sorry I didn't understand that. Try talking to me about something else or asking a question about the series!"

