# Via a tweet by MIke Driscoll (@driscollis)

from cmath import inf
import difflib
from IPython.display import HTML

def diff_line_table(txt1, txt2, from_head='', to_head='', linesplit=True, num_lines=inf):
    """Line by line differences in an HTML table."""
    d = difflib.HtmlDiff()

    if linesplit:
        txt1 = txt1.splitlines()
        txt2 = txt2.splitlines()

    diff = d.make_table(txt1, txt2, from_head, to_head)
    # The diff returns diff elements in classed spans
    # but they aren't rendered visibly unless appropriate CSS is added.
    # Classes: diff_add, diff_chg, diff_sub
    style = """
    <style>
    table.diff span.diff_add {color:green}
    table.diff span.diff_sub {color:red}
    table.diff span.diff_chg {color:orange}
    </style>
    """
    return HTML(style + diff)