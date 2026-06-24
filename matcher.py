def match_jobs(text, jobs):
    results = []

    text = text.lower()

    for j in jobs:
        score = 0
        keywords = ["python", "ai", "llm", "docker", "api", "sql"]

        for k in keywords:
            if k in text and k in j["desc"].lower():
                score += 20

        results.append({**j, "score": score})

    return sorted(results, key=lambda x: x["score"], reverse=True)