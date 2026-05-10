import alchemy

print(f"Testing create_air : {alchemy.create_air()}")

try:
    print(
        f"Testing create_earth : "
        f"{alchemy.create_earth()}"  # type: ignore[attr-defined]
    )
except AttributeError:
    print("AttributeError")
