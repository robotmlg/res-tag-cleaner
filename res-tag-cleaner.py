'''
Removes all non-tagged users from your RES tags file

Retrieve your tags by pulling up the RES console with . (the period key)
Enter 'RESStorage update RESmodules.userTagger.tags'
Copy the text in the box to a text file and save it

Usage: python3 res-tag-cleaner.py <input file> <output file>
'''
import sys
import json


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 res-tag-cleaner.py <input file> <output file>")
        return

    tags_in_filename = sys.argv[1]
    tags_out_filename = sys.argv[2]

    try:
        tags_in_file = open(tags_in_filename, 'r')
    except:
        print("Unable to open input file " + tags_in_filename)
        return

    try:
        tags_in_str = tags_in_file.read()
    except:
        print("Unable to read input file " + tags_in_filename)
        return

    tags_in_file.close()

    tags_in_json = json.loads(tags_in_str)
    tags_out_json = {}

    for user in tags_in_json:
        if "tag" in tags_in_json[user]:
            tags_out_json[user] = tags_in_json[user]

    tags_out_str = json.dumps(tags_out_json)

    try:
        tags_out_file = open(tags_out_filename, 'w')
    except:
        print("Unable to open output file " + tags_out_filename)
        return

    try:
        tags_out_file.write(tags_out_str)
    except:
        print("Unable to write to output file " + tags_out_filename)
        return

    tags_out_file.close()


if __name__ == "__main__":
    main()
