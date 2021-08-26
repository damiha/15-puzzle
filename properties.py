class Properties:
    WINDOW_TITLE = "15-puzzle"

    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = CANVAS_WIDTH

    CELLS_PER_ROW = 4
    CELLS_PER_COLUMN = CELLS_PER_ROW

    CELL_WIDTH = CANVAS_WIDTH / CELLS_PER_ROW
    CELL_HEIGHT = CANVAS_HEIGHT / CELLS_PER_COLUMN

    CELL_EMPTY = -1

    AMOUNT_SHUFFLES = 20

    CELL_BG_COLOR = "#fff"
    CANVAS_BG_COLOR = "lightgrey"
    TEXT_COLOR = "darkblue"
    TEXT_FONT = "Times 20 bold"

    SOLVER_OPTIONS = [
        "breadth first search",
        "depth first search",
        "depth first search (limited)",
        "depth first search (iterative)",
    ]

    DEFAULT_SOLVER = "breadth first search"
    DEFAULT_DEPTH_LIMIT = AMOUNT_SHUFFLES
