import requests
import matplotlib.pyplot as plt

# Fetch data from the API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    # Parse JSON response
    data = response.json()

    # Extract user IDs
    user_ids = [post["userId"] for post in data]

    # Count how many posts each user has
    user_post_count = {}

    for user_id in user_ids:
        if user_id in user_post_count:
            user_post_count[user_id] += 1
        else:
            user_post_count[user_id] = 1

    # Create chart
    plt.bar(
        user_post_count.keys(),
        user_post_count.values()
    )

    plt.xlabel("User ID")
    plt.ylabel("Number of Posts")
    plt.title("Number of Posts per User")

    plt.show()

else:
    print("Failed to fetch data.")
    print("Status code:", response.status_code)