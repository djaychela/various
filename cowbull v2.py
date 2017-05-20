import random


def remove_one_reference(letter_to_remove, target):
    target_letter_index = 0
    for target_letter in target:
        if target[target_letter_index] == letter_to_remove:
            target[target_letter_index] = 'x'
            return target
        target_letter_index += 1
    return target

# def remove_one_reference(letter_to_remove, target):
#     for i in range(0,len(target)):
#         if target[i] == letter_to_remove:
#             target[i] = 'x'
#             return target
#     return target


def check_cowbull(target, guess):
    cows = 0
    bulls = 0
    guess_index = 0
    # check for cows
    for guess_letter in guess:
        guess_index += 1
        target_index = 0
        for target_letter in target:
            target_index += 1
            if guess_letter == target_letter and guess_index == target_index:
                cows += 1
                target = remove_one_reference(guess_letter, target)
                break

    # check for bulls
    for guess_letter in guess:
        for target_letter in target:
            if guess_letter == target_letter:
                bulls += 1
                target = remove_one_reference(guess_letter, target)
                break
    return cows, bulls


def main():
    attempts = 0
    goal = random.randint(1000, 9999)
    goal_text = str(goal)
    goal = list(goal_text)
    while True:
        user_guess = input("Enter your 4-digit guess: ")
        user_guess = list(user_guess)
        attempts += 1
        goal_copy = goal.copy()
        cows, bulls = check_cowbull(goal_copy, user_guess)
        print("You scored {} cows and {} bulls.".format(cows, bulls))
        if cows == 4:
            print("Well done, you won!  The number was {}.  It took {} attempts.".format(goal_text, attempts))
            break


if __name__ == '__main__':
    main()
