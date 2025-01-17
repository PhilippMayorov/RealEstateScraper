from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# prompt template for the LLM to follow and extract information with
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# initialize the Ollama model
model = OllamaLLM(model="llama3.2:1b")

def parse_with_ollama(dom_chunks, description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):

        # invoke the model with the current chunk and description
        response = chain.invoke({"dom_content": chunk, "parse_description": description})
        print(f"Parsed batch {i} of {len(dom_chunks)}")

        # append LLM response to the list of parsed results
        parsed_results.append(response)

    return "\n".join(parsed_results)