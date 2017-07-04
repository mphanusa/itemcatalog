from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
user1 = User(name="spotify", email="spotify@billboard.com")
session.add(user1)
session.commit()

# Create music categories and popular titles

# Popular titles for Pop
category1 = Category(name="Pop", user_id=1)

session.add(category1)
session.commit()

title1 = CategoryItem(name="Feels", user_id=1,
	artist="Calvin Harris, Pharell Williams", category=category1)

session.add(title1)
session.commit()

title2 = CategoryItem(name="Strip That Down", user_id=1,
	artist="Liam Payne, Quavo", category=category1)

session.add(title2)
session.commit()

title3 = CategoryItem(name="2U", user_id=1, artist="David Guetta, Justin Bieber", category=category1)

session.add(title3)
session.commit()

# Popular titles for Hip Hop
category2 = Category(name="Hip Hop", user_id=1)

session.add(category2)
session.commit()

title1 = CategoryItem(name="Signs", user_id=1, artist="Gucci Mane, Chris Brown", category=category2)

session.add(title1)
session.commit()

title2 = CategoryItem(name="Wokeuplikethis", user_id=1,  artist="Playboi Carti, Lili Uzi Vert", category=category2)

session.add(title2)
session.commit()

title3 = CategoryItem(name="Extra Luv", user_id=1, artist="Future, YG", category=category2)

session.add(title3)
session.commit()

# Titles for Country
category3 = Category(name="Country", user_id=1)

session.add(category3)
session.commit()

title1 = CategoryItem(name="Rescue", user_id=1, artist="Hunter Hayes", category=category3)

session.add(title1)
session.commit()

title2 = CategoryItem(name="Nothin Like Us", user_id=1, artist="Josh Gracin", category=category3)

session.add(title2)
session.commit()

title3 = CategoryItem(name="Good Company", user_id=1, artist="Jake Owen", category=category3)

session.add(title3)
session.commit()

# Titles for Jazz
category4 = Category(name="Jazz", user_id=1)

session.add(category4)
session.commit()

title1 = CategoryItem(name="I'll Let You Know", user_id=1, artist="David Hazeltine", category=category4)

session.add(title1)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name