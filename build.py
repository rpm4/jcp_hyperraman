import pathlib
import subprocess
import platform
import click

#osf_project = "2amkq"
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
    print_with_line("si", "-")
    build_paper.tex2pdf("si", here)
    build_paper.tex2pdf("si", here, False)


def _build_figures():
    print_with_line('figures')
    print_then_call(python, str(here / "figures" / "2D_spec.py"))
    print_then_call(python, str(here / "figures" / "toc.py"))
    print_then_call(python, str(here / "figures" / "2D_spec_chgsign.py"))
    print_then_call(python, str(here / "figures" / "contours.py"))
    print_then_call(python, str(here / "figures" / "plotting_fcht.py"))
    print_then_call(python, str(here / "figures" / "varying_delta.py"))

@click.group()
def main():
    pass

@main.command(name="all", help="build all steps")
def all_():
    print_with_line('building everything!')
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
