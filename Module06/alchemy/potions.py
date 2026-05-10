# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    potions.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:27:34 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:27:35 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from alchemy.elements import create_air, create_earth
from elements import create_water, create_fire


def healing_potion() -> str:
    return (
        "Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        "Strength potion brewed with "
        f"'{create_fire()}' and '{create_water()}'"
    )
