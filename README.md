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
- In the folder CriteriaAlternatives there are the Criteria with the alternatives;
- In the folder CriteriaVersusGoal there are the Goals

They're represented as matrix and the 0 means that the program has to do the reciprocal.

Input file:
- (task id, task name, duration, dependencies) i.e. 20,B,10,10

Output file:
- task id, task name, duration, ES, EF, LS, LF, float, isCritical
- 1, A, 12, 1, 12, 1, 12, 0, True
- 2, B, 6, 13, 18, 31, 36, 18, False
- 3, E, 12, 13, 24, 19, 30, 6, False
- 4, F, 18, 13, 30, 13, 30, 0, True
- 5, C, 2, 19, 20, 37, 38, 18, False
- 6, G, 10, 31, 40, 31, 40, 0, True
- 7, I, 8, 31, 38, 37, 44, 6, False
- 8, D, 8, 21, 28, 39, 46, 18, False
- 9, H, 6, 41, 46, 41, 46, 0, True
- 10, J, 2, 39, 40, 45, 46, 6, False
- 11, K, 8, 47, 54, 47, 54, 0, True

True if is on the critical path, false otherwise.

# Explanation
The first step in the AHP is to develop a graphical representation of the problem in terms of the overall goal, the criteria, and the decision alternatives.
Pairwise comparisons are fundamental building blocks of the AHP. The AHP employs an underlying scale with values from 1 to 9 to rate the relative preferences for two items, higher is the score more is preferred:
<img src="https://i.ibb.co/88VDYZ6/eliminare.png" alt="eliminare" border="0">
The first thing to do is construct a matrix for each criterion (comparing alternatives against each criterion) and one for the criterion against the final decision goal. Then we have to calculate the priority vector for each comparison matrix.
<img src="https://i.ibb.co/8Df7TQw/eliminare.png" alt="eliminare" border="0">


# Implementation
The app is implemented in Python by using Spyder and NumPy.

# Credits
Critical Path Method has been developed by [Alfonso Di Pace](https://github.com/alfonsodipace).