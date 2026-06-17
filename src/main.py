from my_stack import Queue


def find_start_end(
    maze: list[list[str]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Найти координаты старта 'S' и финиша 'E' в лабиринте.

    Граничный случай: если 'S' или 'E' отсутствуют — ValueError.
    """
    start = end = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    if start is None or end is None:
        raise ValueError("Лабиринт должен содержать S и E")
    return start, end


def bfs_path_exists(maze: list[list[str]]) -> bool:
    """Проверить, существует ли путь из S в E (волновой алгоритм, BFS).

    Возвращает True, если путь существует, иначе False.

    Граничные случаи:
        - пустой лабиринт -> False;
        - строки разной длины -> ValueError;
        - отсутствие S или E -> ValueError (из find_start_end).
    """
    if not maze or not maze[0]:
        return False

    rows, cols = len(maze), len(maze[0])
    if any(len(row) != cols for row in maze):
        raise ValueError("Все строки лабиринта должны быть одной длины")

    start, end = find_start_end(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = Queue()
    q.enqueue(start)
    visited: set[tuple[int, int]] = {start}

    while not q.is_empty():
        x, y = q.dequeue()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] != '1' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.enqueue((nx, ny))
    return False


def main() -> None:
    # Пример лабиринта (0 – проход, 1 – стена, S – старт, E – финиш)
    maze = [
        ['0', '0', '0', '0', 'S'],
        ['0', '1', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
        ['1', '1', '0', '1', 'E'],
        ['0', '0', '0', '0', '0'],
    ]

    try:
        if bfs_path_exists(maze):
            print("Путь из S в E существует.")
        else:
            print("Пути из S в E не существует.")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
