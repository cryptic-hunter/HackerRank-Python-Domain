#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

num_participants = int(input("Please enter the number of the participants : "))

score_participants = []

for i in range(0,num_participants):
    scores = int(input("Please enter the scores of the participants : "))
    appended = score_participants.append(scores)


#score_participants
#print(score_participants)

sorted_list = sorted(score_participants)
print(sorted_list)
print(max(sorted_list))

sb = set(sorted_list)
sb.remove(max(sb))
print(sb)
print(max(sb))