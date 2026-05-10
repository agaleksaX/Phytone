# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:24:35 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:24:36 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
