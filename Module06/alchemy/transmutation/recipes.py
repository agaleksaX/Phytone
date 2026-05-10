# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipes.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:27:39 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:27:40 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ..elements import create_air
from ..potions import strength_potion
import elements


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: "
        f"brew '{create_air()}' and '{strength_potion()}' "
        f"mixed with '{elements.create_fire()}'"
    )
