import os
from quickbelog import Log
from awspstore import get_parameters, dump


if __name__ == '__main__':
    get_parameters(
        path='dev',
        update_environ=True,
        dump_parameters=True
    )
    Log.info("* * *  Environ  * * *")
    dump(os.environ)
