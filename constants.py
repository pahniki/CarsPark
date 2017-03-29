class Constants:
    burn_incr = 1.01  # 1% fuel consumption increase
    deg_step = 1000  # 1000km cars properties has degeneration
    hund = 100  # used for calculations

    class Diesel:
        repare_cost = 700  # $
        value_lower = 10.5  # $ per 1000 km

    class Pentol:
        switch_point = 50000  # km
        repare_cost = 500  # $
        value_lower = 9.5  # $ per 1000 km
