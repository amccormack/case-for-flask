import argparse

import io
import pandas as pd
from matplotlib.figure import Figure
from typing import Union

def make_image(excel_path: str, output: str) -> None:
    fig = excel_to_figure(excel_path)
    fig.savefig(output)

def excel_to_bytes(excel: Union[str, bytes]) -> bytes:
    fig = excel_to_figure(excel)
    b = io.BytesIO()
    fig.savefig(b, format="png")
    b.seek(0)
    return b.read()

def excel_to_figure(excel: Union[str, bytes]) -> Figure:
    df = pd.read_excel(excel)
    fig = Figure(figsize=(15,8))
    ax = fig.subplots()
    line_ts, = ax.plot(df.Date, df["Total Sales"], "r-")
    line_e, = ax.plot(df.Date, df["Expected"], "g-")
    ax2 = ax.twinx()
    line_t, = ax2.plot(df.Date, df["Number of Tables"], "+")
    line_ts.set_label('Total Sales')
    line_e.set_label('Expected Sales')
    line_t.set_label('Tables Served')
    ax.set_ylabel('Dollars')
    ax.set_title('Monthly Report')
    ax2.set_ylabel('Tables')
    ax.legend()
    ax2.legend(loc='lower right')
    return fig

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('excel_file')
    parser.add_argument('output_file')
    args = parser.parse_args()
    make_image(args.excel_file, args.output_file)

if __name__ == '__main__':
    main()
