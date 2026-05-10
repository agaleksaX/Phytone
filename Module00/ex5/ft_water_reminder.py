# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:24:41 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:24:43 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
