# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:24:46 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:24:47 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))

    def helper(day: int) -> None:
        if day > n:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(day + 1)

    helper(1)
