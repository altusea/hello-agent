import dotenv


def read_deepseek_api_key():
    """Read DeepSeek API key from .env file in home directory."""
    file_path = dotenv.find_dotenv(usecwd=True)
    return dotenv.dotenv_values(file_path).get("DEEPSEEK_API_KEY")


if __name__ == "__main__":
    print(read_deepseek_api_key())
