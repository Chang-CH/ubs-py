def max_earnings(lessons):
    max_earnings = [0] * 13  # Initialize a list to store maximum earnings for each possible duration
    selected_lessons = [[] for _ in range(13)]  # Initialize a list to store selected lessons for each duration

    for lesson in lessons:
        for duration in range(12, lesson["duration"] - 1, -1):
            # Check if adding the current lesson improves earnings
            if max_earnings[duration - lesson["duration"]] + lesson["potentialEarnings"] > max_earnings[duration]:
                max_earnings[duration] = max_earnings[duration - lesson["duration"]] + lesson["potentialEarnings"]
                selected_lessons[duration] = selected_lessons[duration - lesson["duration"]] + [lesson["lessonRequestId"]]

    return max_earnings[12], selected_lessons[12]

lessons = [
    {
        "lessonRequestId": "LR1",
        "duration": 1,
        "potentialEarnings": 100,
        "availableDays": ["monday", "wednesday"]
    }, {
        "lessonRequestId": "LR2",
        "duration": 2,
        "potentialEarnings": 800,
        "availableDays": ["friday"]
    }, {
        "lessonRequestId": "LR3",
        "duration": 6,
        "potentialEarnings": 800,
        "availableDays": ["friday"]
    }, {
        "lessonRequestId": "LR4",
        "duration": 12,
        "potentialEarnings": 1000,
        "availableDays": ["friday"]
    }
]

total_earnings, selected_lessons = max_earnings(lessons)
print("Maximum possible earnings:", total_earnings)
print("Selected lessons:")
for lesson_id in selected_lessons:
    print(f"- {lesson_id}")
