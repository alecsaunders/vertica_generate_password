# Vertica Generate Password
Simple Vertica UDx—written in Python—for generating random passwords

## Installation
+ Clone this repo on a node with Vertica installed
+ In Vertica run the following two commands

```sql
CREATE OR REPLACE LIBRARY gen_pass_lib AS '/path/to/file/generate_password.py' LANGUAGE 'Python';
CREATE OR REPLACE FUNCTION generate_password AS LANGUAGE 'Python' NAME 'generate_password_factory' LIBRARY gen_pass_lib FENCED;
```

## Usage
The `GENERATE_PASSWORD` function takes only one integer argument for the length of the password. The password length must be between 8 and 100 characters long. Any value passed in less than 8 will be changed to 8, and any value passed in greather than 100 will be changed to 100.

```
=> SELECT generate_password(12);
 generate_password
-------------------
 tEU#*Zu(2112
(1 row)
```
