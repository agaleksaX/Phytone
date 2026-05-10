# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:24:44 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:24:45 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
    n = int(input("Days untils harvest: "))

    for i in range(1, n+1):
        print(f"Day {i}")

    print("Harvest time!")
