import os

FILE_NAME = "study_log.txt"
sessions = []

def classify_session(duration):
    if duration < 30:
        return "Short"
    elif duration <= 90:
        return "Medium"
    else:
        return "Long"

def add_session():
    print("\n--- Add a Study Session ---")
    subject = input("Enter subject name: ").strip()
    topic = input("Enter topic covered: ").strip()
    date_label = input("Enter date / day label: ").strip()
    while True:
        try:
            duration = float(input("Enter duration in minutes: ").strip())
            if duration <= 0:
                print("Error: Duration must be positive.")
                continue
            break
        except ValueError:
            print("Error: Enter a valid number.")
    sessions.append({"subject": subject, "topic": topic, "date": date_label, "duration": duration})
    print(f"Added! Classified as: {classify_session(duration)}")

def view_sessions():
    print("\n--- All Study Sessions ---")
    if not sessions:
        print("No sessions yet.")
        return
    print(f"{'No.':<4} {'Subject':<15} {'Topic':<20} {'Date':<15} {'Duration':<10} {'Class':<8}")
    print("-" * 80)
    for i, s in enumerate(sessions, 1):
        print(f"{i:<4} {s['subject']:<15} {s['topic']:<20} {s['date']:<15} {s['duration']:<10} {classify_session(s['duration']):<8}")

def search_by_subject(subject=None):
    if subject is None:
        subject = input("\nEnter subject to search: ").strip()
    found = [s for s in sessions if s['subject'].lower() == subject.lower()]
    if not found:
        print(f"No sessions found for '{subject}'.")
        return
    total = 0
    for s in found:
        print(f"{s['subject']} | {s['topic']} | {s['date']} | {s['duration']} mins | {classify_session(s['duration'])}")
        total += s['duration']
    print(f"Total time on {subject}: {total} mins ({total/60:.2f} hours)")

def study_statistics():
    print("\n--- Study Statistics ---")
    if not sessions:
        print("No data.")
        return
    total = sum(s['duration'] for s in sessions)
    print(f"Total overall: {total/60:.2f} hours")
    per = {}
    for s in sessions:
        per[s['subject']] = per.get(s['subject'], 0) + s['duration']
    for k, v in per.items():
        print(f" {k}: {v/60:.2f} hours")
    weakest = min(per, key=per.get)
    print(f"Weakest area: {weakest}")
    longest = max(sessions, key=lambda x: x['duration'])
    print(f"Longest: {longest['subject']} - {longest['topic']} ({longest['duration']} mins)")

def save_sessions():
    with open(FILE_NAME, "w") as f:
        for s in sessions:
            f.write(f"{s['subject']}|{s['topic']}|{s['date']}|{s['duration']}\n")
    print(f"Saved to {FILE_NAME}")

def load_sessions():
    if not os.path.exists(FILE_NAME):
        return
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    sessions.append({"subject": parts[0], "topic": parts[1], "date": parts[2], "duration": float(parts[3])})
    except:
        pass

def main():
    load_sessions()
    while True:
        print("\n===== SMART STUDY PLANNER =====")
        print("1. Add a study session")
        print("2. View all sessions")
        print("3. Search sessions by subject")
        print("4. View statistics")
        print("5. Save and exit")
        c = input("Choose (1-5): ").strip()
        if c == "1":
            add_session()
        elif c == "2":
            view_sessions()
        elif c == "3":
            search_by_subject()
        elif c == "4":
            study_statistics()
        elif c == "5":
            save_sessions()
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Enter 1-5.")

if __name__ == "__main__":
    main()