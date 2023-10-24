from .ali import ali
from .slowhttptest import slowhttptest
from .wrk2 import wrk2


testers_dict = {
    "wrk2": wrk2,
    "slowhttptest": slowhttptest
}
testers_list = list(testers_dict.values())
