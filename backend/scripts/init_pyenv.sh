#!/usr/bin/env bash


# Install pyenv if not already installed
if [ ! -d "$HOME/.pyenv" ]; then
  curl https://pyenv.run | bash

  # Add pyenv to PATH
  echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
fi

# Add pyenv to PATH
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Install python version
make pyenv
# Activate pyenv
pyenv activate
# Install dependencies
make install-dev-deps