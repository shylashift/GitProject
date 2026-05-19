import os
import argparse

# Research Metadata
PROJECT_NAME = "Digital_Tools_Research"
ORCID_ID = "https://orcid.org"  # Replace with your ID


def initialize_ecosystem(base_dir: str = "research_ecosystem"):
    """Generate standardized directory structure and automated README."""

    directories = ["data/raw", "data/processed", "scripts", "bib", "docs"]

    print(f"Initializing research ecosystem in: {base_dir}/")
    for folder in directories:
        path = os.path.join(base_dir, folder)
        os.makedirs(path, exist_ok=True)
        print(f"  Created: {folder}/")

    readme_content = f"""# {PROJECT_NAME}

## Researcher Information
- **ORCID:** {ORCID_ID}

## Project Structure
- `data/`: Research datasets.
- `scripts/`: Python/Bash scripts for data processing.
- `bib/`: Bibliography files (.bib).
- `docs/`: Drafts and documentation.

*Generated automatically by init_research.py*
"""

    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"Success: Project structure and README.md have been generated in {base_dir}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Initialize a standardized digital research ecosystem."
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="research_ecosystem",
        help="Target directory (default: research_ecosystem)",
    )
    args = parser.parse_args()
    initialize_ecosystem(args.output_dir)
