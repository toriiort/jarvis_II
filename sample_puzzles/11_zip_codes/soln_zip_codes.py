# TITLE: zip_codes:
# AUTHOR: Chalmer Lowe
# DESCRIPTION:
#     You are given a file with multiple lines, some of which contain
#     zip codes. You need to find the 'SUM' of all the values
#     present as part of zip codes.
#
#     What do we mean by zip codes?
#     Some lines will contain a state abbreviation followed by either
#         a five digit zip code OR a five plus four digit zip code.
#         TX 12345
#         VA 23456
#         HI 98765-4321
#         OK 87654-5432
#
#     Find all the lines with either of the following patterns
#         SS nnnnn
#         SS nnnnn-nnnn
#
#     There will be lines in the file that contain distractors, do be
#     cautious.
#
# From all the patterns, sum up the value of each of the four and
# five digit numbers.
#
# For example if the file had these sequences:
#     TX 11111       < matches SS nnnnn
#     VA 11111-2222  < matches SS nnnnn-nnnn
#     VA 222229      < doesn't match SS nnnnn
#     HI 1111-1111   < doesn't match SS nnnnn-nnnn
#     OK 22222-222   < doesn't match SS nnnnn-nnnn
#     11111-1111     < doesn't match SS nnnnn-nnnn
#     2222           < doesn't match SS nnnnn
#
# To do the math:
#     TX 11111                     = 11111
#     VA 11111-2222 > 11111 + 2222 = 13333
#     ------------------------------------
#                           answer = 24444
#
# Possible regular expression evaluators:
#     * https://regex101.com/ <<< I find this to be more fully featured
#                                 than regexpal
#     * https://www.regexpal.com/

# ==============================================================
# Put your code here:

import re
patt = re.compile(r'(\b\w{2} ((\d{5})-(\d{4})([ ]|\n+)|(\d{5})([ ]|\n+)))')

with open('output.txt') as fin:
    matches = []
    for line in fin:
        mo = patt.search(line)
        if mo:
            print(mo.group())
            matches.append(mo)

total = 0
for match in matches:
    # 2 * 3 > niner
    print(match.groups())
    if match.group(3):
        value = int(match.group(3)) + int(match.group(4))

    # 4 > fiver
    elif match.group(6):
        value = int(match.group(6))

    total += value

print('ANSWER: ', total)

# ANSWER: 914778 
