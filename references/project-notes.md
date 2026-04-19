# Project Notes

## Project Goal
Build a tutor scheduling optimization model using Python and Google OR-Tools.

## Core Objective
Assign tutors to sessions while:
- minimizing uncovered sessions,
- balancing tutor workloads,
- rewarding preferred assignments.

## Current Constraints
- tutor must be available for assigned session
- each session must meet required staffing if possible
- each tutor must stay within min/max shift limits
- each tutor can work at most one session per day

## Future Improvements
- replace one-session-per-day rule with time overlap constraints
- add session start and end times
- add tutor skill levels
- allow some sessions to require multiple tutors
- create workload balance visualizations

## Notes on Objective Function
Current weighted objective:
- heavily penalize uncovered sessions
- moderately penalize fairness gap
- reward preferred assignments

## References
- Google OR-Tools CP-SAT documentation
- OR-Tools employee scheduling examples
