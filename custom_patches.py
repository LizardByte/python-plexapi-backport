# -*- coding: utf-8 -*-

# standard imports
import argparse
import re

# lib imports
from typing import List


def get_indentation(line):
    # type: (str) -> str
    """
    Get the leading whitespace of a line.

    Parameters
    ----------
    line : str
        A line from the file.

    Returns
    -------
    str
        The leading whitespace of the line.
    """
    return line[:len(line) - len(line.lstrip())]


def arg_unpack_patch(lines):
    # type: (List[str]) -> List[str]
    """
    Patch `**variable or {}` to be `**(variable or {})`.

    Parameters
    ----------
    lines : List[str]
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    pattern = r'\*\*(\w+ or \{\})'

    for i, line in enumerate(lines):
        matches = re.findall(pattern, line)
        for match in matches:
            lines[i] = line.replace("**{}".format(match), "**({})".format(match))

    return lines


def backport_import_patch(lines):
    """
    Apply patches required from plexapi_backports.py (plexapi.backports).

    This patch applies necessary imports and function replacements to make the code compatible with Python 2.7.

    Parameters
    ----------
    lines
        The lines of the file.

    Returns
    -------
    list[str]
        Updated lines.
    """
    patterns = {
        'glob': {
            'original_import': 'from glob import glob',
            'new_import': 'from plexapi.backports import glob',
            'function': 'glob',
            'replace_function': False,
        },
        'makedirs': {
            'original_import': 'from os import makedirs',
            'new_import': 'from plexapi.backports import makedirs',
            'function': 'makedirs',
            'replace_function': False,
        },
        'normalize': {
            'original_import': 'from unicodedata import normalize',
            'new_import': 'from plexapi.backports import unicodedata_normalize',
            'function': 'unicodedata_normalize',
            'replace_function': True,
        },
        'glob.glob': {
            'new_import': 'from plexapi.backports import glob',
            'function': 'glob',
            'replace_function': True,
        },
        'os.makedirs': {
            'new_import': 'from plexapi.backports import makedirs',
            'function': 'makedirs',
            'replace_function': True,
        },
        'unicodedata.normalize': {
            'new_import': 'from plexapi.backports import unicodedata_normalize',
            'function': 'unicodedata_normalize',
            'replace_function': True,
        }
    }

    output_lines = lines[:]
    added_imports = set()

    for idx, line in enumerate(output_lines):
        for pattern, details in patterns.items():
            # If we find an original import, replace it with the new import
            if 'original_import' in details and details['original_import'] == line.strip():
                output_lines[idx] = details['new_import'] + '\n'
                break  # Break out of the inner loop; we've made a replacement

            # If the pattern is in the line and the function needs to be replaced, replace it
            if details['replace_function']:
                # Check for the pattern as a function (with an opening parenthesis following it)
                pattern_as_function = pattern + '('
                if pattern_as_function in line:
                    output_lines[idx] = line.replace(pattern_as_function, details['function'] + '(')
                    added_imports.add(details['new_import'])

    # Find the position to insert the new imports: directly after the last top-level import block
    insert_position = 0
    inside_multiline_import = False
    for idx, line in enumerate(output_lines):
        trimmed_line = line.strip()
        if trimmed_line and not trimmed_line.startswith(
                ('import ', 'from ', '#', '"', "'")) and not inside_multiline_import:
            break  # End of header/comments found
        if trimmed_line.startswith(('import ', 'from ')):
            insert_position = idx + 1
        # Check for multiline imports
        if '(' in line:
            inside_multiline_import = True
        if ')' in line:
            inside_multiline_import = False

    # Insert the imports in reverse order to maintain order
    for added_import in reversed(list(added_imports)):
        if added_import not in output_lines:
            output_lines.insert(insert_position, added_import + '\n')
            insert_position += 1  # Update the insertion point for the next import

    return output_lines


def cached_property_patch(lines):
    # type: (List[str]) -> List[str]
    """
    Patch cached_property to be compatible with Python 2.7.

    If the file contains `from functools import cached_property`, then this function will replace it.

    Parameters
    ----------
    lines : List[str]
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    target_line = "from functools import cached_property"
    replacement = """try:
    from functools import cached_property
except ImportError:
    from cached_property import cached_property
"""

    for i, line in enumerate(lines):
        if line.strip() == target_line:
            indentation = get_indentation(line)
            indented_replacement = '\n'.join(
                ['{}{}'.format(indentation, sub_line) for sub_line in replacement.split('\n')])
            lines[i] = indented_replacement

    return lines


