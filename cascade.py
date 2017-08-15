
import os
import shutil

MY_PATH = "/home/aelkikhia/IdeaProjects/cascade/archive"
BASE_DIR = "/home/aelkikhia/IdeaProjects/cascade/"
my_list = ["general", "action", "drama"]


def move_files(directory):
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)

            for genre in my_list:
                newpath = os.path.join(BASE_DIR+genre, filename)
                if root.endswith(genre):
                    shutil.move(filepath, newpath)


def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
full_file_paths = get_filepaths(MY_PATH)

for word in full_file_paths:
    print(word)


