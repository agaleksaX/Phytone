def input_temperatur(temp_str: str) -> int:
    return int(temp_str)


def testing_temperatur() -> None:
    print("=== Garden Temperature ===\n")

    try:
        print("Input data is '25'")
        temp = input_temperatur("25")
        print(f"Temperature is now {temp}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        print("Input data is 'abc'")
        temp = input_temperatur("abc")
        print(f"Temperature is now {temp}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    testing_temperatur()
