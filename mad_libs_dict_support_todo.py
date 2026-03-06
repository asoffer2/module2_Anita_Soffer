# Day 1 Dictionary Mad Libs (NO nested dictionaries)
# -------------------------------------------------
# You are GIVEN: TEMPLATE, PROMPTS, RULES, state
# You must COMPLETE the TODO functions:
# 1) validate_input
# 2) collect_answers
# 3) score_answers
# 4) play_once
TEMPLATE = (
"I was waiting for the {adj1} train at {num1} o’clock when a {noun1} "
"{verb_past1} past me and shouted, “{exclaim1}!” "
"I grabbed my {noun2} and ran {num2} steps to the {noun3}."
)
# PROMPTS is a dictionary:
# key = placeholder name (must match TEMPLATE placeholders)
# value = what we ask the user to type
PROMPTS = {
"adj1": "Enter an adjective",
"num1": "Enter a number (0-23)",
"noun1": "Enter a noun",
"verb_past1": "Enter a past-tense verb",
"exclaim1": "Enter an exclamation (one word)",
"noun2": "Enter a noun",
"num2": "Enter a number (1-500)",
"noun3": "Enter a noun",
}
# RULES is a dictionary:
# key = placeholder name (only for some placeholders)
# value = a rule dictionary describing how to validate the input
# we access a dictionary within a dictionary like it is a nested loop
# For instance, to access num1's max value 23 : RULES["num1"]["max"]
# To access the value word of exclaim1 : RULES["exclaim1"]["type"]
RULES = {
"num1": {"type": "int", "min": 0, "max": 23},
"num2": {"type": "int", "min": 1, "max": 500},
"exclaim1": {"type": "word"},
}
# state tracks information across multiple plays
state = {
"plays_total": 0,
"best_score": None,
"total_score": 0,
"score": 0
}
def validate_input(key, raw, rules):
    """
        Validate ONE user entry.
        Parameters:
        key : the placeholder key (example: "num1" or "noun2")
        raw : the user's raw input (a string)
        rules : the RULES dictionary
        Return:
        (ok, value, error_message)
        ok = True/False
        value = cleaned value (string or int) if ok is True, else None
        error_message = "" if ok is True, else a message to show the user
        Rules supported:
        - If key NOT in rules: accept any non-empty string (strip whitespace)
        - {"type":"int", "min":..., "max":...}
        - {"type":"word"} -> one word only (no spaces), not empty
        How to use the RULES dictionary :
        - we access a dictionary within a dictionary like it is a nested loop
        - For instance, to access num1's max value 23 : RULES["num1"]["max"]
        - To access the value word of exclaim1 : RULES["exclaim1"]["type"]
    """
    stripped_input = raw.strip() # stripping side whitespace

    # TODO 1: get the rule for this key using rules.get(key)
    rule = rules.get(key, None) # default value set to prevent error

    # TODO 2: if there is NO rule, return (True, stripped_input, "")
    if rule is None:
        return True, stripped_input, ""

    # TODO 3: if type == "int":
    # - try to convert stripped_input to int
    if rules[key]["type"] == "int":
        try: # try to convert stripped_input to int
            int_raw = int(stripped_input)
        except ValueError: # if it fails
            return False, None, "Please enter a valid integer"
        if "min" in rules[key] and "max" in rules[key]: # enforce min/max if present
            my_min = rules[key]["min"]
            my_max = rules[key]["max"]
            if int_raw < my_min or int_raw > my_max:
                return False, None, "Please enter a valid integer"
        return True, int_raw, ""

    # TODO 4: if type == "word":
    if rules[key]["type"] == "word":
        if stripped_input == "":  # return None for an empty answer
            return False, None, "Empty answer provided"
        for letter in stripped_input:  # return none if there is any kind of whitespace character
            if letter.isspace():
                return False, None, "Please enter only one word"
        return True, stripped_input, ""

    # TODO 5: if unknown rule type, treat it like a normal string
    if rules[key]["type"] != "int" and rules[key]["type"] != "word":
        return True, stripped_input, ""
    return False, None, "TODO: implement validate_input"


