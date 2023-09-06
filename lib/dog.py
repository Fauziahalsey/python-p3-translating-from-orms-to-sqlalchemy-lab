from models import Dog  # Import the Dog model from your models.py

def create_table(base):
    # Create the table for the Dog model in the database
    base.metadata.create_all()

def save(session, dog):
    # Save a Dog object to the database
    session.add(dog)
    session.commit()

def get_all(session):
    # Retrieve all Dog records from the database
    return session.query(Dog).all()

def find_by_name(session, name):
    # Find a Dog by its name in the database
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    # Find a Dog by its ID in the database
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    # Find a Dog by its name and breed in the database
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    # Update the breed of a Dog in the database
    dog.breed = breed
    session.commit()
