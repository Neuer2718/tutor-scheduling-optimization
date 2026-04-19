from pathlib import Path
import pandas as pd


def load_data(data_dir="data/raw"):
    """
    Load CSV files and return both DataFrames and Python structures.
    """
    data_path = Path(data_dir)

    tutors_df = pd.read_csv(data_path / "tutors.csv")
    sessions_df = pd.read_csv(data_path / "sessions.csv")
    availability_df = pd.read_csv(data_path / "availability.csv")

    tutors = tutors_df["tutor"].tolist()
    sessions = sessions_df["session_id"].tolist()

    max_shifts = dict(zip(tutors_df["tutor"], tutors_df["max_shifts"]))
    min_shifts = dict(zip(tutors_df["tutor"], tutors_df["min_shifts"]))
    required_tutors = dict(zip(sessions_df["session_id"], sessions_df["required_tutors"]))
    session_day = dict(zip(sessions_df["session_id"], sessions_df["day"]))

    availability = {}
    preferences = {}

    for _, row in availability_df.iterrows():
        key = (row["tutor"], row["session_id"])
        availability[key] = int(row["available"])
        preferences[key] = int(row["preferred"])

    return {
        "tutors_df": tutors_df,
        "sessions_df": sessions_df,
        "availability_df": availability_df,
        "tutors": tutors,
        "sessions": sessions,
        "max_shifts": max_shifts,
        "min_shifts": min_shifts,
        "required_tutors": required_tutors,
        "session_day": session_day,
        "availability": availability,
        "preferences": preferences,
    }
