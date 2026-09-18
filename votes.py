from collections import Counter

vote = input("Enter a musician: ")
votes = []
votes.append(vote)
while vote != "done":
    vote = input("Enter a musician: ")
    if vote == "done":
        break
    else:
        pass
        votes.append(vote)

votes.sort()

votesdict = dict(Counter(votes))

print("Votes \n---------------")
print(votesdict)