import random

Cardinality = 2
NumberTrials = 100
p = 0.5

TrialSequence =[] # delaring list (vector)
for TrialIndex in range(0,NumberTrials): #defining a loop
	if random.random()<p:
			TrialSequence.append(1)

	else:
			TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
	EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex)/float(NumberTrials))
print (EmpiricalDistribution)
