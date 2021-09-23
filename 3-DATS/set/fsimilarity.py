"""
authors : Bhavna Singh (18134501003)
          Ritik Pal (18134501025)


input   : transition system and a state

output  : return vector which is most similar to the
		 given state
"""

import ts_set

states,events,transitions=ts_set.TransitionSystem()
def similarity(given_state):
	# vector which have to be returned
	v=[]

	# sum of all the similarity values
	sumi=0

	# calculating similarity value
	for i in states:
		intersect=len((set(i)).intersection(set(given_state)))
		union=len((set(i)).union(set(given_state)))
		sumi+=intersect/union

	# normalising similarity values
	for i in states:
		intersect=len((set(i)).intersection(set(given_state)))
		union=len((set(i)).union(set(given_state)))
		pi=intersect/union
		v.append(pi/sumi)
	# print(v)
	return v