from langchain_community.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv


load_dotenv()
#Career Advice
llm=openai.OpenAI(temperature=0.5)

prompt_temp = PromptTemplate(
    input_variables=["degree"],
    template='''I am a career advisor. I help people find the right career path. 
    I have a client who has a degree in {degree}. What career path would you recommend for them?
    Format it as bullet points.''' 
)
chain = LLMChain(llm=llm, prompt=prompt_temp)
response = chain({'degree':'pure science'})

print(response)
