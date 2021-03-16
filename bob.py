# def questions_bob(quest):
#     S = "str"
#     S1 = "Как дела?"
#     S2 = S.isupper()
#     S3 = '?'.join()
#     S4 = " "
#         if quest == S1:
#             return "Ага"
#         elif quest == S2:
#             return "Воу, остынь!"
#         elif quest == S3:
#             return "Успокойся, я знаю, что делаю!"
#         elif quest == S4:
#              return "Ну и ладненько."
#         else:
#              return("Ясно.")
# print(questions_bob())

# print(bob("Ты сегодня кушал?") == "Ага.")
# print(bob("КОГДА БУДЕТ ГОТОВА РАБОТА?") == "Успокойся, я знаю, что делаю!")
# print(bob("ИНОПЛАНЕТЯНЕ НАПАДАЮТ НА МАРС") == "Воу, остынь!")
# print(bob("ЙЦУКЕНГШЩЗВВООВОВЬЛЬСЛЬСЛ") == "Воу, остынь!")
# print(bob("    \n \t \b") == "Ну и ладненько.")
# print(bob("1, 2, 3") == "Ясно.")
# print(bob("1, 2, 3 ПОЕХАЛИ") == "Воу, остынь!")
# print(bob("Сегодня красивый закат") == "Ясно.")
# def is_uppercase(string):
#     return string == string.upper()


# def bob(quest):
#     if quest[-1] == "?":
#         if is_uppercase(quest):
#             return "Успокойся, я знаю, что делаю!"
#         else:
#             return "Ага."
#     elif is_uppercase(quest):
#         return ("Воу, остынь!")
#     else:
#         return "Ясно."


# print(bob("КОГДА БУДЕТ ГОТОВА РАБОТА?") == "Успокойся, я знаю, что делаю!")


def curry(x):
    return lambda y: lambda z: print(x + " " + y + " " + z)


def curry_one(x): return lambda y: lambda z: print(x + " " + y + " " + z)


curry("I")("love")("you")
curry_one("Je")("t'")("aime")

# two = one
# three = two

# print(two)
# print(three)
