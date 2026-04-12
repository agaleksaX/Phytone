def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except ValueError:
        print(f"Invalid temperature: {temp_str}")
        return 0


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    print("Input data is '25'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}°C\n")

    print("Input data is 'abc'")
    temp = input_temperature("abc")
    print(f"Temperature is now {temp}°C\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
