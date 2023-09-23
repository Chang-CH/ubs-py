from flask import Blueprint, render_template, session, jsonify, request, make_response


scheduling = Blueprint("calendar-scheduling", __name__)

# def max_earnings(lessons):
#     lessons.sort(key=lambda x: x["potentialEarnings"], reverse=True)
#     days = {"monday": 0, "tuesday": 0, "wednesday": 0, "thursday": 0, "friday": 0}
#     total_earnings = 0
#     selected_lessons = {"monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": []}

#     for lesson in lessons:
#         for day in lesson["availableDays"]:
#             if lesson["duration"] + days[day] <= 12:
#                 days[day] += lesson["duration"]
#                 total_earnings += lesson["potentialEarnings"]
#                 selected_lessons[day].append(lesson["lessonRequestId"])
#                 break

#     return selected_lessons

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



@scheduling.route("/calendar-scheduling", methods=["POST"])
def getCommon():
    lessons = request.json
    selected_lessons = max_earnings(lessons)
    formatted_lessons = {day: selected_lessons[day] for day in selected_lessons if selected_lessons[day]}
    return jsonify(formatted_lessons)
