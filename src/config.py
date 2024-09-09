import os

from dotenv import load_dotenv


load_dotenv()

PORT = int(os.getenv("HUNTFLOW_USERNAME", 8081))
