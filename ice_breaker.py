from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers.string import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.twitter import scrape_user_tweets
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from dotenv import load_dotenv
from output_parsers import summary_parser, Summary
from typing import Tuple

def ice_break_with(name: str) -> Tuple[Summary, str]:

    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock=True)
    linkedin_photo_url = linkedin_data.get("photoUrl")

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username, mock=True)

    summary_template = """
            given the information {information} about a person from linkedIn
            and their latest Twitter posts {twitter_posts} I want you to create:
            1. a short summary
            2. two interesting facts about them
        use both information from Twitter and LinkedIn
        \n{format_instructions}
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables = {"format_instructions": summary_parser.get_format_instructions()}
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    # llm = ChatOllama(model="mistral")
    chain = summary_prompt_template | llm | summary_parser
    res:Summary = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})
    # The placeholder image URL that we know works
    placeholder_image_url = "https://placehold.co/400x400/png"

    # Check if the LinkedIn URL is from LinkedIn's CDN
    if linkedin_photo_url and ("licdn.com" in linkedin_photo_url or "linkedin.com" in linkedin_photo_url):
        # Use placeholder instead of LinkedIn CDN URL
        return res, placeholder_image_url
    elif linkedin_photo_url:
        # Some other photo URL that might work (not from LinkedIn)
        return res, linkedin_photo_url
    else:
        # No photo URL at all
        return res, placeholder_image_url

if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter:")
    ice_break_with("Eden Marco")




