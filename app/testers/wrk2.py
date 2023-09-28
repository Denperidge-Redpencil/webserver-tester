from .Tester import BinaryTester

wrk2 = BinaryTester(
    binary="wrk2/wrk",
    build_commands=[
        "git clone https://github.com/giltene/wrk2.git",
        "cd wrk2", 
        "make"
    ],
    default_args="-t2 -c100 -d30s -R2000"
)
