from shutil import get_terminal_size

def important_message(message: str) -> str:
    """
    Оформляет текст в рамку из символов '=' и '#', сохраняя пробелы между словами.
    """
    width = get_terminal_size().columns - 1
    border = "#" + "=" * (width - 2) + "#"
    empty = "#" + " " * (width - 2) + "#"
    max_width = width - 6

    lines = []
    current_line = ""
    for char in message:
        if len(current_line) < max_width:
            current_line += char
        else:
            lines.append(current_line.center(max_width))
            current_line = char
    if current_line:
        lines.append(current_line.center(max_width))

    # Формируем рамку
    framed_message = [border, empty]
    framed_message += [f"#  {line}  #" for line in lines]
    framed_message += [empty, border]
    return "\n".join(framed_message)