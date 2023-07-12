import os
import subprocess
import sys
import logging


def check_venv():
    # Check if venv directory exists
    return os.path.isdir("venv")


def setup_venv():
    # Check if venv already exists
    if check_venv():
        logging.info("Virtual environment already exists. Skipping setup.")
        return

    # Create a virtual environment
    subprocess.run([sys.executable, "-m", "venv", "venv"])

    # Activate the virtual environment
    activate_script = os.path.join("venv", "Scripts" if os.name == "nt" else "bin", "activate")
    activate_command = f"source {activate_script}" if os.name != "nt" else activate_script
    subprocess.run(activate_command, shell=True)

    # Install packages from requirements.txt
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])


def create_database():
    # Check if mysqlclient is installed
    try:
        import MySQLdb
    except ImportError:
        logging.error("mysqlclient package is not installed. Please install it.")
        return

    # Connect to MySQL and create a database if not exist
    db_connection = MySQLdb.connect(host="localhost", user="root", passwd="")
    cursor = db_connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS qwarta")
    logging.info("Database 'qwarta' created successfully.")


def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Call the setup function
    try:
        setup_venv()
        logging.info("Virtual environment setup completed successfully.")

        # Check if mysqlclient is installed and create the database
        create_database()
    except Exception as e:
        logging.error("An error occurred during virtual environment setup or database creation.")
        logging.exception(e)


if __name__ == "__main__":
    main()
