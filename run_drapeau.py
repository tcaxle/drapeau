#!/usr/bin/python
import os
import toml

def main():
    # Chech if config file exists
    chezmoi_config_dir = os.path.join(os.environ["HOME"], ".config", "chezmoi")
    if os.path.exists(os.path.join(chezmoi_config_dir, "chezmoi.toml")):
        chezmoi_config_file = os.path.join(chezmoi_config_dir, "chezmoi.toml")
    else:
        return "=== ERROR: No chezmoi.toml found ==="

    # Load config file into memory
    chezmoi_config_dict = toml.load(chezmoi_config_file)

    # Extract drapeau data
    if "drapeau" not in chezmoi_config_dict["data"]:
        chezmoi_config_dict["data"]["drapeau"] = {}

    # Get colorscheme
    if "colorscheme" in chezmoi_config_dict["data"]["drapeau"]:
        drapeau_color_scheme = chezmoi_config_dict["data"]["drapeau"]["colorscheme"]
    else:
        drapeau_color_scheme = "default"
        chezmoi_config_dict["data"]["drapeau"]["colorscheme"] = drapeau_color_scheme

    # Find colorscheme files
    # Produce dict of {"name": "path"} for all schemes
    drapeau_config_dir = os.path.join(os.environ["HOME"], ".config", "drapeau")
    if os.path.exists(drapeau_config_dir):
        drapeau_color_scheme_files = {".".join(scheme.split(".")[:-1]): os.path.join(drapeau_config_dir, scheme) for scheme in os.listdir(drapeau_config_dir) if os.path.isfile(os.path.join(drapeau_config_dir, scheme))}
    else:
        drapeau_color_scheme_files = {}

    # Extract colorscheme data from desired scheme
    drapeau_color_scheme_dict = toml.load(drapeau_color_scheme_files[drapeau_color_scheme])

    # Add colorscheme to chezmoi config data
    chezmoi_config_dict["data"]["drapeau"]["colors"] = drapeau_color_scheme_dict

    # Write out modified dict to chezmoi config file
    with open(chezmoi_config_file, 'w') as f:
        toml.dump(chezmoi_config_dict, f)

    return "=== SUCCESS ==="

main()
