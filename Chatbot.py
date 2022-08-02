import Keywords as kw
import Response as res
import AOTdb as aot
from time import sleep

def loading():
    for _ in "...\n":
        sleep(0.35)
        print(_, end='', flush=True)

def chat():
    start = "TitanBot: Hello! {}\n" \
            "Try to ask me anything about the anime! E.g. What is Attack on Titan?\n" \
            "Type /more for more options!\n".format(aot.Bot["Intro"])
    for output in start:
        sleep(0.01)
        print(output, end='', flush=True)
    while True:
        print()
        user_input = input()
        if user_input == "/more":
            for output in "TitanBot: Type /help for more information on how to interact with me!\n" \
                                         "Type /quit to exit this program!\n":
                sleep(0.01)
                print(output, end='', flush=True)
        elif user_input == "/help":
            for output in "TitanBot: Chat with me by asking me questions about the anime series!\n" \
                          "Not getting the answers you want? Try correcting your spelling or asking more specific questions!\n":
                sleep(0.01)
                print(output, end='', flush=True)
        elif user_input == "/quit":
            for output in "TitanBot: Thanks for chatting with me or asking me questions about 'Attack on Titan'!\n":
                sleep(0.01)
                print(output, end='', flush=True)
            sleep(1)
            break
        else:
            tokens = kw.tokenize(user_input)
            key = kw.find_keywords(tokens)

            if key[0] == "series":
                loading()
                print("TitanBot: ", end='')
                for output in res.get_series(key[1]) + "\n":
                    sleep(0.01)
                    print(output, end='', flush=True)
                # print("TitanBot: " + res.get_series(key[1]))
            elif key[0] == "character":
                loading()
                print("TitanBot: ", end='')
                for output in res.get_character(key[1]) + "\n":
                    sleep(0.01)
                    print(output, end='', flush=True)
                # print("TitanBot: " + res.get_character(key[1]))
            elif key[0] == "titan":
                loading()
                print("TitanBot: ", end='')
                for output in res.get_titan(key[1]) + "\n":
                    sleep(0.01)
                    print(output, end='', flush=True)
                # print("TitanBot: " + res.get_titan(key[1]))
            elif key[0] == "organization":
                loading()
                print("TitanBot: ", end='')
                for output in res.get_organization(key[1]) + "\n":
                    sleep(0.01)
                    print(output, end='', flush=True)
                # print("TitanBot: " + res.get_organization(key[1]))
            elif key[0] == "location":
                loading()
                print("TitanBot: ", end='')
                for output in res.get_location(key[1]) + "\n":
                    sleep(0.01)
                    print(output, end='', flush=True)
                # print("TitanBot: " + res.get_location(key[1]))
            elif key[0] == "object":
                loading()
                print("TitanBot: ", end='')
                for output in res.get_object(key[1]) + "\n":
                    sleep(0.01)
                    print(output, end='', flush=True)
                # print("TitanBot: " + res.get_object(key[1]))
            elif key[0] == "bot":
                loading()
                print("TitanBot: ", end='')
                for output in res.get_bot(key[1]) + "\n":
                    sleep(0.01)
                    print(output, end='', flush=True)
                # print("TitanBot: " + res.get_bot(key[1]))


if __name__ == "__main__":
    chat()
