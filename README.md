# AWS Vault
Vault for your software project using AWS Parameter Store

## What it is for
Usually in every backend project there is use of environment variables for holding values that can differ for each environment or need to be change from time to time. 

Sometimes these parameters can hold sensitive data like passwords or other secrets, there for need to be stored in a safe place.
One alternative for storing such data is AWS Parameter Store, this service ia part of the AWS Systems Manager service (https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

In AWS Parameter Store every parameter has a path. 
Here for example we have two parameters for `dev` environment and two for stage.

    /dev/DB_HOST
    /dev/DB_USER
    /dev/DB_PWD
    /stage/DB_HOST
    /stage/DB_USER
    /stage/DB_PWD

To load parameters for `dev` environment see this code snippet

    from awsvault import get_parameters
    
    get_parameters(
        path='dev',  # Parameters path
        update_environ=True,  # Update the environ
        dump_parameters=True  # Dump all loaded parameters to standard output
    )

Parameters dump into standard output. Notice tha the password is masked, by default every parameter that it's name suggesting that it contains a password or other secret will be masked.  

    DEBUG	__init__.py(54) method: dump 	 DB_HOST: my.owsome-db.net
    DEBUG	__init__.py(54) method: dump 	 DB_USER: db_dev_user
    DEBUG	__init__.py(54) method: dump 	 DB_PWD: ***********