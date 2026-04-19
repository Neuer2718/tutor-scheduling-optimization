from ortools.sat.python import cp_model


def build_schedule_model(data):
    """
    Build the tutor scheduling CP-SAT model.
    """
    model = cp_model.CpModel()

    tutors = data["tutors"]
    sessions = data["sessions"]
    max_shifts = data["max_shifts"]
    min_shifts = data["min_shifts"]
    required_tutors = data["required_tutors"]
    session_day = data["session_day"]
    availability = data["availability"]
    preferences = data["preferences"]
    sessions_df = data["sessions_df"]

    x = {}
    for t in tutors:
        for s in sessions:
            x[(t, s)] = model.NewBoolVar(f"assign_{t}_{s}")

    for t in tutors:
        for s in sessions:
            if availability.get((t, s), 0) == 0:
                model.Add(x[(t, s)] == 0)

    uncovered = {}
    for s in sessions:
        uncovered[s] = model.NewIntVar(0, required_tutors[s], f"uncovered_{s}")
        model.Add(
            sum(x[(t, s)] for t in tutors) + uncovered[s] == required_tutors[s]
        )

    for t in tutors:
        total_load = sum(x[(t, s)] for s in sessions)
        model.Add(total_load >= min_shifts[t])
        model.Add(total_load <= max_shifts[t])

    days = sessions_df["day"].unique()
    for t in tutors:
        for day in days:
            day_sessions = [s for s in sessions if session_day[s] == day]
            model.Add(sum(x[(t, s)] for s in day_sessions) <= 1)

    load = {}
    for t in tutors:
        load[t] = model.NewIntVar(0, len(sessions), f"load_{t}")
        model.Add(load[t] == sum(x[(t, s)] for s in sessions))

    max_load = model.NewIntVar(0, len(sessions), "max_load")
    min_load = model.NewIntVar(0, len(sessions), "min_load")
    model.AddMaxEquality(max_load, [load[t] for t in tutors])
    model.AddMinEquality(min_load, [load[t] for t in tutors])

    fairness_gap = model.NewIntVar(0, len(sessions), "fairness_gap")
    model.Add(fairness_gap == max_load - min_load)

    total_uncovered = sum(uncovered[s] for s in sessions)
    preference_score = sum(
        preferences.get((t, s), 0) * x[(t, s)]
        for t in tutors
        for s in sessions
    )

    model.Minimize(
        100 * total_uncovered +
        5 * fairness_gap -
        2 * preference_score
    )

    return {
        "model": model,
        "x": x,
        "uncovered": uncovered,
        "load": load,
        "max_load": max_load,
        "min_load": min_load,
        "fairness_gap": fairness_gap,
    }
