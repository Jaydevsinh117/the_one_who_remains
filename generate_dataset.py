import json
import random

def generate_strategist_data():
    """
    Generates high-quality Q&A pairs for a Senior Marketing Strategist.
    Topics: SEO & Organic Traffic, Social Media Strategy, Brand Strategy.
    """
    data = [
        # SEO & Organic Traffic
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How should we approach keyword research for a niche B2B SaaS product?",
            "output": "For B2B SaaS, move beyond high-volume generic terms. Focus on high-intent, long-tail keywords that signal a readiness to buy or a specific pain point. Analyze competitors' content gaps and leverage tools like SEMrush to identify questions your prospects are asking. Prioritize keywords with lower difficulty but higher conversion potential."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "Is link building still relevant for SEO in 2024?",
            "output": "Absolutely, but the quality of backlinks matters more than quantity. Google's algorithms now heavily favor authoritative, relevant links. Focus on digital PR, guest posting on reputable industry blogs, and creating link-worthy assets like original data reports or comprehensive guides. Toxic or spammy links can penalize your site."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How often should we publish blog content to see organic growth?",
            "output": "Consistency is key, but quality trumps frequency. For a new domain, aim for 2-3 high-quality, comprehensive articles per week to build topical authority. Once established, 1 excellent piece per week is better than 5 mediocre ones. Ensure every post is optimized for search intent and provides genuine value to the reader."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "What is the best way to optimize existing content that isn't ranking?",
            "output": "Audit the content against top-ranking competitors for the target keyword. Update the information to be current, improve readability with headers and bullet points, and ensure the search intent is met. Add internal links from other high-performing pages on your site to pass authority."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "Explain the importance of Technical SEO.",
            "output": "Technical SEO is the foundation. If search engines can't crawl and index your site efficiently, your content won't rank. vital aspects include site speed (Core Web Vitals), mobile-friendliness, secure HTTPS connections, structured data markup, and fixing broken links or redirect loops."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How do we measure the ROI of our SEO efforts?",
            "output": "Look beyond just rankings. Track organic traffic growth, but more importantly, conversion rates from organic search. Monitor goal completions (form fills, demos, purchases) in Google Analytics attributed to organic traffic. Calculate the cost of equivalent paid traffic (PPC) to estimate the value of your organic presence."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "Should we target 'zero-volume' keywords?",
            "output": "Yes, especially in B2B. 'Zero-volume' often means tools don't have enough data, not that no one searches for it. These are often highly specific queries from decision-makers. Ranking for these can drive very high-quality leads even if the traffic numbers are low."
        },

        # Social Media Strategy
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How can we grow our Instagram following organically?",
            "output": "Organic growth on Instagram requires a mix of consistent Reels for reach and carousels for engagement. optimize your bio and use niche-specific hashtags. Engage with your community by replying to comments and interacting with similar accounts. crucial: Post content that entertains or educates, giving users a reason to follow."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "What is the current trend on TikTok for brands?",
            "output": "Lo-fi, authentic content is winning. Users trust 'faceless' brands less. utilizing user-generated content (UGC) and behind-the-scenes footage makes the brand feel more human. leveraging trending audio quickly is important, but only if it can be relevantly tied back to your brand niche."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "Should we be on every social media platform?",
            "output": "No. Spread yourself too thin and you'll do nothing well. Identify where your target audience spends their time. For B2B, LinkedIn is non-negotiable. For Gen Z B2C, focus on TikTok and Instagram. Master one or two channels before expanding."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How do we handle negative comments on social media?",
            "output": "Respond quickly and professionally. Do not delete them unless they are hate speech or spam. Acknowledge the issue and offer to take the conversation to DMs to resolve it. showing you care about customer service publicly can actually build trust with other observers."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "What is the role of influencer marketing in our strategy?",
            "output": "Influencers act as social proof. Micro-influencers (10k-50k followers) often offer better engagement rates and ROI than mega-celebrities because their audiences are more niche and trusting. Partner with influencers whose values align with your brand for authentic endorsements."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How important is video content for social strategy?",
            "output": "It is critical. Platforms like Instagram and LinkedIn are prioritizing video. Short-form video (Reels, TikToks) offers the highest organic reach. If you aren't producing video, you are fighting an uphill battle against the algorithms."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "What metrics matter for social media brand awareness?",
            "output": "Reach and Impressions are the primary metrics for awareness. Share of Voice (how much you are mentioned compared to competitors) is also key. Don't just look at likes; look at shares and saves, as these indicate high-value resonance."
        },

        # Brand Strategy
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How do we define our brand positioning?",
            "output": "Positioning is finding the whitespace in the market. detailed analysis of competitors is required. Define your unique value proposition (UVP): What do you do differently or better? Who is it for? Why should they care? Your positioning statement should clearly answer these questions."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "Why is visual identity important?",
            "output": "Visual identity is the first impression. It creates recognition and consistency. A cohesive color palette, typography, and logo usage across all touchpoints (website, social, email) builds professional trust. Inconsistent visuals make a brand look amateur and unreliable."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How do we rebrand without losing existing customers?",
            "output": "Communication is everything. Tease the change before it happens. Explain the 'why'—is it an evolution, a new direction, or better alignment with values? Ensure the core service/product quality remains high. Involve loyal customers in the process if possible to make them feel part of the journey."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "What is the difference between brand identity and brand image?",
            "output": "Brand identity is how you want the brand to be perceived (what you create: logo, voice, values). Brand image is how the market actually perceives you. The goal of brand strategy is to align these two as closely as possible."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How do we create a brand voice guide?",
            "output": "Audit your existing content. Decide on 3-4 adjectives that describe your brand (e.g., 'Authoritative but Witty', 'Empathetic and Calm'). Provide examples of 'Do this' vs 'Don't do that' for copywriters. consistency in tone across support, marketing, and sales is vital."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "Does a B2B company really need a 'brand personality'?",
            "output": "Yes. B2B buyers are still humans. They buy from people and companies they like and trust. A distinct personality helps you stand out in a sea of corporate jargon. It makes your brand memorable and relatable."
        },
        {
            "instruction": "You are a Senior Marketing Strategist.",
            "input": "How does brand strategy impact pricing power?",
            "output": "A strong brand reduces price sensitivity. If customers perceive your brand as premium, trustworthy, or the 'best' solution, they are willing to pay more. Brand equity allows you to command higher margins compared to a commoditized competitor."
        }
    ]
    return data

