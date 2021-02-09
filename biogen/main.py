import sys
import os
import re
import argparse
import yaml
import jinja2
from pprint import pprint
from docxtpl import DocxTemplate
from docx.shared import Mm

from .portrait import VersentInlinePortrait

CONFIG_FILE = 'biogen.yaml'
PORTRAIT_FILE_PREFIX = 'portrait'


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate your Versent Bio from a config file')
    parser.add_argument('--config', '-c', dest='config_file',
                        type=str, default=CONFIG_FILE)
    parser.add_argument('--portrait', '-p', dest='image_file',
                        type=str, default=PORTRAIT_FILE_PREFIX)
    return parser.parse_args()


def load_config(config_file=CONFIG_FILE, **kwargs):
    if os.path.exists(config_file):
        with open(config_file) as config_fh:
            config = yaml.load(config_fh, Loader=yaml.FullLoader)
        for skill in config['skills']:
            skill['sub_skills'] = ', '.join(skill.get('skills', []))
        return config
    else:
        print(f'No {config_file} found in current directory')
        sys.exit(1)


def load_image(template, image_file=PORTRAIT_FILE_PREFIX, **kwargs):
    if image_file == PORTRAIT_FILE_PREFIX:
        for ext in ('jpg', 'jpeg', 'png'):
            image_file = f'{image_file}.{ext}'
            if os.path.exists(image_file):
                break
        else:
            print(f'No portrait image file found')
            sys.exit(1)
    elif not os.path.exists(image_file):
        print(f'Portrait file `{image_file}` not found')
    return VersentInlinePortrait(template, image_file, width=Mm(66))


def get_template_doc(template_path):
    if os.path.basename(template_path) == template_path:
        template_path = os.path.join(os.path.dirname(
            __file__), 'templates', template_path)
    return DocxTemplate(template_path)


def main():
    options = parse_args().__dict__
    config = load_config(**options)
    template = get_template_doc(f"{config['template']}.docx")

    portrait = load_image(template, **options)
    config['portrait'] = portrait

    try:
        template.render(config)
    except jinja2.exceptions.UndefinedError as e:
        print(f'There is something missing from your biogen.yaml: {e}')
        sys.exit()

    output_filename = '{first_name} {last_name} - {current_role}.docx'.format(**config)
    template.save(output_filename)
    print(f'Generated {output_filename}')
