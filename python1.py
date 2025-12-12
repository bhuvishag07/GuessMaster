import matplotlib.pyplot as plt

names = [s.name for s in att.students]
percentages = [s.calculate_percentage() for s in att.students]

plt.bar(names, percentages)
plt.axhline(75, color='r', linestyle='--')
plt.title("Student Attendance %")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.show()
