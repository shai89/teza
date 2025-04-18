import json
from pathlib import Path
from core.models import SubmissionOut

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "submissions.json"

def save_submission(submission: SubmissionOut):
    data = []
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append(json.loads(submission.json()))

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)



def load_last_submission() -> SubmissionOut:
    if not DATA_FILE.exists():
        return None

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if data:
                return SubmissionOut(**data[-1])
        except Exception:
            return None
