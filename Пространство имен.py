calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()

    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()

    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]

    return string_lower in list_lower


print(string_info("Hello World"))
print(is_contains("urban", ["city", "village", "URBAN"]))
print(is_contains("town", ["city", "village", "urban"]))

print("Количество вызовов функций:", calls)
