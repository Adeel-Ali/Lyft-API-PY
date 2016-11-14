# -*- coding: utf-8 -*-

"""
    lyftapilib.models.cost
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 11/14/2016
"""
from .base_model import BaseModel

class Cost(BaseModel):

    """Implementation of the 'Cost' model.

    TODO: type model description here.

    Attributes:
        amount (int): Total price of the ride
        currency (string): The ISO 4217 currency code for the amount (e.g.
            USD)
        description (string): The description for the cost

    """

    def __init__(self, 
                 amount = None,
                 currency = None,
                 description = None):
        """Constructor for the Cost class"""
        
        # Initialize members of the class
        self.amount = amount
        self.currency = currency
        self.description = description

        # Create a mapping from Model property names to API property names
        self.names = {
            "amount" : "amount",
            "currency" : "currency",
            "description" : "description",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            amount = dictionary.get("amount")
            currency = dictionary.get("currency")
            description = dictionary.get("description")
            # Return an object of this model
            return cls(amount,
                       currency,
                       description)
