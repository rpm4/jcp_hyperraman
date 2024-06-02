import pathlib
import subprocess
import platform
import click

osf_project = "2amkq"
here = pathlib.Path(__file__).resolve().parent


if platform.system() == 'Windows':
    python = 'python'
else:
    python = 'python3'


def print_with_line(s, char='#'):
    s += ' '
    s += char * (80 - len(s))
    print(s)


def print_then_call(*args, **kwargs):
    print_with_line(' '.join(args), '-')
    subprocess.run(args, check=True, **kwargs)


def _fetch_data():
    print_with_line('fetch data')
    print_then_call("osf", "-p", osf_project, "clone", "-U", str(here / "data"))


def _build_documents():
    from library import build_paper
    print_with_line("documents")
    print_with_line("paper", "-")
    build_paper.tex2pdf("paper", here)
    build_paper.tex2pdf("paper", here, False)


def _build_figures():
    print_with_line('figures')
    print_then_call(python, str(here / "figures" / "workup.py"))
    # print_then_call(python, str(here / "figures" / "preamp.py"))
    # print_then_call(python, str(here / "figures" / "poweramp.py"))
    # print_then_call(python, str(here / "figures" / "powerampslice.py"))
    # print_then_call(python, str(here / "figures" / "tunetest.py"))
    # print_then_call(python, str(here / "figures" / "spectral_delay_corrections.py"))


@click.group()
def main():
    pass

@main.command(name="fetch", help="download and extract the [raw data](https://osf.io/2nr9d)")
def fetch_data():
    _fetch_data() 

@main.command(name="all", help="build all steps")
def all_():
    print_with_line('building everything!')
    _fetch_data()
    _build_figures()
    _build_documents()
    print_with_line('building done!')


@main.command("documents")
def build_documents():
    _build_documents()

@main.command(name="figures", help="generate manuscript figures from the data")
def build_figures():
    _build_figures()


if __name__ == '__main__':
    main()
