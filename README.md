# Branch Me
This repository is designed for contributors to practice branching and pull requests.

## Getting Started

1. Clone the repo:
   ```sh
   git clone https://github.com/sakhileln/branch-me.git
   ```
2. Create a new branch:
   ```sh
   git checkout -b feature/YourFeature
   ```
3. Implement one of the functions in `functions.py`.
4. Run the tests to ensure correctness:
   ```sh
   python -m unittest discover
   ```
5. Push your changes:
   ```sh
   git push origin feature/YourFeature
   ```
6. Open a pull request for review.

## Contribution Rules
- Contributors **cannot** push directly to `main`.
- All Pull Requests must be reviewed before merging.
- The CI workflow must pass all tests before merging.
- **Main Branch Protection:** Direct pushes to `main` are blocked. Contributors must use feature branches and create pull requests for review.
- **Branch Protection Rules:**
  - Pull requests are **required** before merging.
  - CI tests must **pass** before merging.

Happy Coding! 🚀
