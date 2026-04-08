import sys

print("=== Player Score Analytics ===")

if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    scores = []

    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            scores.append(num)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("Scores processed:", scores)

        total = sum(scores)
        count = len(scores)
        avg = total / count
        high = max(scores)
        low = min(scores)
        rng = high - low

        print("Total players:", count)
        print("Total score:", total)
        print("Average score:", avg)
        print("High score:", high)
        print("Low score:", low)
        print("Score range:", rng)
