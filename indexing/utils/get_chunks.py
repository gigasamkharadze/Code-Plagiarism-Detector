# TODO: Refine chunking logic

def get_chunks(content, chunk_size=4096):
    return [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
