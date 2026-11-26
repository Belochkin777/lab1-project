import json
import sys
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    return json.loads(TASKS_FILE.read_text(encoding="utf-8"))


def save_tasks(tasks):
    TASKS_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main(args):
    if len(args) == 1 and args[0] == "list":
        tasks = load_tasks()
        if not tasks:
            print("Список задач пуст.")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")
        return 0

    if len(args) == 2 and args[0] == "add" and args[1].strip():
        tasks = load_tasks()
        tasks.append(args[1].strip())
        save_tasks(tasks)
        print("Задача добавлена.")
        return 0

    print('Использование: python app.py list | python app.py add "Текст задачи"')
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
