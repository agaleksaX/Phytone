from typing import Any, List

from ex0.data_processor import (
    DataProcessor,
    LogProcessor,
    NumericProcessor,
    TextProcessor,
)


class DataStream:

    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:

        for data in stream:

            processed = False

            for proc in self.processors:

                if proc.validate(data):
                    proc.ingest(data)
                    processed = True
                    break

            if not processed:
                raise ValueError(f"No processor could handle: {data}")


stream = DataStream()

stream.register_processor(LogProcessor())
stream.register_processor(TextProcessor())
stream.register_processor(NumericProcessor())

stream.process_stream([
    "Hello",
    42,
    [1, 2, 3],
    {
        "log_level": "ERROR",
        "log_message": "Something failed"
    }
])
