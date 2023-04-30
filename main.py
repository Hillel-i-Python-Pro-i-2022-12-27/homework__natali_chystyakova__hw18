from application.fuzz_generator.fuzz_generator import concurrency_fuzz_generator
from application.logging.init_logging import init_logging


def main() -> None:

    concurrency_fuzz_generator()


if __name__ == "__main__":
    init_logging()
    main()