def pathlib_patch(lines):
    # type: (List[str]) -> List[str]
    """
    Patch pathlib to be compatible with Python 2.7.

    If the file contains `from pathlib import Path`, then this function will replace it.

    Parameters
    ----------
    lines : List[str]
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    target_line = "from pathlib import Path"
    replacement = """try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path
"""

    for i, line in enumerate(lines):
        if line.strip() == target_line:
            indentation = get_indentation(line)
            indented_replacement = '\n'.join(
                ['{}{}'.format(indentation, sub_line) for sub_line in replacement.split('\n')])
            lines[i] = indented_replacement

    return lines


def raise_from_none_patch(lines):
    # type: (List[str]) -> List[str]
    """
    Patch `raise from None` to be compatible with Python 2.7.

    If the file contains `raise() from None`, then this function will remove the `from None`.

    Parameters
    ----------
    lines : List[str]
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    target = ") from None"
    replacement = ")"

    for i, line in enumerate(lines):
        if line.rstrip().endswith(target):
            # Remove the `from None` part
            lines[i] = line.rstrip().replace(target, replacement) + '\n'

    return lines


def remove_trailing_commas(lines):
    """
    Remove the trailing comma from function definitions, when there is a trailing comma after **kwargs.

    Parameters
    ----------
    lines : List[str]
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    for i in range(len(lines) - 1):
        line = lines[i].rstrip()
        next_line = lines[i + 1].strip()

        # Handle multiline function definitions
        if line.endswith('**kwargs,') and next_line == '):':
            lines[i] = line[:-1] + '\n'

    return lines


def shutil_which_patch(lines):
    # type: (List[str]) -> List[str]
    """
    Patch `from shutil import which` to be compatible with Python 2.7.

    If the file contains `from shutil import which`, then this function will replace it with a try-except block.

    Parameters
    ----------
    lines : List[str]
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    modified_lines = []

    # Regular expression to detect the import pattern for shutil
    shutil_import_pattern = re.compile(r'from shutil import (?P<imports>.+)')

    i = 0
    while i < len(lines):
        line = lines[i]
        match = shutil_import_pattern.search(line)

        if match:
            # Extract imports from the match
            imported_items = match.group('imports').split(',')
            imported_items = [item.strip() for item in imported_items]

            # If 'which' is among the imported items
            if 'which' in imported_items:
                # Remove 'which' from the list
                imported_items.remove('which')

                # Update the import statement without 'which'
                if imported_items:
                    remaining_imports = ', '.join(imported_items)
                    modified_lines.append('from shutil import {}\n'.format(remaining_imports))
                else:
                    # If no other imports alongside 'which', we skip adding the import line for shutil
                    pass

                # Add the try-except block after the import statement
                try_except_block = [
                    'try:\n',
                    '    from shutil import which\n',
                    'except ImportError:\n',
                    '    from backports.shutil_which import which\n'
                ]
                modified_lines.extend(try_except_block)

                # Increment the counter to skip the current line as it has been processed
                i += 1
                continue

        # If no matching pattern, append the original line
        modified_lines.append(line)  # The line should already have a trailing newline
        i += 1

    return modified_lines


