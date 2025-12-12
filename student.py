class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.present_count = 0
        self.total_count = 0

    def update_attendance(self, status):
        """Update present/absent count based on daily status."""
        self.total_count += 1
        if status.lower() == "present":
            self.present_count += 1

    def get_percentage(self):
        if self.total_count == 0:
            return 0
        return (self.present_count / self.total_count) * 100
