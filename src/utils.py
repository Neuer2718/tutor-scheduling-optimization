from pathlib import Path
import pandas as pd


def build_assignment_table(data, model_objects, solver):
    tutors = data["tutors"]
    sessions = data["sessions"]
    session_day = data["session_day"]
    preferences = data["preferences"]
    x = model_objects["x"]

    assignment_rows = []

    for s in sessions:
        assigned_any = False
        for t in tutors:
            if solver.Value(x[(t, s)]) == 1:
                assigned_any = True
                assignment_rows.append({
                    "session_id": s,
                    "day": session_day[s],
                    "tutor": t,
                    "preferred_assignment": preferences.get((t, s), 0)
                })

        if not assigned_any:
            assignment_rows.append({
                "session_id": s,
                "day": session_day[s],
                "tutor": "UNFILLED",
                "preferred_assignment": 0
            })

    return pd.DataFrame(assignment_rows)


def build_load_table(data, model_objects, solver):
    tutors = data["tutors"]
    min_shifts = data["min_shifts"]
    max_shifts = data["max_shifts"]
    load = model_objects["load"]

    rows = []
    for t in tutors:
        rows.append({
            "tutor": t,
            "assigned_sessions": solver.Value(load[t]),
            "min_shifts": min_shifts[t],
            "max_shifts": max_shifts[t]
        })

    return pd.DataFrame(rows)


def build_summary_table(data, model_objects, solver):
    tutors = data["tutors"]
    sessions = data["sessions"]
    preferences = data["preferences"]
    x = model_objects["x"]
    uncovered = model_objects["uncovered"]
    max_load = model_objects["max_load"]
    min_load = model_objects["min_load"]
    fairness_gap = model_objects["fairness_gap"]

    summary = pd.DataFrame([{
        "objective_value": solver.ObjectiveValue(),
        "total_uncovered_sessions": sum(solver.Value(uncovered[s]) for s in sessions),
        "preference_matches": sum(
            preferences.get((t, s), 0) * solver.Value(x[(t, s)])
            for t in tutors
            for s in sessions
        ),
        "max_load": solver.Value(max_load),
        "min_load": solver.Value(min_load),
        "fairness_gap": solver.Value(fairness_gap),
    }])

    return summary


def export_results(schedule_df, load_df, summary_df, results_dir="results"):
    results_path = Path(results_dir)
    results_path.mkdir(parents=True, exist_ok=True)

    schedule_df.to_csv(results_path / "final_schedule.csv", index=False)
    load_df.to_csv(results_path / "tutor_loads.csv", index=False)
    summary_df.to_csv(results_path / "summary.csv", index=False)
