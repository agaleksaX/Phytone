# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:25:53 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:25:54 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main() -> None:
    args = sys.argv

    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")

    if len(args) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        index = 1
        for arg in args[1:]:
            print(f"Argument {index}: {arg}")
            index += 1

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
