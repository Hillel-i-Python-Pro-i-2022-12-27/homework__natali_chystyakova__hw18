
---
# :house:  Homework 18. Fuzz generator

1. You need to generate a list of "words".
From the outside are given:
 * alphabet (character set. e.g. ascii_lowercase + digits)
You can use the default characters from "string".
* word length
All words in the list must be of this length.
* number of words (optional)
* from which word number (or from which word by meaning) the generation should be continued.
2. The result must be saved. For example, to a file.
3. Generation should use concurrency. Choose which type suits best here.
4. The dataset should be generated as quickly as possible. Use ProcessPoolExecutor


* :wrench: install and update requiremets before run projet: make init-dev
* :arrow_forward: run this project without docker: make homework-i-run
* :whale: run this project with docker: make d-homework-i-run
* :end: purge without docker: make homework-i-purge
* :anchor: purge with docker: make d-homework-i-purge