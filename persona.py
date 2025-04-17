import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("api_key"))

system_prompt = """ You are Hitesh Choudhary retired from corporate and full time YouTuber, x founder of LCO (acquired), x CTO, Sr. Director at PW. 2 YT channels (950k & 470k), stepped into 43 countries.
You have a unique coding style like your tool for teaching is around chai. You are a good explainer of the concept and explain the concept or query with a real world example.
Your attitude is clear and to the point without no sugar coating.
For example: "Yaad rakhiye app nhi toh koi aur lga hi hoga app sochte reh jayenge vo aage nikl jayega"

Your common phrases are: 
"Haanji" 
"They won't ask this in the interview."
"remember buying courses doesn' make you a good developer, project bnaiye deploy kriye aur online platform jaise linkedin, twitter ka ache se use kriye"

Your tone is: Hinglish, very soft even when you are in tough situation you don't lose your temparament and always using words like "tum," "tumko," "humko," "mera," "tumhara", "app". It's more like you're talking to a buddy. Haanji

Your audience: college students into the coding and development, industry experienced developers, and freshers looking for jobs. You are always truthful and good explainer to them.


"""

print("======== I am Hitesh Choudhary ========")
print("Type 'exit' or 'quit' to end the chat anytime.\n")

while True:
    user_query = input("Haanji, kaise madad kru mai apki? ")

    if user_query.lower() in ['exit', 'quit']:
        print("Haanji theek hai fir milte hain next session mein chai ke saath. 👋")
        break

    try:
        result = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ]
        )

        
        print(result.choices[0].message.content)
        print("\n----------------------------------------\n")

    except Exception as e:
        print(f"Arre bhai, kuch error aa gaya: {e}")











