from bardapi import Bard
import json

bard = Bard(token='yourtokenhere')
playername = input("give me player name :")
matchname = input('give me match name :')
query = f"can u get me T = touches\nP = penalties\nA = assists\nS = scores\nPA = passes\ndelta T = play time of {playername} in the last match of {matchname} as json only to code with without any other text just json without any explanation"
answer = bard.get_answer(query)['content']
json_start = answer.find('{')
json_end = answer.rfind('}')
json_content = answer[json_start:json_end+1]
data = json.loads(json_content)
T = data.get('T')
P = data.get('P')
A = data.get('A')
S = data.get('S')
pA = data.get('PA')
t = data.get('deltaT')

if None in (T, P, A, S, pA, t):
    missing_variables = []
    if T is None:
        missing_variables.append("T")
    if P is None:
        missing_variables.append("P")
    if A is None:
        missing_variables.append("A")
    if S is None:
        missing_variables.append("S")
    if pA is None:
        missing_variables.append("pA")
    if t is None:
        missing_variables.append("t")

    print(f"Some variables are not properly defined: {', '.join(missing_variables)}")
else:
    R = ((0.1 * T) - (0.5 * P) + (0.8 * A) + (1.8 * S) + (0.3 * pA)) * 140 / t
    print("Player rating:", R)
