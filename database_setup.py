import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)

	@property
	def serialize(self):
	    """Return object data in easily serializeable format"""
	    return {
	    	'id': self.id,
	        'name': self.name,
	        'email': self.email
	    }

class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
	    """Return object data in easily serializeable format"""
	    return {
	    	'id': self.id,
	        'name': self.name
	    }

class CategoryItem(Base):
	__tablename__ = 'category_item'

	name = Column(String(80), nullable = False)
	artist = Column(String(250))
	id = Column(Integer, primary_key = True)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
	    """Return object data in easily serializeable format"""
	    return {
	        'category': self.category.name,
	        'artist': self.artist,
	        'name': self.name
	    }

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)