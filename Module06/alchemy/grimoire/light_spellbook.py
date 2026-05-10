# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    light_spellbook.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:24:12 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:24:13 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]

def light_spell_record() -> dict[str, str]:
    return {
        "name": "Light Spell",
        "description": "A spell that creates a bright light to illuminate dark areas.",
        "ingredients": light_spell_allowed_ingredients(),
        "incantation": "Lumos"
    }