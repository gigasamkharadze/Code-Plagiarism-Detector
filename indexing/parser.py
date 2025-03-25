from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import logging
import re

logging.basicConfig(level=logging.INFO)


class Parser:
    def __init__(self, config: dict[str, Any]):
        self._path_to_repositories = Path(config["path_to_repositories"])
        self._file_extensions_to_parse = config["file_extensions_to_parse"]
        self._regex_mappings = config["regex_mappings"]
        self._processed_files = []

    def get_content(self):
        self._parse_directory()
        return self._processed_files

    def _parse_directory(self):
        with ThreadPoolExecutor() as executor:
            futures = []
            for file in self._path_to_repositories.rglob('*'):
                if file.is_file() and file.suffix in self._file_extensions_to_parse:
                    regex_patterns = self._regex_mappings.get(file.suffix, [])
                    futures.append(executor.submit(self._parse_file, file, regex_patterns))

            for future in as_completed(futures):
                self._processed_files.append(future.result())

    @staticmethod
    def _parse_file(file, regex_patterns: list[str]) -> str:
        logging.info(f"Parsing file: {file}")
        content = file.read_text(encoding="utf-8", errors="ignore")
        for pattern in regex_patterns:
            content = re.sub(pattern, '', content)

        return content
