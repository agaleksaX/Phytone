# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:24:37 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:24:38 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
    d1 = int(input("Day 1 harvest: "))
    d2 = int(input("Day 2 harvest: "))
    d3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {d1 + d2 + d3}")
