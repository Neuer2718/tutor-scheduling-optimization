# Tutor Scheduling Optimization

A Python-based operations research project that uses **Google OR-Tools CP-SAT** to assign tutors to academic support sessions while balancing staffing needs, tutor availability, workload fairness, and scheduling preferences.

## Project Overview

This project models a real-world **workforce scheduling problem** in a university setting. The goal is to assign tutors to sessions in a way that:

- covers as many sessions as possible,
- respects tutor availability,
- limits overload,
- balances assignments across tutors,
- rewards preferred matches when possible.

This project is designed as a portfolio piece for data analyst, business analytics, and operations research-oriented roles. It combines **Python, pandas, CSV-based data handling, and optimization modeling** into a reproducible workflow.

## Business Problem

Manual scheduling can be time-consuming and inconsistent, especially when multiple tutors have different availability windows, workload limits, and preferred session times. This project demonstrates how optimization can improve scheduling decisions by turning those rules into a mathematical model.

A scheduling model like this can be adapted for:
- tutoring centers,
- teaching assistant office hours,
- campus support staffing,
- shift scheduling in service operations,
- basic workforce planning problems.

## Objective

The optimization model aims to:

1. **Minimize uncovered sessions**
2. **Reduce workload imbalance across tutors**
3. **Reward preferred tutor-session assignments**

These goals are combined into a weighted objective function using OR-Tools CP-SAT.

## Tools Used

- **Python**
- **pandas**
- **Google OR-Tools (CP-SAT solver)**
- **Google Colab / Jupyter Notebook**
- **CSV files for input data**

## Repository Structure

```text
tutor-scheduling-optimization/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── tutors.csv
│   │   ├── sessions.csv
│   │   └── availability.csv
│   └── processed/
├── notebooks/
│   └── 01-mg-tutor-scheduling-optimization.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── build_model.py
│   ├── solve_model.py
│   └── utils.py
├── results/
│   ├── final_schedule.csv
│   ├── tutor_loads.csv
│   └── summary.csv
└── references/
    └── project-notes.md
```

## Input Data

The model uses three CSV files stored in `data/raw/`:

### `tutors.csv`
Contains tutor-level workload rules such as:
- tutor name
- minimum shifts
- maximum shifts

### `sessions.csv`
Contains session-level information such as:
- session ID
- day
- time slot
- required number of tutors

### `availability.csv`
Contains tutor-session compatibility data such as:
- tutor name
- session ID
- availability indicator
- preference indicator

## Methodology

The workflow for this project is:

1. Load CSV input data using pandas
2. Convert the data into Python dictionaries/lists for modeling
3. Define binary decision variables:
   - `x[tutor, session] = 1` if a tutor is assigned to a session
4. Add constraints:
   - unavailable tutors cannot be assigned
   - session staffing requirements must be met when possible
   - tutors must stay within min/max shift limits
   - each tutor can work at most one session per day
5. Define a weighted objective function
6. Solve the model with OR-Tools CP-SAT
7. Export results to CSV for interpretation

## Constraints Included

The current version of the model includes:

- **Availability constraints**
- **Session coverage constraints**
- **Minimum and maximum workload limits**
- **At most one session per day per tutor**
- **Fairness measurement using workload spread**
- **Preference-based assignment rewards**

## Results

The model exports the following output files into `results/`:

- **`final_schedule.csv`** — final tutor-to-session assignments
- **`tutor_loads.csv`** — number of assigned sessions per tutor
- **`summary.csv`** — objective value, uncovered sessions, fairness gap, and preference match totals

These outputs allow quick evaluation of:
- how well sessions were covered,
- whether workloads were balanced,
- whether tutor preferences were respected.

## How to Run

### Option 1: Google Colab
1. Upload the CSV files and notebook to Colab
2. Install dependencies:
   ```python
   !pip install ortools pandas
   ```
3. Run the notebook cells in order

### Option 2: Local Python Environment
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the solver script:
   ```bash
   python src/solve_model.py
   ```

## Example Use Cases

Although this project uses tutor scheduling as the example, the same framework can be adapted to:
- employee shift scheduling
- service desk staffing
- class support scheduling
- lab assistant scheduling
- resource allocation problems

## Future Improvements

Planned extensions for the project include:

- adding real start/end times
- replacing “one session per day” with **time overlap constraints**
- allowing multi-tutor sessions with different skill requirements
- adding visualization of workload balance
- comparing OR-Tools with a linear programming version in PuLP
- building a simple dashboard for schedule review

## Skills Demonstrated

This project highlights the following skills:

- optimization modeling
- structured problem solving
- Python programming
- CSV and tabular data handling
- constraint-based decision modeling
- reproducible project organization
- communicating technical work clearly

## Resume-Ready Project Description

**Tutor Scheduling Optimization | Python, pandas, OR-Tools**  
Built an operations research scheduling model to assign tutors to support sessions using Python and Google OR-Tools. Designed constraints for availability, workload limits, fairness, and preference matching, then exported optimized schedules and summary metrics for analysis.

## Author

**Mitchell Garcia**  
M.S. in Applied Mathematics, Northern Illinois University  
Interested in data analyst, business analytics, and operations research roles.

## Notes

This project is intended as a learning-focused and portfolio-ready introduction to optimization in Python. It emphasizes both technical correctness and clear project communication.
