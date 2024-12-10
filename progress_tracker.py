from tqdm import tqdm

def show_progress_bar(iterable, desc="Downloading"):
    for item in tqdm(iterable, desc=desc):
        yield item