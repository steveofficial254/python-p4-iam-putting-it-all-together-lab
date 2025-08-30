from random import randint, choice as rc
from faker import Faker

from app import app
from models import db, User, Recipe

fake = Faker()

def create_users():
    users = []
    usernames = []

    for i in range(50):
        username = fake.first_name() + str(randint(1, 1000))
        while username in usernames:
            username = fake.first_name() + str(randint(1, 1000))
        usernames.append(username)

        user = User(
            username=username,
            image_url=fake.image_url(),
            bio=fake.sentence()
        )
        user.password_hash = fake.password()
        users.append(user)

    return users

def create_recipes():
    recipes = []

    recipe_titles = [
        "Chocolate Chip Cookies",
        "Beef Tacos",
        "Caesar Salad",
        "Chicken Alfredo",
        "Banana Bread",
        "Fish and Chips",
        "Vegetable Stir Fry",
        "Spaghetti Carbonara",
        "Apple Pie",
        "BBQ Ribs",
        "Mushroom Risotto",
        "Chicken Curry",
        "Beef Stew",
        "Pancakes",
        "Thai Pad See Ew",
        "Greek Salad",
        "Lemon Bars",
        "Pork Chops",
        "Vegetable Soup",
        "Chocolate Cake"
    ]

    for i in range(100):
        recipe = Recipe(
            title=rc(recipe_titles),
            instructions=fake.text(min_chars=50, max_chars=500),
            minutes_to_complete=randint(15, 120),
            user_id=randint(1, 50)
        )
        recipes.append(recipe)

    return recipes

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")

        # Clear existing data
        Recipe.query.delete()
        User.query.delete()

        # Create and add users
        users = create_users()
        db.session.add_all(users)
        db.session.commit()

        # Create and add recipes
        recipes = create_recipes()
        db.session.add_all(recipes)
        db.session.commit()

        print(f"Seeded {len(users)} users and {len(recipes)} recipes!")