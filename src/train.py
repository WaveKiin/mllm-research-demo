import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/baseline.yaml")
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Training baseline MLLM experiment with config: {args.config}")


if __name__ == "__main__":
    main()