from ex1.data_stream import DataStream
from typing import Protocol, List, Tuple

class ExportPlugin(Protocol):

    def process_output(
        self,
        data: List[Tuple[int, str]]
    ) -> None:
        ...
        
class CSVExportPlugin:
    
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        result = []
        for _, value in data:
            result.append(value)
        print(",".join(result))
        
class JSONExportPlugin:
    
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        result = []
        for rank, value in data:
            result.append(f'"item_{rank}": "{value}"')
        print("{" + ", ".join(result) + "}")


def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
    for proc in self.processors:
        export_data: List[Tuple[int, str]] = []
        for _ in range(nb):
            try:
                data = proc.output()
                export_data.append(data)
            except IndexError:
                break
        if export_data:
            plugin.process_output(export_data)