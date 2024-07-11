import argparse
import os

# Returns the result of resolving the optionally passed directory against the CWD
def get_working_directory(specified_dir: str | None) -> str:
    if specified_dir is None:
        return os.getcwd()
    return os.getcwd() + '/' + specified_dir.strip('/')

# Returns either the optionally passed directory prefix, or the default "Takeout"
def get_directory_prefix(specified_prefix: str | None) -> str:
    if specified_prefix is None:
        return "Takeout"
    return specified_prefix

# Returns either the optionally passed ignore keyword, or the default "done"
def get_ignore_keyword(specified_keyword: str | None) -> str:
    if specified_keyword is None:
        return "done"
    return specified_keyword

# Returns either the optionally passed output directory, or the default CWD
def get_output_directory(specified_output: str | None) -> str:
    if specified_output is None:
        return os.getcwd()
    return os.getcwd() + '/' + specified_output.strip('/')

# Gets all the relevant directory names to walk
def get_toplevel_directories(root: str, prefix: str, ignore: str) -> list[str]:
    w = os.walk(root)
    for (dirpath, dirnames, filenames) in w:
        localdirs = filter(lambda dirname: dirname.startswith(prefix) and ignore not in dirname, dirnames)
        return [root + "/" + dirname for dirname in localdirs]
    
# Copies all files to the golden tree
def merge_in_target(dir: str, target: str):
    w = os.walk(dir)
    for (dirpath, dirnames, filenames) in w:
        relativepath = dirpath.removeprefix(dir + '/').removesuffix('/')
        absolutepath = target + "/" + relativepath
        
        os.makedirs(absolutepath, exist_ok=True)

        for filename in filenames:
            if filename == ".DS_Store":
                continue
            srcfile = dirpath + "/" + filename
            dstfile = absolutepath + "/" + filename
            # print(f"Moving {srcfile} to {dstfile}")
            os.rename(srcfile, dstfile)

def construct_tree(input_dirs: list[str], target: str):
    for dir in input_dirs:
        merge_in_target(dir, target)

def main(): 
    # init arg parser
    parser = argparse.ArgumentParser(description = "Drive Merger")
    parser.add_argument("-r", "--root", help = "Set input directory root")
    parser.add_argument("-p", "--prefix", help = "Set directory prefix to search for (default: Takeout)")
    parser.add_argument("-i", "--ignore", help = "Set directory ignore keyword (default: done)")
    parser.add_argument("-o", "--output", help = "Set output directory root")
    parser.add_argument(
        "-d", "--dryrun", help = "Whether changes should not take effect", default = False, action = 'store_true'
    )
    args = parser.parse_args()

    root = get_working_directory(args.root)
    prefix = get_directory_prefix(args.prefix)
    ignore = get_ignore_keyword(args.ignore)
    output = get_output_directory(args.output) 
    print(f"Root: {root}\nPrefix: {prefix}\nIgnore: {ignore}")

    dirs = get_toplevel_directories(root, prefix, ignore)
    print(f"Directories to parse: {dirs}")
    if not args.dryrun:
        construct_tree(dirs, output)

    print()
    print("Done!") 
  
if __name__=="__main__": 
    main() 
