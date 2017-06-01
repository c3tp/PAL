#!/usr/bin/env python
"Module for reading configs from files"

import os
import yaml
import pal.config.defaults as defaults


def read_config():
    "Reads the configs for the project from some file"
    config_map = None
    with open(defaults.CONFIG_FILEPATH, 'r') as stream:
        try:
            config_map = yaml.load(stream)
            print(config_map)
        except yaml.YAMLError as exc:
            print(exc)
        except FileNotFoundError as error:
            print("Configuration File not Found", error)

    return config_map
