def get_calc_policy(build_name):
    if build_name == "calculator":
        return "py_library"
    else:
        return ""