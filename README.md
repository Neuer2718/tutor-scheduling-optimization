# OR Tutor Scheduling Starter Project

This starter project uses **Google OR-Tools CP-SAT** to assign tutors to support sessions while:
- covering as many sessions as possible,
- respecting tutor availability,
- limiting tutors to at most one session per day,
- keeping workloads reasonably balanced,
- rewarding preferred assignments.

## Why this is a good portfolio project
This is a realistic operations research scheduling model similar to employee and nurse scheduling examples documented by Google OR-Tools.

## Project structure
- `data/tutors.csv`: tutor workload limits
- `data/sessions.csv`: sessions to cover
- `data/availability.csv`: tutor-session availability and preferences
- `src/solve_schedule.py`: optimization model and solver
- `results/`: exported solution files

## Install
```bash
pip install -r requirements.txt
```

## Run
```bash
python src/solve_schedule.py
```

## Model idea
Decision variable:
- `x[tutor, session] = 1` if a tutor is assigned to a session, otherwise `0`

Objective:
- minimize uncovered sessions,
- reduce imbalance between maximum and minimum tutor load,
- reward preferred assignments.

## Good next upgrades
- Add time-based overlap constraints using actual start/end times.
- Add multi-tutor sessions.
- Add weekend/evening penalties.
- Add visualization of final assignments.
- Compare OR-Tools with a PuLP linear programming version.
