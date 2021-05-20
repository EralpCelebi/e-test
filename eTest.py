from typing import Optional, Text

from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table


class test(object):
    functions = {}
    
    def __init__(self, result: Optional[any]) -> None:
        self.result = result
    
    def __call__(self, function) -> any:
        test.functions[function.__name__] = [function, self.result]
        
        return function

    def run() -> bool:
        share_progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%")
        )
        
        accepted =  share_progress.add_task("[green]Accepted", total=len(test.functions.keys()))
        rejected =  share_progress.add_task("[red]Rejected",total=len(test.functions.keys()))
        total    =  share_progress.add_task("[blue]Total", total=len(test.functions.keys()))

        
        
        progress_table = Table.grid()
        progress_table.add_row(
            Panel.fit(share_progress, title="[b]Jobs", border_style="red", padding=(1,2))
        )
        
        rejected_shares = []
        
        with Live(progress_table, refresh_per_second=10):
            for key in test.functions.keys():
                if test.functions[key][0]() == test.functions[key][1]:
                    share_progress.advance(accepted)
                else:
                    rejected_shares.append(key)
                    share_progress.advance(rejected)
                
                share_progress.advance(total)
                    
                        

if __name__ == "__main__":
    @test(29)
    def main():
        return 29


    test.run()