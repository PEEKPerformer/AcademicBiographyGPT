from scholarly import scholarly
from datetime import datetime
import openai

openai.api_key = str(input("Enter OpenAI API key: "))
authoridNum = str(input("Enter Author ID: "))
authorGender = str(input('Enter Author Gender:'))
authorName = str(input('Enter Author Name:'))


def get_author_papers(author_id):
    author = scholarly.search_author_id(author_id)
    author = scholarly.fill(author)  # fill additional author info

    current_year = datetime.now().year
    ten_years_ago = current_year - 10

    publications = []

    for pub in author['publications']:
        pub = scholarly.fill(pub)  # fetch publication info
        title = pub['bib'].get('title')
        abstract = pub['bib'].get('abstract')
        pub_year = pub['bib'].get('pub_year')  # Corrected field name
        print(pub_year)

        # Only add the publication to the list if it was published in the last 10 years
        if pub_year and int(pub_year) >= ten_years_ago:
            citations = pub.get('num_citations', 0)
            publications.append((title, abstract, pub_year, citations))

    # sort by number of citations (in descending order)
    publications.sort(key=lambda x: x[3], reverse=True)

    return publications


# replace 'Author ID' with the actual author's ID
publications_data = get_author_papers(authoridNum)

# Convert list of tuples into a single string
publications_str = "\n".join([f"Title: {title}\nAbstract: {abstract}\nYear: {pub_year}\nCitations: {citations}" for
                              title, abstract, pub_year, citations in publications_data])

print(publications_str)
print('-----------------------------------')

MODEL = "gpt-3.5-turbo-16k"
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a AcademicBiographyGPT, an AI that writes academic biographies for "
                                      "researchers. You will be provided with a list of publications with abstracts, "
                                      "the year published, and the number of citations. The publications will only be "
                                      "from the past 10 years. You will write a biography for the researcher based on "
                                      "this information. Please stick to chronological order and emphasize papers "
                                      "with more citations. Tell a compelling and interesting but informative story. "
                                      "Their name is " + authorName + " and they are a " + authorGender + "Do not "
                                                                                                          "directly "
                                                                                                          "mention "
                                                                                                          "the number "
                                                                                                          "of "
                                                                                                          "citations. "
                                                                                                          "Keep it "
                                                                                                          "brief but "
                                                                                                          "informative."},
        {"role": "user", "content": publications_str},
    ],
    temperature=1,
)

print(response['choices'][0]['message']['content'])
