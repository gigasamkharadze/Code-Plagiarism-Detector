import re
from typing import List

def get_chunks(content: str, pattern: str, include_delimiter: bool = True) -> List[str]:
    """
    Splits the content into chunks based on the provided pattern.
    :param content: the code to be chunked
    :param pattern: the regex pattern to match and split the content
    :param include_delimiter: whether to include the delimiter in the chunks
    :return: a list of chunks
    """
    matches = list(re.finditer(pattern, content))
    if not matches:
        return [content] if content else []

    chunks = []
    last_index = 0

    for match in matches:
        start = match.start() if include_delimiter else match.end()
        if start > last_index:
            chunks.append(content[last_index:start])
        last_index = match.start() if include_delimiter else match.end()

    if last_index < len(content):
        chunks.append(content[last_index:])

    return chunks
