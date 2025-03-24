import re
from pygments.lexers import get_lexer_for_filename
from pathlib import Path
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed


def parse_dir(path: Path, file_extensions_to_parse: list[str]) -> None:
    """
    This function will recursively parse all files in the directory
    :param file_extensions_to_parse: The list of file extensions to parse
    :param path: The path to the directory
    """
    with ThreadPoolExecutor() as executor:
        futures = []
        for file in path.rglob('*'):
            if file.is_file() and file.suffix in file_extensions_to_parse:
                futures.append(executor.submit(parse_file, file))

        for future in as_completed(futures):
            future.result()


def parse_file(file: Path) -> None:
    """
    Parse a file
    :param file: The file to parse
    """
    clean(file, [])
    chunks = read_file_in_chunks(file)
    embeddings = [get_embeddings(chunk) for chunk in chunks]
    # Store embeddings in a database
    for embedding in embeddings:
        # store embedding in database
        pass


def get_embeddings(chunk: str) -> list:
    """
    Get embeddings for the given chunk
    :param chunk: The chunk to get embeddings for
    :return: The embeddings
    """
    pass


def read_file_in_chunks(file_path: Path, chunk_size: int = 4096):
    """
    Read a file in chunks
    :param file_path:
    :param chunk_size:
    :return:
    """
    with file_path.open("r", encoding="utf-8", errors="ignore") as f:
        while chunk := f.read(chunk_size):
            yield chunk


def clean(file: Path, regex_patterns: list[str]) -> None:
    """
    Clean the file by removing content that matches the given regex patterns
    :param file: The file to clean
    :param regex_patterns: List of regex patterns to remove from the file
    """
    content = file.read_text(encoding="utf-8", errors="ignore")
    for pattern in regex_patterns:
        content = re.sub(pattern, '', content)
    file.write_text(content, encoding="utf-8", errors="ignore")


def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    file_extensions_to_parse: list[str] = config["file_extensions_to_parse"]
    path_to_repositories: Path = Path(config["path_to_repositories"])

    parse_dir(path_to_repositories, file_extensions_to_parse)



if __name__ == "__main__":
    main()

