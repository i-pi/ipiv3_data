def recursive_copy(source_dict: dict, target_dict: dict) -> dict:
    """
    Recursively copy keys and values from a source dictionary to a target dictionary, if they are not present in the target.

    This function takes two dictionaries, 'source_dict' and 'target_dict', and copies keys and values from 'source_dict' to 'target_dict'. If a key exists in both dictionaries and both values are dictionaries, the function recursively calls itself to copy nested keys and values. If a key does not exist in 'target_dict', it is added along with its corresponding value from 'source_dict'.

    Args:
        source_dict (dict): The source dictionary containing keys and values to be copied.
        target_dict (dict): The target dictionary to which keys and values are copied if missing.

    Returns:
        dict: The modified 'target_dict' with keys and values copied from 'source_dict'.

    Example:
        >>> dict_A = {"a": 1, "b": {"b1": 2, "b2": {"b2_1": 3}}, "c": 4}
        >>> dict_B = {"a": 10, "b": {"b1": 20, "b2": {"b2_2": 30}}, "d": 40}
        >>> result = recursive_copy(dict_A, dict_B)
        >>> print(result)
        {'a': 10, 'b': {'b1': 20, 'b2': {'b2_1': 3, 'b2_2': 30}}, 'd': 40}
    """
    for key, value in source_dict.items():
        if (
            isinstance(value, dict)
            and key in target_dict
            and isinstance(target_dict[key], dict)
        ):
            recursive_copy(value, target_dict[key])
        else:
            if key not in target_dict:
                target_dict[key] = value
    return target_dict


def add_default(dictionary: dict = None, default: dict = None) -> dict:
    """
    Add default key-value pairs to a dictionary if they are not present.

    This function takes two dictionaries: 'dictionary' and 'default'. It checks each key in the 'default' dictionary, and if the key is not already present in the 'dictionary', it is added along with its corresponding value from the 'default' dictionary. If 'dictionary' is not provided, an empty dictionary is used as the base.

    Args:
        dictionary (dict, optional): The input dictionary to which default values are added. If None, an empty dictionary is used. Default is None.
        default (dict): A dictionary containing the default key-value pairs to be added to 'dictionary'.

    Returns:
        dict: The modified 'dictionary' with default values added.

    Raises:
        ValueError: If 'dictionary' is not of type 'dict'.

    Example:
        >>> existing_dict = {'a': 1, 'b': 2}
        >>> default_values = {'b': 0, 'c': 3}
        >>> result = add_default(existing_dict, default_values)
        >>> print(result)
        {'a': 1, 'b': 2, 'c': 3}
    """
    if dictionary is None:
        dictionary = {}

    if not isinstance(dictionary, dict):
        raise ValueError("'dictionary' has to be of 'dict' type")

    return recursive_copy(source_dict=default, target_dict=dictionary)

def straigh_line(ax,shift,get_lim,func,set_lim,**argv):

    default = {"color": "black", "alpha": 0.5, "linestyle": "dashed"}
    argv = add_default(argv,default)

    xlim = get_lim()
    
    func(shift,xlim[0],xlim[1],**argv)

    set_lim(xlim[0],xlim[1])

    return ax

def hzero(ax, shift=0, **argv):
    return straigh_line(ax,shift,ax.get_xlim,ax.hlines,ax.set_xlim,**argv)

def vzero(ax, shift=0, **argv):
    return straigh_line(ax,shift,ax.get_ylim,ax.vlines,ax.set_ylim,**argv)

def remove_empty_space(ax):
    """
    Adjusts the x-axis limits (xlim) of the given axis according to the minimum and maximum values encountered in the plotted data.

    Parameters:
        ax (matplotlib.axes.Axes): The axis to adjust the x-axis limits for.
    """
    # Get the lines plotted on the axis
    lines = ax.get_lines()

    # Initialize min and max values with the first line's data
    min_x, max_x = lines[0].get_xdata().min(), lines[0].get_xdata().max()

    # Iterate over the rest of the lines to find the overall min and max values
    for line in lines[1:]:
        min_x = min(min_x, line.get_xdata().min())
        max_x = max(max_x, line.get_xdata().max())

    # Set the x-axis limits accordingly
    ax.set_xlim(min_x, max_x)
