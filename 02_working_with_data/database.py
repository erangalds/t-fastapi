# Defining the database models using SQLAlchemy
from sqlalchemy.orm import DeclarativeBase 
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Defining a base class for the models
class Base(DeclarativeBase):
    """
    Base class for all database models.
    This class uses SQLAlchemy's DeclarativeBase to define the base for all models.
    """
    pass

# Defining the User model
class User(Base):
    """
    User model representing a user in the database.
    """
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

# Defining the database connection string
DATABASE_URL = "sqlite:///./fastapi-sqlalchemy.db"
# This is a SQLite database file located in the current directory.
# You can change this to connect to a different database by modifying the URL.
# Example: For PostgreSQL, it would be "postgresql://user:password@localhost/dbname"
# Example: For MySQL, it would be "mysql+pymysql://user:password@localhost/dbname"

# Creating the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# The connect_args={"check_same_thread": False} is used for SQLite to allow multiple threads to access the database.
# Creating the database tables
Base.metadata.create_all(bind=engine)
# Now we have finished defining the database abstration. 

# Setting the Database Connection
# Database connection is managed using Sessions. A session is a workspace for your database operations.
# We can add new records, query existing records, update records, and delete records using sessions.
# Each session is bound to a single database connection. 
# Creating a session factory. With this factory, we can create new sessions as needed.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



