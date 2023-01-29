from pymongo import MongoClient


def get_database(connection_string):
    client = MongoClient(connection_string)

    # Creates the database for storing internet health data
    return client['internet_health_data']


if __name__ == "__main__":
    # Get the database
    dbname = get_database()
