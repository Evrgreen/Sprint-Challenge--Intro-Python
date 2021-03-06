# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass
# This is the base class


class FlightVehicle(Vehicle):
    pass
    # Child of baseclass


class Airplane(FlightVehicle):
    pass
    # child of FlightVehicle, grandchild of Vehicle


class Starship(FlightVehicle):
    pass
    # child of FlightVehicle, grandchild of Vehicle


class GroundVehicle(Vehicle):
    pass
    # child of baseclass


class Car(GroundVehicle):
    pass
    # child of FlightVehicle, grandchild of Vehicle


class Motorcycle(GroundVehicle):
    pass
    # child of FlightVehicle, grandchild of Vehicle
