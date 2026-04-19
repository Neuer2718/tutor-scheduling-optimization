from ortools.sat.python import cp_model

from data_loader import load_data
from build_model import build_schedule_model
from utils import (
    build_assignment_table,
    build_load_table,
    build_summary_table,
    export_results,
)


def main():
    data = load_data("data/raw")
    model_objects = build_schedule_model(data)

    model = model_objects["model"]

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 10

    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        print("No feasible solution found.")
        return

    print("Solution found!\n")

    schedule_df = build_assignment_table(data, model_objects, solver)
    load_df = build_load_table(data, model_objects, solver)
    summary_df = build_summary_table(data, model_objects, solver)

    print("Final Schedule")
    print(schedule_df.to_string(index=False))
    print("\nTutor Loads")
    print(load_df.to_string(index=False))
    print("\nSummary")
    print(summary_df.to_string(index=False))

    export_results(schedule_df, load_df, summary_df, "results")
    print("\nResults exported to results/ folder.")


if __name__ == "__main__":
    main()
