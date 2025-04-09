def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował(a) {user["posts"]} postów.")


def add_user (users_data: list)->None:
    new_name=input("podaj imię: ")
    new_location=input("podaj miejscowość: ")
    new_posts=input("podaj ilośc postów: ")
    users_data.append({"name": new_name, "location": new_location, "posts": new_posts})

    add_user(users_data)