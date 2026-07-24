import sqlite3
from collections import Counter, defaultdict
import random
import time

conn = sqlite3.connect('bac-database/bacap.db')
cursor = conn.cursor()
database_data = cursor.execute('''SELECT name from advancements ''')


# database_data = cursor.execute('''SELECT name from advancements WHERE name like 'a%' ''')
# database_data = cursor.execute('''SELECT name from advancements WHERE version like '%1.20%' OR version like '%1.19%' OR version like '%1.18%' OR version like '%1.17%' OR version like '%1.16%' ''')

d = database_data.fetchall()
advs = [str(adv[0]) for adv in d]

nadvs = ["".join([c.upper() for c in adv if c.lower() in "abcdefghijklmnopqrstuvwxyz0123456789"]) for adv in advs]
nsadvs = ["".join([c.upper() for c in adv if c.lower() in "abcdefghijklmnopqrstuvwxyz0123456789 "]) for adv in advs]

# Below follows a bunch of random analysis

# PRINT ALL LOADED ADVS
def printAllAdvs():
    for l in advs:
        print(l)

# LIST ALL ADVANCEMENTS WHOSE LENGTH IS X
def printAllAdvsLengthX(X: int):
    arr = [a for a in nadvs if len(a) == X]
    print(arr)
    print(len(arr))


# COUNT ALL DUPLICATE ADVS
def countDuplicates():
    advs = [a.strip() for a in advs]
    c = [(a, b) for a, b in Counter(advs).items()]
    print([cn for cn in c if cn[1] >= 2])

# COUNT ALL SINGLE LETTERS IN WORDS
def countSingleLetters():
    for a in nsadvs:
        a = a.split()
        for w in a:
            if len(w) == 1 and w != 'A' and w != 'I':
                print(" ".join(a))
                break

def advsWithRepeatedWords():
    for a in nsadvs:
        a = a.split()
        words = []
        for w in a:
            if w in words:
                print(" ".join(a))
                break
            words.append(w)

def nonTitleCaseAdvs():
    for a in advs:
        a = a.split()
        for w in a:
            if w[0] in "abcdefghijklmnopqrstuvwxyz" and len(w) > 3:
                print(" ".join(a))
                break

# Sort words by how many times they appear in adv names
def sortObscurity():
    words = defaultdict(int)
    for a in nsadvs:
        for word in a.split():
            words[word] += 1
    print(sorted([(a, b) for a, b in words.items()], key=lambda x: x[1], reverse=True)) # How many times does each word appear
    obscurity = [(a,
                  sum(words[w] for w in a.split()),
                  [(w, words[w]) for w in a.split()]
                  ) for a in nsadvs]
    obscurity.sort(key=lambda x: x[1])
    print(obscurity) # Rank advs by obscurity (words more unique to this advancement)


print(nonTitleCaseAdvs())
# o = open("Text/out.txt", "w+", encoding="UTF-8")
# for a in sorted(advs):
#     o.write(a + "\n")
#     print(a)
# o.close()
# for a in advs:
#         a = a.split()
#         for w in a[1:]:
#             if w[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and len(w) < 3:
#                 print(" ".join(a))

# for a in advs:
#     print(a)

    # if len(o[0].split()) == o[1]:
    #     print(o)

# for a in nadvs:
#     a = a.split()
#     if len(a) == 4:
#         print([(w, words[w]) for w in a])


# time.sleep(1000)

# Sort advs by length letters only
# nadvs = ["".join([c.upper() for c in adv if c.lower() in "abcdefghijklmnopqrstuvwxyz0123456789"]) for adv in advs]
# res = list(zip(ladvs, [len(l) for l in nadvs]))
# res.sort(key=lambda x: x[1])
# for l in res:
#     print(l)

#
# # Exit code 1
# print(advs[1000000])