def super_patch(lines):
    # type: (List[str]) -> List[str]
    """
    Patch `super()` to be compatible with Python 2.7.

    If the file contains `super()`, then this function will replace it with `super(CurrentClass, self)`.

    Parameters
    ----------
    lines : List[str]
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    # Copy the lines to avoid in-place modification issues
    output_lines = lines[:]

    # Regular expression to detect a class definition
    class_pattern = re.compile(r'^\s*class\s+(?P<classname>\w+)')

    # Regular expression to detect super() usage
    super_pattern = re.compile(r'super\(\)')

    # Placeholder for detected class name
    current_class = None

    for i, line in enumerate(output_lines):
        # Detect if current line is a class definition and capture class name
        class_match = class_pattern.search(line)
        if class_match:
            current_class = class_match.group('classname')

        # Detect if super() is used in this line
        super_match = super_pattern.search(line)
        if super_match and current_class:
            # Replace super() with super(CurrentClass, self)
            output_lines[i] = line.replace('super()', 'super({}, self)'.format(current_class))

    return output_lines


def urllib_imports_patch(lines):
    # type: (List[str]) -> List[str]
    """
    Patch urllib imports to be compatible with Python 2.7.

    If the file contains `from urllib.parse import`, then this function will replace it with
    `from six.moves.urllib.parse import`.

    Parameters
    ----------
    lines
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    patched_lines = []

    for line in lines:
        if 'from urllib.parse import' in line:
            # Just replace the original module path with six.moves
            new_import_line = line.replace('from urllib.parse', 'from six.moves.urllib.parse')
            patched_lines.append(new_import_line)
        else:
            patched_lines.append(line)

    return patched_lines


def yield_from_patch(lines):
    # type: (List[str]) -> List[str]
    """
    Patch `yield from` to be compatible with Python 2.7.

    If the file contains `yield from`, then this function will replace it with an explicit loop.

    Parameters
    ----------
    lines : List[str]
        The lines of the file.

    Returns
    -------
    List[str]
        Updated lines.
    """
    # Copy the lines to avoid in-place modification issues
    output_lines = lines[:]

    # Regular expression to detect the yield from pattern
    yield_from_pattern = re.compile(r'\s*yield from (?P<iterable>[\w.]+)')

    for i, line in enumerate(output_lines):
        # Detect if 'yield from' is used in this line
        match = yield_from_pattern.search(line)
        if match:
            # Extract the iterable name from the match
            iterable = match.group('iterable')

            # Find the indentation of the current line
            indentation = len(line) - len(line.lstrip())
            spaces = ' ' * indentation

            # Create the explicit loop replacement
            loop_start = ("{spaces}for _plexapi_backport_yield in {iterable}:".format(spaces=spaces, iterable=iterable))
            yield_statement = "{spaces}    yield _plexapi_backport_yield".format(spaces=spaces)

            replacement = '{}\n{}\n'.format(loop_start, yield_statement)

            output_lines[i] = replacement

    return output_lines


def process_file(file_path):
    # type: (str) -> List[str]
    """
    Process the file to apply all patches.

    Parameters
    ----------
    file_path : str
        The path to the file to process.

    Returns
    -------
    List[str]
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Apply patches
    lines = backport_import_patch(lines=lines)

    lines = arg_unpack_patch(lines=lines)
    lines = raise_from_none_patch(lines=lines)
    lines = remove_trailing_commas(lines=lines)
    lines = super_patch(lines=lines)
    lines = urllib_imports_patch(lines=lines)
    lines = yield_from_patch(lines=lines)

    # these are last because they mess with indentation of imports
    lines = cached_property_patch(lines=lines)
    lines = pathlib_patch(lines=lines)
    lines = shutil_which_patch(lines=lines)

    with open(file_path, 'w') as f:
        f.writelines(lines)

    return lines


if __name__ == '__main__':
    # setup argument parser
    parser = argparse.ArgumentParser(description='Patch Python 3.x files to be compatible with Python 2.7')
    parser.add_argument('file_path', type=str, help='The file to patch')
    args = parser.parse_args()

    process_file(file_path=args.file_path)
    print("Finished processing: {}".format(args.file_path))
