# Drapeau
An add-on for [Chezmoi](https://github.com/twpayne/chezmoi) to synchronise your colorschemes across systems and allow easy colorscheme switching using chezmoi templates

# Use
* Put [run_drapeau.py](run_drapeau.py) in the root of your chezmoi repository.
* Add `run_drapeau.py` to your chezmoi repository.
* Add your color schemes as [toml](https://github.com/toml-lang/toml) files in `~/.config/drapeau`
* Run `# chezmoi add ~/.config/drapeau/*` to track your colorschemes with chezmoi
* Run `# chezmoi apply`
* Edit your chezmoi config (`# chezmoi edit-config`) and change the `[data.drapeau]` colorscheme name to the same name as your desired colorscheme file (by default it will look for a colourscheme named `default.toml`)
* Convert any files managed by chezmoi to [templates](https://github.com/twpayne/chezmoi/blob/master/docs/HOWTO.md#use-templates-to-manage-files-that-vary-from-machine-to-machine) using `# chezmoi add --template /path/to/file`
* Replace all colours you wish to be in line with your colorscheme with tempate tags in the form `{{ .drapeau.colors.color10 }}` or `{{ .drapeau.colors.l_green }}` (or if you have used a different naming scheme for your colors, use `{{ .drapeau.colors.your_color_name_here }}`)
* Run `# chezmoi apply` any time you make any changes to colorschemes and all of your config files will update too

# Example Colorschemes
Example colorschemes can be found in the examples folder.
