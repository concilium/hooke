# Notes on development.

## Installed pyenv and pyenv-virtualenv using administrator account.

    % sudo su - mgsimpson

        % brew update
        % brew install pyenv
        % brew install pyenv-virtualenv
        % exit

## Installed Python 3.5 under local account.

    % vi .zshrc

        [ added magic lines to startup file and re-started terminal ]

    % pyenv install 3.5.1
    
## Created project-specific virtual environment.
    
    % pyenv virtualenv 3.5.1 s9-concilium-hooke
    % pyenv global s9-concilium-hooke
    % pip install Flask
    % pyenv global system

## Initialized project directory.

    % cd ~/Desktop/Projects
    % mkdir s9-concilium-hooke
    % cd s9-concilium-hooke
    % pyenv local s9-concilium-hooke
    % git init
    % vi .gitignore

        [ added .python-version to .gitignore file ]

    % git add DEVELOPERS.md .gitignore
    % git commit -m “Initial commit with developers notes.”
