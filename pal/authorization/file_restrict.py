#!/usr/bin/env python3
import pal.config.defaults as defaults
import yaml


def can_access(username, bucket, key):
    with open(defaults.RESTRICT_CONFIG_FILEPATH, 'r+') as file:
        try:
            config_map = yaml.load(file)
            return __config_exists(config_map, username, bucket, key)
        except yaml.YAMLError as exc:
            print(exc)
        except FileNotFoundError as error:
            print("Configuration File not Found", error)
    return "stub"


def add_restrict(username, bucket, key):
    with open(defaults.RESTRICT_CONFIG_FILEPATH, 'w+') as file:
        try:
            config_map = yaml.load(file)
            new_map = __write_config(config_map, username, bucket, key)
            yaml.dump(new_map, file)
            return "Restriction has been added"
        except yaml.YAMLError as exc:
            print(exc)
        except FileNotFoundError as error:
            print("Configuration File not Found", error)
    return "stub"


def remove_restrict(username, bucket, key):
    with open(defaults.RESTRICT_CONFIG_FILEPATH, 'r+') as file:
        try:
            config_map = yaml.load(file)
            if __config_exists(config_map, username, bucket, key):
                del config_map[bucket][key][username]
            yaml.dump(config_map, file)
            return "Restriction has been removed"
        except yaml.YAMLError as exc:
            print(exc)
        except FileNotFoundError as error:
            print("Configuration File not Found", error)

    return "stub"


def __delete_config(config_map, username, bucket, key):
    if config_map is None:
        return config_map
    if bucket not in config_map:
        return config_map
    if key not in config_map[bucket]:
        return config_map
    if username in config_map[bucket][key]:
        del config_map[bucket][key][username]
    return config_map


def __write_config(config_map, username, bucket, key):
    if config_map is None:
        config_map = dict()
    if bucket not in config_map:
        config_map[bucket] = dict()
    if key not in config_map[bucket]:
        config_map[bucket][key] = dict()
    if username not in config_map[bucket][key]:
        config_map[bucket][key][username] = True
    return config_map


def __config_exists(config_map, username, bucket, key):
    if config_map is None:
        return False
    if bucket not in config_map:
        return False
    if key not in config_map[bucket]:
        return False
    if username not in config_map[bucket][key]:
        return False
    return True