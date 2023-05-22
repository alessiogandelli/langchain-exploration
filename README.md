# langchain-exploration
Today I decided to explore the [langchain](https://python.langchain.com/en/latest/getting_started/getting_started.html) library, i want to use this repository to track the process from 0 to 0 + epsilon 


# Setup repo and install dependencies

i usually create an empty repository on github with gitignore with python template 
and and then clone to my dev folder, then i create a src folder for source code files and a main.py file to start coding
    
```
git clone https://github.com/alessiogandelli/langchain-exploration
cd langchain-exploration
mkdir src 
touch src/main.py
```

then i create a virtual environment and install dependencies

```
virtuelenv venv
source venv/bin/activate
pip install langchain
pip install openai
```

create a .env file sto store tokens

```
touch .env

```

Usually i work with the jupyter environment but not with notebooks but with the #%% vs code notation that allow us to run cells from a plain python file



export HNSWLIB_NO_NATIVE=1  to solve chromadb installing error 