def response(hey_bob):
    answer = ""
    hey_bob = hey_bob.strip()
    if (hey_bob == ""):
        answer = "Fine. Be that way!"
    elif (hey_bob[-1] == "?"):
        if (hey_bob == hey_bob.upper() and hey_bob.isupper()):
            answer = "Calm down, I know what I'm doing!"
        else:
            answer = "Sure."
    elif (hey_bob == hey_bob.upper() and hey_bob.isupper()):
        answer = "Whoa, chill out!"
    else:
        answer = "Whatever."
    return answer
