from models import *


class Database:
    def __init__(self):
        self.db = {
            "users": [
                User(
                    name="John Doe",
                    email="johndoe123@gmail.com",
                    frequency=1,
                    categories=["Business", "Entertainment"],
                ),
                User(
                    name="Jane Smith",
                    email="janedoe234@yahoo.com",
                    frequency=7,
                    categories=["Business", "Science"],
                ),
            ],
            "summarizations": [],
            "categories": [
                Category(name="Technology", keywords=["technology"]),
                Category(name="Business", keywords=["business"]),
                Category(name="Entertainment", keywords=["entertainment"]),
                Category(name="Health", keywords=["health"]),
                Category(name="Science", keywords=["science"]),
                Category(name="Sports", keywords=["sports"]),
            ],
        }

    def get_users(self) -> list[User]:
        return self.db["users"]

    def create_user(self, user) -> None:
        self.db["users"].append(user)

    def update_user(self, user) -> None:
        for i, u in enumerate(self.db["users"]):
            if u["name"] == user["name"]:
                self.db["users"][i] = user
                break

    def delete_user(self, user) -> None:
        self.db["users"] = [u for u in self.db["users"] if u["name"] != user["name"]]

    def get_user_emails(self) -> list[str]:
        return [u["email"] for u in self.db["users"]]

    def get_user_by_email(self, email: str) -> User:
        for u in self.db["users"]:
            if u["email"] == email:
                return u

    def get_summarizations_since(self, since: int) -> list[Summarization]:
        return [s for s in self.db["summarizations"] if s.timestamp > since]

    def create_summarization(self, summarization: Summarization) -> None:
        self.db["summarizations"].append(summarization)

    def get_categories(self) -> list[Category]:
        return self.db["categories"]

    def create_category(self, category: Category) -> None:
        self.db["categories"].append(category)

    def update_category(self, category: Category) -> None:
        for i, c in enumerate(self.db["categories"]):
            if c.name == category.name:
                self.db["categories"][i] = category
                break

    def get_category_by_name(self, name: str) -> Category:
        for c in self.db["categories"]:
            if c.name == name:
                return c

    def get_summarizations_by_category(self, category: Category) -> list[Summarization]:
        return [s for s in self.db["summarizations"] if s.category == category.name]

    def get_user_categories(self, user: User) -> list[Category]:
        return [c for c in self.get_categories() if c.name in user.categories]
