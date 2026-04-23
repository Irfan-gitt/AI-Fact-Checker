from django.shortcuts import render
from ddgs import DDGS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("API"))


def search(query):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query + "fact check", max_results=5):
            results.append(
                f"Title: {r['title']}\nSummary: {r['body']}\nSource: {r['href']}")
    return "\n\n".join(results)


def check_claim(claim):
    search_result = search(claim)

    prompt = f"""You are a fact checker. A user made the following claim verify it and give a relevent answers:

CLAIM:{claim}

Here are the search results from the web about this claim:
{search_result}

Based on the search results above, analyze the claim and respond with:
1. VERDICT: TRUE / FALSE / UNVERIFIED / MISLEADING / FAKE
2. EXPLANATION: explanation must be good and try to add major informations can be long and relevant to the claim and the search results. If the claim is false or misleading, explain why and provide evidence from the search results. If the claim is true, explain why and provide evidence from the search results. If the claim is unverified, explain what information is missing and what would be needed to verify it. If the claim is fake, explain why it is fake and provide evidence from the search results. 
3. SOURCES: list the relevant sources as plain URLs

And things must be in arrnged manner like real ai applications now days can give spaces between VERDICT and EXPLANATION sessions
Be honest and objective."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def home(request):
    result = None
    if request.method == 'POST':
        claim = request.POST.get("claim")

        if claim:
            result = check_claim(claim).strip()

    context = {'result': result}

    return render(request, 'checker/home.html', context)
