import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in ANY OS we find ourselves in
# Allow outside files/folders to be added to the project from the base dir


class Config():
    """
        Set Config variables for the flask app.
        Using Environment variables where available otherwise
        create the config variables if not done already.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:PASSWORD HERE@127.0.0.1:5432/car-collection'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off update messages from the sqlalchemy


    # Save this for later os.environ.get('DATABSE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')