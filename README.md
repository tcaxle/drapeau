# Drapeau
An add-on for [Chezmoi](https://github.com/twpayne/chezmoi) to synchronise your colorschemes across systems and allow easy colorscheme switching using chezmoi templates

# Installation
* Put [run_drapeau.py](run_drapeau.py) in the root of your chezmoi repository.
* Add `run_drapeau.py` to your chezmoi repository.
* Add your color schemes as [toml](https://github.com/toml-lang/toml) files in ~/.config/drapeau
* Run `# chezmoi apply`
* Edit your chezmoi config (`# chezmoi edit-config`) and change the `[drapeau]` colourscheme name to the same name as your desired colorscheme file