def collect_answers(prompts, rules):
    """
        Build the answers dictionary.
        prompts: PROMPTS dict (placeholder -> prompt)
        rules : RULES dict (placeholder -> rule)
        How to use the RULES dictionary :
        - we access a dictionary within a dictionary like it is a nested loop
        - For instance, to access num1's max value 23 : RULES["num1"]["max"]
        - To access the value word of exclaim1 : RULES["exclaim1"]["type"]
        Returns:
        answers dict where:
        key = placeholder name (example: "noun1")
        value = validated user input (string or int)
        Requirements:
        - Start with answers = {}
        - Loop through prompts.items()
        - For each key:
        keep prompting until validate_input(...) returns ok=True
        - Store answers using answers[key] = value
        """
    # TODO: implement collect_answers
    # Hint: you'll want a while True loop inside the for-loop
    answers = {}
    for key, value in prompts.items():
        while True:
            answer = input(f"{value} ")
            ok, val, error_message = validate_input(key, answer, rules)
            if ok:
                answers[key] = val
                break
            else:
                print(error_message)
                continue
    return answers


def score_answers(answers, rules):
    """
    Compute a score for one round.
    Recommended scoring:
    - +1 for each answer key in answers
    - +2 bonus if that key also appears in rules
    Example:
    If answers has 8 keys, and 3 keys are in rules:
    score = 8*1 + 3*2 = 14
    How to use the RULES dictionary :
    - we access a dictionary within a dictionary like it is a nested loop
    - For instance, to access num1's max value 23 : RULES["num1"]["max"]
    - To access the value word of exclaim1 : RULES["exclaim1"]["type"]
    """
    score = 0
    # TODO: implement score_answers
    for key in answers:
        if key in rules:
            score += 2
        else:
            score += 1
    # Requirements:
    # - iterate over the dictionary keys in answers (for key in answers:)
    # - use membership test (if key in rules:)
    return score


def play_once():
    """
    Play one round of Mad Libs.
    Steps:
    1) Collect answers into a dictionary
    2) Fill TEMPLATE using TEMPLATE.format_map(answers)
    3) Score the round
    4) Update state:
    - plays_total increases by 1
    - best_score updates if this score is higher
    5) Print:
    - completed story
    - answers dict
    - score
    """
    print("\nFill in the blanks (you won't see the full story until the end!)\n")
    # TODO 1: answers = collect_answers(PROMPTS, RULES)
    answers = collect_answers(PROMPTS, RULES)
    # TODO 2: finished = TEMPLATE.format_map(answers)
    finished = TEMPLATE.format_map(answers)
    # TODO 3: score = score_answers(answers, RULES)
    score = score_answers(answers, RULES)
    # TODO 4: update state["plays_total"] and state["best_score"]
    state["plays_total"] += 1
    state["score"] += score
    if state["best_score"] is None:
        state["best_score"] = score
    else:
        if state["best_score"] < score:
            state["best_score"] = score
    # TODO 5: print the finished story + answers dict + score
    print()
    print(finished)
    print("-------------------------------------------------------------------------------------------------")
    print(answers)
    print("-------------------------------------------------------------------------------------------------")
    print(f"Score = {score}")
    print("---------------------------------------------------------------------------------------------------")


def main():
    """
    What main does:
    - Repeatedly asks the user if they want to play
    - Calls play_once() when the user says 'y'
    - Stops when the user says 'n'
    - Prints a summary using the state dictionary
    """
    print("Mad Libs ")
    # TODO (READ ONLY): This while loop keeps the program running
    user_input = ""
    while user_input != "n":
        raw_user_input = input("Do you want to play? (y/n) ")
        user_input = raw_user_input.strip().lower()
        if user_input == "y":
            play_once()
            continue
        elif user_input == "n":
            break
        else:
            print("Please enter y or n")
            continue
    print("Summary:")
    print(f"Total plays: {state["plays_total"]}")
    print(f"Best score: {state["best_score"]}")
    print(f"Total score: {state["score"]}")

    # until the user chooses to stop.
    # TODO (READ ONLY): Get user choice and normalize it
    # TODO (READ ONLY): Stop the game loop if user types 'n'
    # TODO (READ ONLY): Play one full round if user types 'y'
    # TODO (READ ONLY): Any other input is invalid
    # TODO (READ ONLY): After the loop ends, print summary info
    # using the state dictionary.

if __name__ == "__main__":
    main()
