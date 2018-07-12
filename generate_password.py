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
        pass

    def setup(self, server_interface, col_types): 
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        while(True):
            lower_bool = True
            upper_bool = True
            digit_bool = True
            symbl_bool = True

            if arg_reader.isNull(0):
                raise ValueError("I found a NULL!")
            else:
                pass_len = arg_reader.getInt(0)  # Input column      


            if pass_len < 8:
                pass_len = 8
            if pass_len > 24:
                pass_len = 24

            all_possible_symbols = ''
            if lower_bool:
                all_possible_symbols = all_possible_symbols + self.lower_case
            if upper_bool:
                all_possible_symbols = all_possible_symbols + self.upper_case
            if digit_bool:
                all_possible_symbols = all_possible_symbols + self.digits
            if symbl_bool:
                all_possible_symbols = all_possible_symbols + self.symbols

            new_password = ''.join(random.sample(all_possible_symbols, pass_len)) 
            res_writer.setString(new_password)
            res_writer.next()
            if not arg_reader.next():
                break

    def destroy(self, server_interface, col_types):
        pass


class generate_password_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return generate_password()
 
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addInt()
        return_type.addVarchar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarchar(24)
