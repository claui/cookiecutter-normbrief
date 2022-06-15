# pylint: disable=pointless-string-statement

"""
# After abandoning support for Cookiecutter 1.x, maybe write
# a custom Jinja extension that provides a `startswith` test.
# Usage examples:

cookiecutter.items()
    | selectattr(0, 'startswith', 'author_postal_address_line_')
    | sort(attribute=0)

cookiecutter.items()
    | selectattr(0, 'startswith', 'recipient_postal_address_line_')
    | sort(attribute=0)
"""

"""
{%
    set author_postal_address = [
        cookiecutter.author_postal_address_line_1,
        cookiecutter.author_postal_address_line_2,
        cookiecutter.author_postal_address_line_3,
    ] | map("string") | reject("eq", "") | list
%}
{%
    set recipient_postal_address = [
        cookiecutter.recipient_postal_address_line_1,
        cookiecutter.recipient_postal_address_line_2,
        cookiecutter.recipient_postal_address_line_3,
    ] | map("string") | reject("eq", "") | list
%}
{{
    cookiecutter.update({
        "author_postal_address": author_postal_address,
        "recipient_postal_address": recipient_postal_address,
    })
}}
"""
