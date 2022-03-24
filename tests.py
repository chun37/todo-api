import requests

admin_key = "e61e58c61d7502778ba2c38135c100aaf9fb66ea2518893c1a0e1dbcc51c4965750c54e2a306f423742259e9dd26f3cf0ee1a63702769e18b67a6800377cbfe2"
HOST = "http://localhost:8000"


def get_authorizattion_header(token):
    return {"Authorization": f"Token {token}"}


def register_user(user_id, key):
    res = requests.post(
        HOST + "/users/",
        json={"id": user_id},
        headers=get_authorizattion_header(key),
    )
    return res.json()


def list_tasks(key):
    res = requests.get(
        HOST + "/tasks/",
        headers=get_authorizattion_header(key),
    )
    return res.json()


def create_task(content, key):
    res = requests.post(
        HOST + "/tasks/",
        json={"content": content},
        headers=get_authorizattion_header(key),
    )
    return res.json()


def update_task(id, status: int, key):
    res = requests.put(
        HOST + f"/tasks/{id}",
        json={"status": status},
        headers=get_authorizattion_header(key),
    )
    return res.json()


def main():
    user_key = "e61e58c61d7502778ba2c38135c100aaf9fb66ea2518893c1a0e1dbcc51c4965750c54e2a306f423742259e9dd26f3cf0ee1a63702769e18b67a6800377cbfe2"
    tasks = list_tasks(admin_key)
    target_task = tasks[0]
    print(target_task)
    print(update_task(target_task["id"], target_task["status"] + 1, user_key))


if __name__ == "__main__":
    main()
