#
# Copyright 2022 IBM Corp.
# SPDX-License-Identifier: Apache-2.0
#
import yaml

class Config:
    def __init__(self, config_path):
        with open(config_path, 'r') as stream:
            self.values = yaml.safe_load(stream)

    @property
    def app_uuid(self) -> str:
        return self.values.get('app-uuid', '')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