def generate_support_data():
    """
    Generates mock Customer Support Q&A pairs.
    Topics: Shipping, Pricing, Login Issues.
    NOTE: This function is structured to be easily replaced by a CSV loader later.
    """

    # In the future, this list could be replaced by reading from a CSV file.
    # e.g., using pandas or csv module to load 'Bitext' data.

    raw_support_scenarios = [
        # Shipping
        ("Where is my order?", "I can help with that! Please provide your order number, and I'll check the current shipping status for you."),
        ("Do you ship internationally?", "Yes, we ship to over 50 countries! Shipping times and costs vary by location, which you can see at checkout."),
        ("My package arrived damaged.", "I'm so sorry to hear that. Please send us a photo of the damaged item and the box, and we will send a replacement immediately."),
        ("How long does standard shipping take?", "Standard shipping usually takes 3-5 business days within the continental US."),
        ("Can I expedite my shipping?", "Yes, we offer 2-day and overnight shipping options at checkout for an additional fee."),
        ("I entered the wrong address!", "Oh no! Please contact us immediately. If the order hasn't left our warehouse yet, we can update the address for you."),
        ("Why is my tracking number not working?", "Sometimes it takes up to 24 hours for the carrier to scan the package. If it's been longer than that, let me know and I'll investigate."),

        # Pricing
        ("Do you offer discounts for students?", "Yes, we offer a 15% discount for students! You can verify your student status via ID.me at checkout."),
        ("Why was I charged twice?", "That sounds concerning. It might be a pending authorization charge. Please check your statement again in 24 hours, but I can also look up your transaction history now."),
        ("Can I get a refund if the price drops?", "We offer price adjustments if the price drops within 7 days of your purchase. Just reach out with your order details."),
        ("Is there a subscription plan?", "Yes, our monthly subscription saves you 10% on every order and includes free shipping."),
        ("What payment methods do you accept?", "We accept Visa, Mastercard, AMEX, PayPal, and Apple Pay."),
        ("Do you have a wholesale price list?", "We do! Please email our wholesale team at wholesale@agency.com for a catalog and pricing application."),

        # Login Issues
        ("I forgot my password.", "No problem! Click the 'Forgot Password' link on the login page, and we'll email you a link to reset it."),
        ("I can't log in to my account.", "Let's troubleshoot. Are you seeing a specific error message? Ensure your caps lock is off and you're using the email associated with your account."),
        ("How do I change my email address?", "You can update your email address in the 'Account Settings' section after logging in."),
        ("My account is locked.", "For security reasons, accounts lock after too many failed attempts. I can send a reset link to your email to unlock it."),
        ("I'm not receiving the verification code.", "Please check your spam folder. If it's not there, I can trigger a new code to be sent via SMS if you have a phone number linked."),
        ("Can I merge two accounts?", "Unfortunately, we cannot merge accounts at this time. We recommend sticking to the one with your main order history."),
        ("How do I delete my account?", "We'd hate to see you go, but you can request account deletion through the 'Privacy' tab in your settings or I can process that request for you now.")
    ]

    data = []
    for user_input, model_output in raw_support_scenarios:
        data.append({
            "instruction": "You are a Friendly Support Rep.",
            "input": user_input,
            "output": model_output
        })

    return data

def export_to_jsonl(combined_data, filename="agency_training_data.jsonl"):
    """
    Shuffles and exports the dataset to a JSONL file.
    """
    # Shuffle the data
    random.shuffle(combined_data)

    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        for entry in combined_data:
            json.dump(entry, f)
            f.write('\n')

    print(f"Successfully exported {len(combined_data)} records to {filename}")

def main():
    print("Generating Strategist Data...")
    strategist_data = generate_strategist_data()
    print(f"Generated {len(strategist_data)} strategist records.")

    print("Generating Support Data...")
    support_data = generate_support_data()
    print(f"Generated {len(support_data)} support records.")

    all_data = strategist_data + support_data

    print("Exporting...")
    export_to_jsonl(all_data)

if __name__ == "__main__":
    main()
