lessons = [
    {
        "lessonRequestId": "LR1",
        "duration": 1,
        "potentialEarnings": 100,
        "availableDays": ["monday", "wednesday"]
    },
    {
        "lessonRequestId": "LR2",
        "duration": 2,
        "potentialEarnings": 50,
        "availableDays": ["monday"]
    },
    {
        "lessonRequestId": "LR3",
        "duration": 12,
        "potentialEarnings": 1000,
        "availableDays": ["wednesday"]
    },
    {
        "lessonRequestId": "LR4",
        "duration": 13,
        "potentialEarnings": 10000,
        "availableDays": ["sunday"]
    }
]

# Create a list of available days and their hours
available_hours = {
    "monday": 12,
    "tuesday": 12,
    "wednesday": 12,
    "thursday": 12,
    "friday": 12,
    "saturday": 12,
    "sunday": 12
}

# Initialize a dictionary to store the maximum earnings for each day and remaining hours
dp = {day: {hours: 0 for hours in range(available_hours[day] + 1)} for day in available_hours}

# Fill the DP dictionary
for lesson in lessons:
    for day in lesson["availableDays"]:
        for hours in range(available_hours[day], lesson["duration"] - 1, -1):
            dp[day][hours] = max(dp[day][hours], dp[day][hours - lesson["duration"]] + lesson["potentialEarnings"])

# Reconstruct the optimal solution
optimal_lessons = []
day = "sunday"  # Start with any day
remaining_hours = available_hours[day]

for lesson in reversed(lessons):
    if remaining_hours >= lesson["duration"] and dp[day][remaining_hours] == dp[day][remaining_hours - lesson["duration"]] + lesson["potentialEarnings"]:
        optimal_lessons.append(lesson)
        day = [d for d in lesson["availableDays"] if d != day][0]
        remaining_hours -= lesson["duration"]

# Print the optimal lessons and their potential earnings
total_earnings = sum(lesson["potentialEarnings"] for lesson in optimal_lessons)
for lesson in optimal_lessons:
    print(f"Lesson {lesson['lessonRequestId']} - Duration: {lesson['duration']} hours, Earnings: ${lesson['potentialEarnings']}")
print(f"Total Earnings: ${total_earnings}")
