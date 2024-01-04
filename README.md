<h1 align="center">
    UACP
</h1>
<p align="center">
  🚀 Using Universal Agent Communication Protocol to Build Your Agent 🤖
</p>

## What is UACP?

UACP is an innovative API specification designed to serve as the lingua franca for communication between diverse intelligent Agents. By providing a set of standardized interfaces, UACP enables seamless integration and efficient, flexible interaction among a variety of AI Agents. The design philosophy of UACP is centered around openness, extensibility, and interoperability, ensuring that it can adapt to the evolving technological ecosystem and support use cases ranging from simple automation tasks to complex multi-Agent systems.

## Core Concept

📋**Task Management**: At the heart of UACP is the concept of task management. A task represents a discrete unit of work assigned to an agent, which could range from simple file operations to intricate decision-making processes. UACP defines a clear structure for tasks, ensuring that agents understand what is required and can report their progress and results in a consistent manner.

🔀 **Dynamic Workflow Composition**: UACP introduces dynamic workflow composition, allowing agents to not only execute predefined sequences of actions but also to dynamically determine the next steps based on context, results, and external triggers. This adaptive approach ensures that agents can handle complex, non-linear workflows with ease.

⚡ **Real-Time Interaction**: Real-time interaction is a cornerstone of UACP. Agents can communicate in real-time, exchanging messages, status updates, and data streams. This enables synchronous operations and immediate responses, which are crucial for time-sensitive tasks and collaborative activities among multiple agents.

📈 **Scalability and Extensibility**: UACP is built with scalability in mind. It can support a growing number of agents and tasks without compromising performance. Additionally, the protocol is extensible, allowing for the introduction of new features and capabilities without disrupting existing operations.

🔗 **Interoperability**: UACP emphasizes interoperability, enabling agents built on different frameworks or languages to communicate without barriers. This is achieved through a well-defined API and a set of standard data formats that ensure compatibility across diverse systems.

## Status && Roadmap

UACP is build by [Promptulate AI](https://github.com/Undertone0809/promptulate) and [Cogit AGI](). We aim to explore all possible locations in the AGI field. Welcome your coming anytime.  

## Coming Soon 💟

🏃🚀🛸 We are exciting to launch this project externally. Currently, we are conducting intensive detailed design and capability testing, and the detailed protocol SDK implementation is expected to be officially released **by the end of January**.


## Very first steps

### Initialize your code

1. Clone the project

```bash
git clone https://github.com/Undertone0809/UACP
cd UACP
```

2. If you don't have `Poetry`. 

Conda environment is is recommended.

```bash
conda create -n uacp python==3.10
```

Please activate python of current project and install run:

```bash
conda activate uacp
pip install poetry
```

3. Initialize poetry and `pre-commit` hooks:

```bash
make install
```


### Makefile usage

[`Makefile`](https://github.com/Undertone0809/uacp/blob/master/Makefile) contains a lot of functions for faster development.


<details>
<summary>1. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>2. Codestyle and type checks</summary>
<p>

Automatic formatting uses `ruff`.

```bash
make polish-codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `ruff` and `darglint` library

</p>
</details>

<details>
<summary>3. Code security</summary>
<p>

> If this command is not selected during installation, it cannnot be used.

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>4. Tests with coverage badges</summary>
<p>

Run `pytest`
Ensure that your test files are located in a `tests/` directory in the root of the repository. Run `make test` to execute the tests.

```bash
make test
```

</p>
</details>

<details>
<summary>5. All linters</summary>
<p>

Of course there is a command to run all linters in one:

```bash
make lint
```

the same as:

```bash
make check-codestyle && make test && make check-safety
```

</p>
</details>

<details>
<summary>6. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/Undertone0809/python-package-template/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker).

</p>
</details>

<details>
<summary>7. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 🛡 License

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/Undertone0809/uacp/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{uacp,
  author = {Zeelnad},
  title = {Universal Agent Communication Protocol},
  year = {2024},
  publisher = {Underonte0809},
  journal = {https://github.com/Undertone0809/UACP},
  howpublished = {\url{https://github.com/Undertone0809/uacp}}
}
```
