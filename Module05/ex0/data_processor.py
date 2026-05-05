from abc import ABC, abstractmethod
from typing import Any, List, Tuple


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError("No data")

        return self._storage.pop(0)


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, (int, float)):
            self._storage.append((self._counter, str(data)))
            self._counter += 1

        elif isinstance(data, list):
            for i in data:
                self._storage.append((self._counter, str(i)))
                self._counter += 1


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self._storage.append((self._counter, data))
            self._counter += 1

        elif isinstance(data, list):
            for i in data:
                self._storage.append((self._counter, i))
                self._counter += 1


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            if "log_level" in data and "log_message" in data:
                return isinstance(data["log_level"], str) and isinstance(
                    data["log_message"], str
                )

        if isinstance(data, list):
            return all(self.validate(item) for item in data)

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            level = data["log_level"]
            message = data["log_message"]
            self._storage.append((self._counter, f"{level}: {message}"))
            self._counter += 1

        elif isinstance(data, list):
            for item in data:
                level = item["log_level"]
                message = item["log_message"]
                self._storage.append((self._counter, f"{level}: {message}"))
                self._counter += 1


if __name__ == "__main__":
    print("Testing NumericProcessor:")
    num = NumericProcessor()
    print(num.validate(42))  # True
    print(num.validate("hello"))  # False

    try:
        num.ingest("foo")
    except Exception as e:
        print(e)

    num.ingest([1, 2, 3])
    while True:
        try:
            print(num.output())
        except IndexError:
            break

    print("\nTesting TextProcessor:")
    text = TextProcessor()
    print(text.validate(42))  # False
    print(text.validate("hello"))  # True
    text.ingest("122512")
    while True:
        try:
            print(text.output())
        except IndexError:
            break
    text.ingest(["foo", "bar", "baz"])
    while True:
        try:
            print(text.output())
        except IndexError:
            break

    print("\nTesting LogProcessor:")
    log = LogProcessor()
    log_data = {"log_level": "ERROR", "log_message": "Something went wrong"}
    print(log.validate(log_data))  # True
    log.ingest(log_data)
    while True:
        try:
            print(log.output())
        except IndexError:
            break

    print("\nTesting LogProcessor with list of logs:\n")
    log_list = [
        {"log_level": "INFO", "log_message": "Process started"},
        {"log_level": "WARNING", "log_message": "Low disk space"},
    ]
    log.ingest(log_list)
    while True:
        try:
            print(log.output())
        except IndexError:
            break
