#added a second call for the get_preposiitional_prase
import random
def main ():

    def get_determiner(quantity):
        """Return a randomly chosen determiner."""
        if quantity == 1:
            words = ["a", "one", "the"]
        else:
            words = ["some", "many", "the"]
        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word
    def get_noun(quantity):
        """Return a randomly chosen noun based on the quantity."""
        if quantity == 1:
            nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        else:
            nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
        # Randomly choose and return a noun.
        noun = random.choice(nouns)
        return noun
                     
    def get_verb(quantity, tense):
        """Return a randomly chosen verb based on the quantity and tense."""
        if tense == "past":
                verbs = ["drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"]
        if tense == "future":
                verbs = ["will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"]
            
        if tense == "present":
            if quantity == 1:
                verbs = ["drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"]
            else:
                verbs = ["drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"]

        verb = random.choice(verbs)
        return verb
    
    def get_preposition():
        """Return a randomly chosen preposition
        from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
        Return: a randomly chosen preposition.
        """
        prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        preposition = random.choice(prepositions)
        return preposition
    
    def get_prepositional_phrase(quantity):
        """Return: a prepositional phrase."""
        preposition = get_preposition()
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        

        return f"{preposition} {determiner} {noun}"




    def make_sentence(quantity, tense):
        """Build and return a sentence with three words:
        a determiner, a noun, and a verb. The grammatical
        quantity of the determiner and noun will match the
        number in the quantity parameter. The grammatical
        quantity and tense of the verb will match the number
        and tense in the quantity and tense parameters.
        """
        determiner = get_determiner(quantity).capitalize()
        noun = get_noun(quantity)
        verb = get_verb(quantity, tense)
        phrase = get_prepositional_phrase(quantity)
        second_phrase = get_prepositional_phrase(quantity)
        # Return the sentence as a string.
        print(f"{determiner} {noun} {verb} {phrase} {second_phrase}.")
    
    make_sentence(1, "past")
    make_sentence(1, "present")
    make_sentence(1, "future")
    make_sentence(2, "past")
    make_sentence(2, "present")
    make_sentence(2, "future")

main()