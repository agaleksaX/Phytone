# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_alembic_4.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:27:13 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:27:14 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import alchemy

print(f"Testing create_air : {alchemy.create_air()}")

try:
    print(
        f"Testing create_earth : "
        f"{alchemy.create_earth()}"  # type: ignore[attr-defined]
    )
except AttributeError:
    print("AttributeError")
