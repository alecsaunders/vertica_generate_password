# Vertica Generate Password
Simple Vertica UDx—written in Python—for generating random passwords

## Installation
+ Clone this repo on a node with Vertica installed
+ In Vertica run the following two commands

```sql
CREATE OR REPLACE LIBRARY gen_pass_lib AS '/path/to/file/generate_password.py' LANGUAGE 'Python';
CREATE OR REPLACE FUNCTION generate_password AS LANGUAGE 'Python' NAME 'generate_password_factory' LIBRARY gen_pass_lib FENCED;
```
