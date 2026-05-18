# StudyPlanner class - shows Method Overloading style, Operator Overloading
# MAIS Study Planner - Built by a 2nd Semester CIS Student

from datetime import datetime, timedelta


class StudyPlanner:
    def __init__(self, exam_date, subjects):
        # Constructor
        self.exam_date = exam_date
        self.subjects = [s.strip() for s in subjects if s.strip() != ""]
        self.weak = []
        self.strong = []

    def set_levels(self, weak_list, strong_list):
        self.weak = weak_list
        self.strong = strong_list

    def make_plan(self, plan_type="daily"):
        if plan_type == "daily":
            return self._daily_plan()
        elif plan_type == "weekly":
            return self._weekly_plan()
        else:
            return self._monthly_plan()

    def _ordered_subjects(self):
        weak_subs, avg_subs, strong_subs = [], [], []
        for s in self.subjects:
            if s in self.weak:
                weak_subs.append((s, "Weak", 2.0))
            elif s in self.strong:
                strong_subs.append((s, "Strong", 1.0))
            else:
                avg_subs.append((s, "Average", 1.5))
        return weak_subs + avg_subs + strong_subs

    def _daily_plan(self):
        plan = [
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "DAILY STUDY PLAN — MAIS STUDY PLANNER",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "Follow this schedule every day until exam day.",
            ""
        ]

        ordered = self._ordered_subjects()
        if not ordered:
            return ["No subjects added. Please enter subjects to generate a plan."]

        current_hour = 8
        current_min = 0
        session_count = 0
        plan.append("MORNING SESSION")
        plan.append("-------------------------------------------")

        for subj, level, duration in ordered:
            start_str = f"{current_hour:02d}:{current_min:02d}"
            total_mins = int(duration * 60)
            end_min = current_min + total_mins
            end_hour = current_hour + end_min // 60
            end_min = end_min % 60
            end_str = f"{end_hour:02d}:{end_min:02d}"

            if level == "Weak":
                label = f"[WEAK - Extra Focus!] {subj}"
            elif level == "Strong":
                label = f"[STRONG - Revision] {subj}"
            else:
                label = f"[AVERAGE] {subj}"

            plan.append(f"  {start_str} - {end_str}  |  {label}")
            plan.append(f"      Study for {int(duration*60)} mins. Cover all key concepts and examples.")

            current_hour = end_hour
            current_min = end_min
            session_count += 1

            if session_count % 2 == 0:
                be_min = current_min + 25
                be_hour = current_hour + be_min // 60
                be_min = be_min % 60
                plan.append(f"  {current_hour:02d}:{current_min:02d} - {be_hour:02d}:{be_min:02d}  |  ** BREAK ** Stretch, drink water, rest your eyes.")
                current_hour = be_hour
                current_min = be_min

            if current_hour >= 13 and current_hour < 14:
                plan.append("")
                plan.append("  LUNCH BREAK  (1:00 PM - 2:00 PM)")
                plan.append("      Eat well, rest 20 mins, then continue.")
                plan.append("")
                plan.append("AFTERNOON SESSION")
                plan.append("-------------------------------------------")
                current_hour = 14
                current_min = 0

        plan.append("")
        plan.append("-------------------------------------------")
        rev_end_h = current_hour + 1
        plan.append(f"  {current_hour:02d}:{current_min:02d} - {rev_end_h:02d}:{current_min:02d}  |  DAILY REVISION")
        plan.append("      Go over today's notes. Highlight weak points for tomorrow.")
        plan.append(f"  {rev_end_h:02d}:{current_min:02d} - {rev_end_h:02d}:30  |  Preview tomorrow's topics.")
        plan.append("  Sleep by 11:00 PM - your brain stores memory during sleep!")
        plan.append("-------------------------------------------")
        plan.append(f"Exam Date: {self.exam_date}  |  Stick to this plan every day!")
        return plan

    def _weekly_plan(self):
        plan = [
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "WEEKLY TIMETABLE — MAIS STUDY PLANNER",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            ""
        ]

        ordered = self._ordered_subjects()
        subs = ordered if ordered else [("No Subject", "Average", 1.5)]

        day_schedules = {
            "MONDAY":    [("08:00-10:00", True), ("10:00-10:25", "Break - stretch, water"), ("10:25-12:00", True), ("12:00-01:00", "Lunch Break"), ("01:00-03:00", True), ("03:00-03:25", "Break"), ("03:25-05:00", "Revision & notes - reflect on what you studied")],
            "TUESDAY":   [("09:00-11:00", True), ("11:00-11:25", "Break"), ("11:25-01:00", True), ("01:00-02:00", "Lunch Break"), ("02:00-04:00", True), ("04:00-04:25", "Break"), ("04:25-06:00", "Practice problems from today's topics")],
            "WEDNESDAY": [("08:30-10:30", True), ("10:30-10:55", "Break"), ("10:55-12:30", True), ("12:30-01:30", "Lunch Break"), ("01:30-03:30", True), ("03:30-03:55", "Break"), ("03:55-05:30", "Focus on weak areas - re-read difficult parts")],
            "THURSDAY":  [("08:00-10:00", True), ("10:00-10:25", "Break"), ("10:25-12:00", True), ("12:00-01:00", "Lunch Break"), ("01:00-03:00", True), ("03:00-03:25", "Break"), ("03:25-05:00", "Past paper questions practice")],
            "FRIDAY":    [("10:00-12:00", True), ("12:00-01:30", "Lunch + Jumu'ah Break"), ("01:30-03:30", True), ("03:30-03:55", "Break"), ("03:55-05:30", "Weekly revision - review all 5 days of study")],
            "SATURDAY":  [("09:00-11:00", True), ("11:00-11:25", "Break"), ("11:25-01:00", True), ("01:00-02:00", "Lunch Break"), ("02:00-04:00", "MCQ practice & past papers - timed"), ("04:00-05:00", "Rest & light reading")],
            "SUNDAY":    [("09:00-11:00", "Full revision - all subjects from this week"), ("11:00-11:25", "Break"), ("11:25-01:00", "Write summary notes per subject"), ("01:00-02:00", "Lunch Break"), ("02:00-04:00", True), ("04:00-05:00", "Relax - walk, rest, recharge for next week!")],
        }

        sub_index = 0
        for day, slots in day_schedules.items():
            plan.append(f"[ {day} ]")
            plan.append("  " + "-" * 48)
            for slot in slots:
                time_str = slot[0]
                activity = slot[1]
                if activity is True and subs:
                    sub_name, level, duration = subs[sub_index % len(subs)]
                    if level == "Weak":
                        sub_label = f"{sub_name}  [WEAK - Extra focus needed!]"
                    elif level == "Strong":
                        sub_label = f"{sub_name}  [STRONG - Revision mode]"
                    else:
                        sub_label = f"{sub_name}  [Average]"
                    plan.append(f"  {time_str}  |  Study: {sub_label}")
                    sub_index += 1
                else:
                    plan.append(f"  {time_str}  |  {activity}")
            plan.append("")

        plan.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        plan.append(f"Exam Date: {self.exam_date}")
        plan.append("Tip: Weak subjects get priority time slots. Never skip breaks - they boost retention!")
        plan.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        return plan

    def _monthly_plan(self):
        plan = [
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "MONTHLY STUDY PLAN — MAIS STUDY PLANNER",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"Exam Date: {self.exam_date}",
            ""
        ]

        ordered = self._ordered_subjects()
        subs = ordered if ordered else [("No Subject", "Average", 1.5)]

        weeks = [
            {"title": "Week 1 - Foundation & Weak Subjects", "focus": "Start with weakest subjects. Build your base from scratch.", "daily": "3-4 hours daily. Understand basics before practice.", "morning": "08:00-10:00  Study weak subject (2 hrs)", "afternoon": "02:00-04:00  Second subject study (2 hrs)", "evening": "08:00-09:00  Daily revision & notes (1 hr)", "goal": "Understand basics of ALL subjects. Make 1-page summary per chapter."},
            {"title": "Week 2 - Build & Practice", "focus": "Move to medium subjects. Start solving practice questions after theory.", "daily": "4-5 hours daily. Mix theory with problems.", "morning": "08:00-10:30  Subject study (2.5 hrs)", "afternoon": "01:30-04:00  Practice problems (2.5 hrs)", "evening": "08:00-09:30  Revision + weak spots (1.5 hrs)", "goal": "Complete all chapters. Do 20+ practice questions per subject."},
            {"title": "Week 3 - Intensive Revision", "focus": "Revise all subjects. Focus on high-weightage and difficult topics.", "daily": "5-6 hours daily. Speed + accuracy both matter now.", "morning": "07:30-10:30  Intensive study block (3 hrs)", "afternoon": "12:30-03:30  Past papers practice (3 hrs)", "evening": "08:00-09:30  Review wrong answers (1.5 hrs)", "goal": "Complete 2 full past papers. Identify remaining weak areas."},
            {"title": "Week 4 - Final Revision & Exam Ready", "focus": "Light, consistent revision. NO new topics - only revise what you know.", "daily": "3-4 hours daily. Rest and sleep are equally important now.", "morning": "08:00-10:00  Summary notes revision (2 hrs)", "afternoon": "01:00-03:00  MCQ practice + formula sheet (2 hrs)", "evening": "08:00-09:00  Flashcards + key formulas (1 hr)", "goal": "Stay calm. Revise summaries only. Sleep 8 hrs. You've got this!"},
        ]

        for i, week in enumerate(weeks):
            plan.append("=" * 42)
            plan.append(week['title'])
            plan.append("=" * 42)
            plan.append(f"Focus: {week['focus']}")
            plan.append(f"Daily Target: {week['daily']}")
            plan.append("")
            plan.append("  Sample Daily Schedule:")
            plan.append(f"  Morning   ->  {week['morning']}")
            plan.append(f"  Afternoon ->  {week['afternoon']}")
            plan.append(f"  Evening   ->  {week['evening']}")
            plan.append("")
            plan.append("  Subjects This Week:")
            start = i % len(subs)
            week_subs = (subs * 2)[start:start+2]
            for sub_name, level, duration in week_subs:
                if level == "Weak":
                    plan.append(f"    [WEAK]    {sub_name}  ->  2.5 hrs/day (HIGH priority!)")
                elif level == "Strong":
                    plan.append(f"    [STRONG]  {sub_name}  ->  1 hr/day (revision only)")
                else:
                    plan.append(f"    [AVERAGE] {sub_name}  ->  1.5 hrs/day")
            plan.append(f"  Goal: {week['goal']}")
            plan.append("")

        plan.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        plan.append("Golden Rules:")
        plan.append("  -> Sleep 7-8 hours - brain stores memory during sleep.")
        plan.append("  -> Take 25-min break every 2 hours of study.")
        plan.append("  -> Drink water - a hydrated brain performs better.")
        plan.append("  -> Revise yesterday's work before starting today's topic.")
        plan.append("  -> Consistency beats intensity. Show up every day!")
        plan.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        return plan

    # Operator Overloading: + to merge two planners
    def __add__(self, other):
        new = StudyPlanner(self.exam_date, self.subjects + other.subjects)
        return new
