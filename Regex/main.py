from pprint import pprint
from defs import join_duplicate_name, result_file_writer


if __name__ == '__main__':
  pprint(join_duplicate_name(), width=300)
  result_file_writer()