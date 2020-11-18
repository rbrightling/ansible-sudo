""" Sudo Ansible Jinja2 Filters """
import re
from ansible.parsing.yaml.objects import AnsibleUnicode


def sudo_user_spec(spec, **kwargs):
    for key, val in kwargs.items():
        spec[key] = val

    user_type = {'user': '',
                 'uid': '#',
                 'group': '%',
                 'gid': '%#',
                 'netgroup': '+',
                 'nonunix_group': '%:',
                 'nonunix_gid': '%:#'}

    if 'type' in spec:
        spec['name'] = user_type[spec['type']] + spec['name']

    if 'hosts' not in spec:
        spec['hosts'] = "ALL"
    if 'commands' not in spec:
        spec['commands'] = "ALL"

    tag_spec = []
    if 'tags' in spec:
        for tag in spec['tags']:
            tag_spec.append('{tag}:'.format(tag=tag.upper()))

    spec_format = [spec['name'], spec['hosts'], '=']

    if any(x in spec for x in ['runas_group', 'runas_user']):
        runas_format = ['(']
        if 'runas_user' in spec:
            runas_format.append(spec['runas_user'])
            if 'runas_group' in spec:
                runas_format.append(":")
        if 'runas_group' in spec:
            runas_format.append(spec['runas_group'])
        runas_format.append(')')
        spec_format.append(''.join(runas_format))

    spec_format.append(' '.join(tag_spec))
    if type(spec['commands']) is list:
        spec_format.append(', '.join(spec['commands']))
    else:
        spec_format.append(spec['commands'])

    return ' '.join(spec_format)


def sudo_alias(alias_list):
    if type(alias_list) is list:
        return ", ".join(alias_list)
    else:
        return alias_list


def sudo_default_parameter(option, value):
    if value is True:
        parameter = option
    elif value is False:
        parameter = "!{option}".format(option=option)
    elif type(value) is str or type(value) is AnsibleUnicode:
        m = re.findall(r'([\+|\-]\=\S+)', value)
        if m:
            join_string = ", {option}".format(option=option)
            parameter = option + join_string.join(m)
        else:
            parameter = "{option}={value}".format(
                option=option, value=value)
    elif type(value) is list:
        set_values, add_values, del_values = [], [], []
        for item in value:
            if item.startswith('+'):
                add_values.append(item[1:])
            elif item.startswith('-'):
                del_values.append(item[1:])
            else:
                set_values.append(item)

        parameter = []

        if set_values:
            parameter.append(
                "{option}={value}".format(
                    option=option, value=":".join(set_values)))

        if add_values:
            parameter.append("{option}+={value}".format(
                option=option, value=":".join(add_values)))

        if del_values:
            parameter.append("{option}-={value}".format(
                option=option, value=":".join(del_values)))
        parameter = ", ".join(parameter)
    return parameter


class FilterModule(object):

    def filters(self):
        return {
            'sudo_user_spec': sudo_user_spec,
            'sudo_default_parameter': sudo_default_parameter,
            'sudo_alias': sudo_alias
        }
