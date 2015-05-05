"""
TODO: add comments
"""
from command import Command
from tow import templates
import os
from datetime import date
from utils import print_warning
from utils import print_ok
from utils import yes_no_all_prompt
from utils import answer


class CreateCommand(Command):

    def add_parser(self, subparsers):
        super(CreateCommand, self).add_parser(subparsers)
        parser = subparsers.add_parser("create",
                                       help="Create tow project in current \
                                       directory")
        parser.add_argument("project_name", type=str,
                            help="name of tow project")
        parser.add_argument("-f", "--force",
                            action='store_true',
                            help="Override project if already exists")

    def command(self, namespace, args):
        project_name = namespace.project_name
        override_all = namespace.force
        for dir_name in ["attributes", "files", "templates"]:
            dir_path = os.path.join(project_name, dir_name)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
        for file_name in ["Dockerfile", "mapping.py", "attributes/default.py"]:
            file_path = os.path.join(project_name, file_name)
            process_tmpl = True
            if not override_all:
                if os.path.exists(file_path):
                    ans = yes_no_all_prompt(
                        "Overwrite %s? [y/N/a]: " % file_path)
                    if ans == answer.YES:
                        print_warning("Overriding %s" % file_path)
                    elif ans == answer.ALL:
                        override_all = True
                    elif ans == answer.NO:
                        process_tmpl = False
                else:
                    print_ok("Creating %s" % file_path)
            else:
                print_warning("Overriding %s" % file_path)
            if process_tmpl or override_all:
                templates.process_template(
                    "%s.tmpl" % os.path.basename(file_name),
                    file_path,
                    {"current_year": date.today().year,
                    "project_name": project_name})
