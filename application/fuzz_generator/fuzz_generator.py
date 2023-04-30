from dotenv import load_dotenv
import os
from application.config.path import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger

import string
import multiprocessing
import concurrent.futures


def generate_words(alphabet: str, len_word: int, continue_index: int = 0, amount_of_words: int | None = None) -> list:
    logger = get_core_logger()
    logger.info(f" continue_index: {continue_index}")
    logger.info(f" amount_of_words: {amount_of_words}")
    logger.info(f" len_word: {len_word}")
    lists_word = []
    if amount_of_words is not None:
        for i in range(continue_index, amount_of_words):
            logger.info(f" continue_index: {continue_index}")
            logger.info(f" amount_of_words: {amount_of_words}")
            index = i % len(alphabet)
            word = alphabet[index]
            list_word = []
            for n in range(len_word):
                if n < len_word - 1:
                    list_word.append(alphabet[0])
                    index = i // (len(alphabet)) ** (len_word - 1 - n)
                    list_word[n] = alphabet[index]
                else:
                    list_word.append(word)
            logger.info(f" print: {list_word}")
            lists_word.append("".join(list_word))

    return lists_word


def generate_words_and_write_to_file(args):
    alphabet, len_word, start_index, end_index, file_name = args
    words = generate_words(alphabet, len_word, start_index, end_index)

    file_name = f"words_{start_index}_{end_index}"
    path_to_file = FILES_OUTPUT_PATH.joinpath(f"{file_name}.txt")
    with open(path_to_file, "w") as f:
        f.write("\n".join(words))


def concurrency_fuzz_generator():
    load_dotenv()

    len_word = int(os.getenv("LEN_WORD", 2))
    amount_of_words = int(os.getenv("AMOUNT_OF_WORDS", 100))
    continue_index = int(os.getenv("CONTINUE_INDEX", 0))
    alphabet = os.getenv("ALPHABET", "".join([string.ascii_lowercase, string.digits]))
    logger = get_core_logger()

    num_words = amount_of_words

    num_processes = multiprocessing.cpu_count() - 1
    chunk_size = (num_words - continue_index) // num_processes
    logger.info(f"Number of available processors: {num_processes}")
    logger.info(f"chunk_size: {chunk_size}")
    logger.info("Start generations")

    args = []
    for i in range(num_processes):
        start_index = i * chunk_size + continue_index
        end_index = (i + 1) * chunk_size + continue_index if i != num_processes - 1 else num_words
        file_name = f"words_{start_index}_{end_index}"
        path_to_file = FILES_OUTPUT_PATH.joinpath(f"{file_name}.txt")
        args.append((alphabet, len_word, start_index, end_index, file_name))

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        executor.map(generate_words_and_write_to_file, args)

    logger.info("Finish generations")

    path_to_file = FILES_OUTPUT_PATH.joinpath("all_words.txt")
    with open(path_to_file, "w") as f:
        for i in range(num_processes):
            start_index = i * chunk_size + continue_index
            end_index = (i + 1) * chunk_size + continue_index if i != num_processes - 1 else num_words
            file_name = f"words_{start_index}_{end_index}"
            path_to_file = FILES_OUTPUT_PATH.joinpath(f"{file_name}.txt")

            with open(path_to_file) as f_part:
                f.write(f_part.read())
