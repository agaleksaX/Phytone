# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agaleksa <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 10:24:58 by agaleksa          #+#    #+#              #
#    Updated: 2026/05/10 10:24:59 by agaleksa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_intro() -> None:
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
