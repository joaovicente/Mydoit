from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.lexers.data import YamlLexer
from pygments.lexers.python import PythonLexer
from pygments.formatters import TerminalFormatter
import json
import yaml
import inspect
import requests
import os


def is_dict_or_list(var):
    r"""
    Checks if var is a dictionary or a list
    :param var: The variable to test
    :return: verdict
    """
    return isinstance(var, dict) or isinstance(var, list)


def is_json(var):
    r"""
    Checks if string is valid json
    :param var: The variable to test
    :return: verdict
    """
    verdict = False
    try:
        if isinstance(var, str):
            if len(var) > 0:
                first_character = var.lstrip()[0]
                if first_character in ['{', '[']:
                    json.loads(var)
                    verdict = True
    except ValueError as e:
        verdict = False
    except TypeError as e:
        verdict = False
    return verdict


def is_yaml(var):
    r"""
    Checks if string is valid yaml
    :param var: The variable to test
    :return: verdict
    """
    verdict = False
    try:
        if isinstance(var, str) and not is_json(var):
            yaml.dump(var)
            verdict = True
    except SyntaxError as e:
        return verdict
    return verdict

def as_yaml(var):
    r"""
    Converts dictionary, list or json string to yaml string
    :param var: A dictionary, list, json string
    :return: yaml string
    """
    if is_dict_or_list(var):
        return yaml.dump(var)
    elif is_json(var):
        return yaml.dump(json.loads(var))
    elif is_yaml(var):
        return var
    else:
        return ""


def as_json(var):
    r"""
    Converts dictionary, list or yaml string to json string
    :param var: A dictionary, list, yaml string
    :return: json string
    """
    if is_dict_or_list(var):
        return json.dumps(var)
    elif is_json(var):
        return var
    elif is_yaml(var):
        return json.dumps(yaml.load(var, Loader=yaml.FullLoader))
    else:
        return ""


def as_dict(var):
    r"""
    Converts JSON to dictionary
    :param var: A JSON string
    :return: dictionary
    """
    if is_json(var):
        return json.loads(var)
    else:
        return ""


def indent(string, indent=2):
    r"""
    Indents json
    :param string: JSON string to indent
    :param indent: Number of spaces to indent JSON
    :return: json string
    """
    output = string
    if is_json(string):
        output = json.dumps(json.loads(string), indent=indent)
    return output


def mypprint(string):
    r"""
    Pretty prints dictionary, list, JSON, YAML
    :param var: The input to indent
    """
    if is_dict_or_list(string):
        # TODO: improve layout for dictionaries, using pprint library?
        mypprint(as_json(string))
    elif is_json(string):
        json_as_dict = json.loads(string)
        json_as_indented_string = json.dumps(json_as_dict, indent=2)
        print(highlight(json_as_indented_string, JsonLexer(), TerminalFormatter()))
    elif is_yaml(string):
        print(highlight(string, YamlLexer(), TerminalFormatter()))