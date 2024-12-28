import click
import json
import os
import random


# Load all the data from the json files
data = {}
for filename in os.listdir(os.getcwd() + "/data"):
    if filename.endswith(".json"):
        data[filename[:-5]] = json.load(open("data/" + filename))


@click.command()
def find():
    """Simple program that generates a single item of loot."""
    click.echo("You found:")
    item = get_item()
    name = parse_name_vars(item["name"])
    click.echo(name)
    if "desc" in item.keys():
        desc = parse_desc_vars(item["desc"])
        click.echo(desc)


def get_item(list_name="master"):
    item = choose(data[list_name])
    if "name" in item:
        if item["name"].startswith("$$"):
            item = get_item(item["name"][2:-2])
    return item


def parse_desc_vars(string):
    """Parses a string and replaces any variables in the form of %%var%% with a
    value from the table of the same name."""
    while r"%%" in string:
        start = string.index(r"%%")
        end = string.index(r"%%", start + 1)
        var_name = string[start + 2 : end]
        value = get_item(var_name)["desc"]
        string = string[:start] + value + string[end + 2 :]
    return string


def parse_name_vars(string):
    """Parses a string and replaces any variables in the form of %%var%% with a
    value from the table of the same name."""
    while r"%%" in string:
        start = string.index(r"%%")
        end = string.index(r"%%", start + 1)
        var_name = string[start + 2 : end]
        value = get_item(var_name)["name"]
        string = string[:start] + value + string[end + 2 :]
    return string


def choose(loot_table):
    """Chooses a random item from a loot table list object. Each entry in the
    table must have a 'prob' key that is a float between 0 and 1."""

    # Get the total probability of all items in the table
    total_prob = sum([item["prob"] for item in loot_table])

    # Choose a random number between 0 and the total probability
    choice = random.random() * total_prob

    # Loop through the items in the table and subtract their probability from
    # the choice until we find the chosen item
    for item in loot_table:
        choice -= item["prob"]
        if choice <= 0:
            return item


if __name__ == "__main__":
    find()
