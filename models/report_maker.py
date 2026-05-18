# ReportMaker - makes TXT and PDF reports
import os


class ReportMaker:
    def __init__(self, student_name, subjects_rows):
        # Constructor
        self.student_name = student_name
        self.subjects = subjects_rows  # list of (name, marks)

    def _summary_text(self):
        lines = []
        lines.append("=" * 40)
        lines.append("   MAIS Study Planner - Student Report")
        lines.append("=" * 40)
        lines.append(f"Student: {self.student_name}")
        lines.append("")
        lines.append("Subjects & Marks:")
        total = 0
        for s in self.subjects:
            lines.append(f"  - {s[0]} : {s[1]}")
            total += s[1]
        avg = total / len(self.subjects) if self.subjects else 0
        lines.append("")
        lines.append(f"Average Marks: {avg:.2f}")
        lines.append("")
        lines.append("Performance:")
        for s in self.subjects:
            if s[1] < 50:
                level = "Weak"
            elif s[1] < 75:
                level = "Average"
            else:
                level = "Strong"
            lines.append(f"  {s[0]} -> {level}")
        lines.append("")
        lines.append("Keep studying. You can do it!")
        return "\n".join(lines)

    def make_txt(self, folder):
        path = os.path.join(folder, f"{self.student_name}_report.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(self._summary_text())
        return path

    def make_pdf(self, folder):
        path = os.path.join(folder, f"{self.student_name}_report.pdf")
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas
            c = canvas.Canvas(path, pagesize=A4)
            text = self._summary_text().split("\n")
            y = 800
            c.setFont("Helvetica", 12)
            for line in text:
                c.drawString(50, y, line)
                y -= 18
                if y < 50:
                    c.showPage()
                    y = 800
            c.save()
        except Exception as e:
            # Fallback: save as txt with .pdf extension is bad, so save txt
            with open(path.replace(".pdf", ".txt"), "w", encoding="utf-8") as f:
                f.write(self._summary_text())
            path = path.replace(".pdf", ".txt")
        return path
