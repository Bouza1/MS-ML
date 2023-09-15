import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
extractor = ConllExtractor()

def run():   
    print("Hello, I am Marvin, the simple bot.\nYou can end this conversation at any time by typing 'bye'\nAfter typing each answer, press 'enter'\nHow are you today?")

    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":            
            break
        else:
            user_input_blob = TextBlob(user_input, np_extractor=extractor)                        
            np = user_input_blob.noun_phrases                                    
            response = ""
            polarity = user_input_blob.polarity
            responses = {
                (-1, -0.5): "Oh dear, that sounds bad. ",
                (-0.5, 0): "Hmm, that's not great. ",
                (0, 0.5): "Well, that sounds positive. ",
                (0.5, 1): "Wow, that sounds great. "
            }
            response = next(v for (k_min, k_max), v in responses.items() if k_min < polarity <= k_max)

            response += f"Can you tell me more about {np[0].pluralize()}?" if len(np) != 0 else "Can you tell me more?"

            print(response)
    
    print("It was nice talking to you, goodbye!")

run()