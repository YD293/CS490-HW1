import requests

url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"
data = {
    "UCID": "yd293",
    "first_name": "Yuxing",
    "last_name": "Deng",
    "github_username": "yd293",
    "discord_username": "deng1234",
    "favorite_cartoon": "Death Note",
    "favorite_language": "SQL",
    "movie_or_game_or_book": "God of War"
}
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
