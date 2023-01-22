from pymongo import MongoClient


def get_database():
    # Connecting to local mongodb
    connection_string = "mongodb://localhost:27017"
    client = MongoClient(connection_string)

    # Creates the database for storing internet health data
    return client['internet_health_data']


if __name__ == "__main__":
    # Get the database
    dbname = get_database()
