# %%
def recite(start_verse, end_verse):
    days = {
        "1": "first",
        "2": "second",
        "3": "third",
        "4": "fourth",
        "5": "fifth",
        "6": "sixth",
        "7": "seventh",
        "8": "eighth",
        "9": "ninth",
        "10": "tenth",
        "11": "eleventh",
        "12": "twelfth"
    }
    presents = {
        "1": "and a Partridge in a Pear Tree.",
        "2": "two Turtle Doves, ",
        "3": "three French Hens, ",
        "4": "four Calling Birds, ",
        "5": "five Gold Rings, ",
        "6": "six Geese-a-Laying, ",
        "7": "seven Swans-a-Swimming, ",
        "8": "eight Maids-a-Milking, ",
        "9": "nine Ladies Dancing, ",
        "10": "ten Lords-a-Leaping, ",
        "11": "eleven Pipers Piping, ",
        "12": "twelve Drummers Drumming, "
    }
    answer = []
    if start_verse == end_verse:
        answer.append(
            f"On the {days[str(start_verse)]} day of Christmas my true love gave to me: ")
        if start_verse == 1:
            answer[0] += "a Partridge in a Pear Tree."
        else:
            for i in range(0, end_verse):
                answer[0] += presents[str(end_verse-i)]
    else:
        count = 0
        for i in range(start_verse, end_verse+1):
            answer.append(
                f"On the {days[str(i)]} day of Christmas my true love gave to me: ")
            if i == 1:
                answer[count] += "a Partridge in a Pear Tree."
            else:
                for j in range(0, i):
                    answer[count] += presents[str(i-j)]
            count += 1
    return answer

# %%
