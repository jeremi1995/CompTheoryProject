def color_text(color: str, text: str):
    match color:
        case "red":
            return f"\033[31m{text}\033[0m"
        case "green":
            return f"\033[32m{text}\033[0m"
        case "yellow":
            return f"\033[33m{text}\033[0m"
        case "blue":
            return f"\033[34m{text}\033[0m"
        case "magenta":
            return f"\033[35m{text}\033[0m"
        case "cyan":
            return f"\033[36m{text}\033[0m"
        case _:
            return text