# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:26:24 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:26:25 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
        content = file.read()

        print("---")
        print(content)
        print("---")

        file.close()
        print(f"File '{filename}' closed.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}\n")


if __name__ == "__main__":
    main()
