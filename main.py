from application.fuzz_generator.fuzz_generator import concurrency_fuzz_generator
from application.logging.init_logging import init_logging
import os


def main() -> None:

    concurrency_fuzz_generator()

    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.exists(dotenv_path):
        env_template_path = os.path.join(os.path.dirname(__file__), ".env.template")
        with open(env_template_path) as f:
            env_template = f.read()

        with open(dotenv_path, "w") as f:
            f.write(env_template)


if __name__ == "__main__":
    init_logging()
    main()
