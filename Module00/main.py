from ex0.ft_hello_garden import ft_hello_garden
from ex1.ft_garden_name import ft_garden_name
from ex2.ft_plot_area import ft_plot_area
from ex3.ft_harvest_total import ft_harvest_total
from ex4.ft_plant_age import ft_plant_age
from ex5.ft_water_reminder import ft_water_reminder
from ex6.ft_count_harvest_iterative import ft_count_harvest_iterative
from ex6.ft_count_harvest_recursive import ft_count_harvest_recursive
from ex7.ft_seed_inventory import ft_seed_inventory


def main():
    print("Testing ex0:")
    ft_hello_garden()
    print(" ")
    print("Testing ex1:")
    ft_garden_name()
    print(" ")
    print("Testing ex2:")
    ft_plot_area()
    print(" ")
    print("Testing ex3:")
    ft_harvest_total()
    print(" ")
    print("Testing ex4:")
    ft_plant_age()
    print(" ")
    print("Testing ex5:")
    ft_water_reminder()
    print(" ")
    print("Testing ex6:")
    ft_count_harvest_iterative()
    print(" ")
    ft_count_harvest_recursive()
    print(" ")
    ft_seed_inventory("tomato", 15, "packets")


if __name__ == "__main__":
    main()
