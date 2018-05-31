#!/usr/bin/env python

import vertica_sdk
import random

class generate_password(vertica_sdk.ScalarFunction):
    """Return the sum of two integer columns"""
 
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = lower_case.upper()
    digits = '1234567890'
    symbols = '!#$*%@()[].,?'

    def __init__(self):
	N = 12
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        while(True):
            if arg_reader.isNull(0):
                raise ValueError("I found a NULL!")
            else:
                input_varchar = arg_reader.getString(0)  # Input column

           
            hash = ''.join(random.choices(upper_case + lower_case + digits + symbols, k=N))

 
            if not arg_reader.next():
                break

    def destroy(self, server_interface, col_types):
        pass


class generate_password_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return generate_password()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()
