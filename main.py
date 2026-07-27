import os
import json
import time
import requests
import subprocess

gemini_key = os.getenv("gemini_key", "weka_key_hapa")
suno_url = "https://api.suno.ai/v1/generate"
suno_key = os.getenv("suno_key", "weka_key_hapa")
replicate_key = os.getenv("replicate_key", "weka_key_hapa")
youtube_token = os.getenv("youtube_token", "weka_token_hapa")
instagram_token = os.getenv("instagram_token", "weka_token_hapa")
instagram_id = os.getenv("instagram_id", "weka_id_hapa")

def pata_maudhui_gemini():
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}"
    prompt = "Soma saikolojia ya watu mtandaoni. Tunga shairi fupi la Kiswahili litakaloenda viral. Pia tengeneza prompt 4 za video za sekunde 6. Toa majibu kwenye JSON yenye sehemu za lyrics na video_prompts."
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        raw_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        clean_json = raw_text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    return None

def tengeneza_wimbo(mashairi):
    headers = {"Authorization": f"Bearer {suno_key}", "Content-Type": "application/json"}
    payload = {"prompt": mashairi, "make_instrumental": False, "wait_audio": True}
    response = requests.post(suno_url, headers=headers, json=payload)
    if response.status_code == 200:
        audio_url = response.json()[0]["audio_url"]
        audio_data = requests.get(audio_url).content
        with open("wimbo.mp3", "wb") as f:
            f.write(audio_data)
        return "wimbo.mp3"
    return None

if __name__ == "__main__":
    print("Mchakato umeanza")
    data = pata_maudhui_gemini()
    if data:
        print("Gemini imerudisha mashairi")
        wimbo = tengeneza_wimbo(data["lyrics"])
        print("Wimbo umekamilika")
        
