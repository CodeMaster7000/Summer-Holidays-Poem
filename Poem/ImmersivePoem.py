def generate_poem(name):
    poem = f"""
    Hark, {name}! The resplendent time of year,
    Where summer holidays doth appear,
    A season bathed in warmest light,
    Where care and worries take their flight.

    Beneath the sun's celestial reign,
    We find delight, free from all restrain.
    A time for mirth and joy unbound,
    As nature's wonders are around.

    Along the shore, where waters meet,
    With glistening sands beneath our feet,
    We trace our dreams in castles grand,
    As waves caress the golden strand.

    Cool ice creams, a sweet ambrosia,
    A taste of bliss, no other could enclose ya.
    Their flavors dance upon the tongue,
    A symphony of summer, forever sung.

    In gardens blooming, colors thrive,
    Amidst the hum of bees alive.
    Where zephyrs whisper in the breeze,
    Amidst the rustling of leafy trees.

    Amidst the park, a verdant embrace,
    We gather with loved ones, face to face.
    As laughter echoes, hearts entwine,
    Memories forged, an eternal sign.

    By moonlit skies, fireflies embark,
    A spectacle divine, a dazzling spark.
    And stars above, like diamonds bright,
    Illuminate our dreams at night.

    O, the summer nights, a mystic dream,
    With crickets' song and moon's soft gleam.
    A canvas painted in indigo and gold,
    Where stories of old are gently told.

    The bonfire's glow, a radiant hue,
    As we gather 'round, the flames imbue.
    With tales and songs that never tire,
    Our spirits soar, like phoenix fire.

    So, {name}, embrace this summer's grace,
    Each moment, a cherished embrace.
    For summer holidays, a timeless reprieve,
    In hearts enshrined, forever believe.
    """

    return poem

def main():
    wants_poem = input("Wouldst thou like to savor a poem on summer holidays? (Y/N): ").upper()
    if wants_poem == "Y":
        user_name = input("Enter thy name: ")
        poem = generate_poem(user_name)
        print("\n   **An immersive poem on blissful summer**\n")
        print(poem)
    else:
        print("Verily, until we meet again!")
if __name__ == "__main__":
    main()
