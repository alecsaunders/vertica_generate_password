#!/usr/bin/env python

import vertica_sdk
import random

class generate_password(vertica_sdk.ScalarFunction):
    """Return random password of N length"""

    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = lower_case.upper()
    digits = '123456789012345'  # The extra 5 numbers are so that the total number of available character symbols = 100
    symbols = "#!+*?,./=~-$_: \"'%&();<>@`[]\^|{}"

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        while(True):
            pass_len = arg_reader.getInt(0)  # Password length input column
            pass_len = 8 if pass_len < 8 else pass_len
            pass_len = 100 if pass_len > 100 else pass_len

            new_password = ''.join(random.sample(self.lower_case + self.upper_case + self.digits + self.symbols, pass_len))
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
