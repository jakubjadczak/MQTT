from multiprocessing import Process
from utils import get_components
import sys
import os


def run_process(path, process):
    os.system(f'python {path} {process}')


class Cli:
    def __init__(self) -> None:
        self.argv = sys.argv
        self.all_components = get_components()
        self.read_argv()

    def read_argv(self):
        if self.argv[1] == 'all':
            self.simulate_all()
        else:
            self.simulate_one()


    def simulate_all(self):
        try:
            for p in self.all_components:
                process = Process(target=run_process,
                                args=('device.py', p))
                process.start()
        except Exception as e:
            print(f'Error: run simulate processes {e}')

    def simulate_one(self):
        run_process('device.py', self.argv[1])


if __name__ == '__main__':
    c = Cli()