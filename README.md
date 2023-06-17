# AcademicBiographyGPT ReadMe

## Description

This Python script is designed to generate an academic biography of a researcher based on their recent papers from the last decade. It uses the `scholarly` library to fetch the researcher's papers, and OpenAI's GPT-3.5-turbo-16k model to write the biography. Other models should be fine depending on number of papers. The prompt can be modified to meet your needs.

## Prerequisites

The following Python libraries are required:

- `scholarly`
- `datetime`
- `openai`

Install them using pip:

```
pip install scholarly datetime openai
```

Also, you need to have an `OpenAI API key` which you can get from [OpenAI's website](https://www.openai.com/).

## Usage

To run the program, simply execute the Python script:

```
python your_script_name.py
```

Upon execution, the script will ask for the following inputs:

- `Enter OpenAI API key:` Here you should enter your OpenAI API key.
- `Enter Author ID:` Here you need to provide the Google Scholar ID of the author. This can be found in the URL of the profile after 'user='.
- `Enter Author Gender:` Specify the gender of the author for the biography.
- `Enter Author Name:` Input the full name of the author.

After providing the necessary inputs, the program will fetch the author's publications from the last 10 years, sort them by citation count, and generate an academic biography based on the fetched information.

The output of the script will be printed in the console. It consists of the author's publications' details (Title, Abstract, Year, Citations) followed by the generated biography.

## License

This project is licensed under the terms of the GPL 3.0 license.
