from abc import ABC, abstractmethod


class IParser(ABC):
    @abstractmethod
    def parse_file(self, file_path: str) -> None:
        pass

    @abstractmethod
    def parse_string(self, ctx: str) -> None:
        pass

    @abstractmethod
    def traverse(self) -> None:
        pass
