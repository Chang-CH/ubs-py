def max_earnings(lessons):
    lessons.sort(key=lambda x: x["potentialEarnings"], reverse=True)
    days = {"monday": 0, "tuesday": 0, "wednesday": 0, "thursday": 0, "friday": 0}
    total_earnings = 0
    selected_lessons = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": []}

    for lesson in lessons:
        for day in lesson["availableDays"]:
            if lesson["duration"] + days[day] <= 12:
                days[day] += lesson["duration"]
                total_earnings += lesson["potentialEarnings"]
                selected_lessons[day].append(lesson["lessonRequestId"])
                break

    return total_earnings, selected_lessons

lessons = [
    {
        "lessonRequestId": "LR1",
        "duration": 1,
        "potentialEarnings": 100,
        "availableDays": ["monday", "wednesday"]
    }, {
        "lessonRequestId": "LR2",
        "duration": 2,
        "potentialEarnings": 50,
        "availableDays": ["monday"]
    }, {
        "lessonRequestId": "LR3",
        "duration": 12,
        "potentialEarnings": 1000,
        "availableDays": ["wednesday"]
    }, {
        "lessonRequestId": "LR4",
        "duration": 13,
        "potentialEarnings": 10000,
        "availableDays": ["friday"]
    }
]

total_earnings, selected_lessons = max_earnings(lessons)

formatted_lessons = {day: selected_lessons[day] for day in selected_lessons if selected_lessons[day]}
print("Maximum possible earnings:", total_earnings)
print("Selected lessons by day:")
print(formatted_lessons)