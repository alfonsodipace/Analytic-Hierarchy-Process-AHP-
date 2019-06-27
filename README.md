# ANALYTIC HIERARCHY PROCESS
The analytic hierarchy process (AHP) is a structured technique for organizing and analyzing complex decisions. the AHP helps decision makers find one that best suits their goal and their understanding of the problem. It provides a comprehensive and rational framework for structuring a decision problem, for representing and quantifying its elements, for relating those elements to overall goals, and for evaluating alternative solutions. Users of the AHP first decompose their decision problem into a hierarchy of more easily comprehended sub-problems, each of which can be analyzed independently. Once the hierarchy is built, the decision makers systematically evaluate its various elements by comparing them to each other two at a time. Each evaluation is made by a matrix. The AHP converts these evaluations to numerical values that can be processed and compared over the entire range of the problem.

It has been built in the context of Project Management course with the Professor Francesco Orciuoli at the University of Salerno(UNISA).

# Why use it?
The Analytic Hierarchy Process (AHP) is most useful where teams of people are working on complex problems, especially those with high stakes, involving human perceptions and judgments, whose resolutions have long-term repercussions.

Decision situations to which the AHP can be applied include:
- Choice: The selection of one alternative from a given set of alternatives, usually where there are multiple decision criteria involved;
- Ranking: Putting a set of alternatives in order from most to least desirable;
- Prioritization: Determining the relative merit of members of a set of alternatives, as opposed to selecting a single one or merely ranking them;
- Resource allocation: Apportioning resources among a set of alternatives;
- Benchmarking: Comparing the processes in one's own organization with those of other best-of-breed organizations;
- Quality management: Dealing with the multidimensional aspects of quality and quality improvement;
- Conflict resolution: Settling disputes between parties with apparently incompatible goals or positions.

# Features
Implement a Python program for:
- apply the AHP method to any domain, problem, criteria and alternatives;
- the number of criteria must be variable (not fixed);
- the number of alternatives must be variable (not fixed).


# Architecture
- assignment2.py is the program file;
- in the folder CriteriaAlternatives there are the Criteria with the alternatives;
- in the folder CriteriaVersusGoal there are the Goals;
- in Alternatives.txt there's the names of the alternatives;
- in RCIvalues.txt there are the values of the RCI.

They're represented as matrix and the 0 means that the program has to do the reciprocal.

# Explanation
The first step in the AHP is to develop a graphical representation of the problem in terms of the overall goal, the criteria, and the decision alternatives.
Pairwise comparisons are fundamental building blocks of the AHP. The AHP employs an underlying scale with values from 1 to 9 to rate the relative preferences for two items, higher is the score more is preferred:
<img src="https://i.ibb.co/88VDYZ6/eliminare.png" alt="eliminare" border="0">

The first thing to do is construct a matrix for each criterion (comparing alternatives against each criterion) and one for the criterion against the final decision goal. Then we have to calculate the priority vector for each comparison matrix.
<img src="https://i.ibb.co/8Df7TQw/eliminare.png" alt="eliminare" border="0">

We do the same for the GOAL matrix.

Example of the structure of the problem:
<img src="https://i.ibb.co/YZcxrTc/eliminare.png" alt="eliminare" border="0">

For each matrix we calculate lambdamax that is the dot product between the priority vector and the sum of elements column by column.
Then we create a matrix(called "fp") of all the priority vectors dot the matrix of the goal.

We sort fp (descending) and use the indexes to build the ranking of the alternatives against the final goal with respect to all the considered criteria.
The final decision will be the alternative whose rank is 1.

In the AHP the pairwise comparisons in a judgment matrix are considered to be adequately consistent if the corresponding consistency ratio (CR) is less than 10%. First the consistency index (CI) needs to be estimated. This is done by adding the columns in the judgment matrix and multiply the resulting vector by the vector of priorities (i.e., the approximated eigenvector) obtained earlier. RCI is fixed number that depends from the number of alternatives.

RCI from 1 to 9: 0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45

CI = (lambdamax - #alternatives) / (#alternatives -1) 

CR = CI / RCI

If CR >= 0.10 is a good idea to reconsider the values in the matrix (it is not mandatory)

# Implementation
The app is implemented in Python by using Spyder and NumPy.

# Credits
Critical Path Method has been developed by [Alfonso Di Pace](https://github.com/alfonsodipace).