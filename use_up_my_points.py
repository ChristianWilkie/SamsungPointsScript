import requests

samsung_id = ""
samsung_webkey = ""
catalog_id = "A6757464-DFA4-11E9-9C6C-FA8B360373E4"
rewards_url = "https://www.samsungrewards.com/v1/rewards/catalog_redemption/"

request_data = {
    "profile_id": "",
    "cat_id": f"{catalog_id}",
    "id": f"{samsung_id}.{samsung_webkey}"
}

if samsung_id == "" or samsung_webkey == "":
    print("Fill out your ID and webkey! Read the README.")
    exit(1)

for i in range(20):
    response = requests.post(url=rewards_url, data=request_data)
    msg_head = response.json()["catalog_content"]["result"]["confirmation_msg_head"]
    msg_body = response.json()["catalog_content"]["result"]["confirmation_msg_body"]
    new_points = response.json()["points_content"]["new_points"]
    print(f"{msg_head} - {msg_body}. You now have {new_points} points.")
