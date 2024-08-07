import os
import shutil
from pathlib import Path
import argparse


def add_file_prefix(file_path):
    directory, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)
    prefix = "duplicate_"
    new_filename = filename
    count = 1
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{prefix}{count}_{name}{ext}"
        count += 1
    return os.path.join(directory, new_filename)


def copyfiles(src_dir, dst_dir):
    try:
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isdir(item_path):
                copyfiles(item_path, dst_dir)
            else:
                extension = os.path.splitext(item)[1].lstrip(".").lower()
                if not extension:
                    extension = "without_ext"
                dest_dir = os.path.join(dst_dir, extension)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                destination_path = os.path.join(dest_dir, item)
                destination_path = add_file_prefix(destination_path)
                shutil.copy2(item_path, destination_path)
    except Exception as e:
        print(f"Помилка при обробці {src_dir}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копіювання та стуктуризація файлів.")
    parser.add_argument("source_dir", help="Вихідна тека з файлами.")
    parser.add_argument(
        "destination_dir",
        nargs="?",
        default="dist",
        help="Вихідна тека для створення стуктури з файлів по розширенню. За замовченням dist.",
    )

    args = parser.parse_args()
    copyfiles(Path(args.source_dir), Path(args.destination_dir))
